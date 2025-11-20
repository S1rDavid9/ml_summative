"""
PREDICTION SCRIPT - Moss Growth Prediction System
Auto-generated with correct feature names
"""

import joblib
import numpy as np
import pandas as pd
import json

def load_model():
    """Load the saved model and scaler"""
    try:
        model = joblib.load('best_model.pkl')
        scaler = joblib.load('scaler.pkl')

        with open('model_info.json', 'r') as f:
            model_info = json.load(f)

        return model, scaler, model_info
    except FileNotFoundError as e:
        print(f"Error: Required file not found - {e}")
        return None, None, None

def predict_growth_days(temperature, humidity, tds, ph):
    """
    Predict growth days based on environmental factors

    Parameters:
    -----------
    temperature : float - Temperature in Celsius
    humidity : float - Humidity percentage
    tds : float - Total Dissolved Solids in ppm
    ph : float - pH level

    Returns:
    --------
    float : Predicted growth days
    dict : Input conditions and prediction details
    """
    model, scaler, model_info = load_model()

    if model is None:
        return None, None

    # Get actual feature names from model
    feature_names = model_info['features']

    # Create input with exact feature names from training
    input_values = [temperature, humidity, tds, ph]
    input_data = pd.DataFrame([input_values], columns=feature_names)

    # Standardize and predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    result = {
        'input_conditions': {
            'temperature': temperature,
            'humidity': humidity,
            'tds': tds,
            'ph': ph
        },
        'predicted_growth_days': round(prediction, 2),
        'model_used': model_info['model_name'],
        'model_accuracy_r2': round(model_info['test_r2'], 4)
    }

    return prediction, result

def get_interpretation(predicted_days):
    """Provide interpretation of predicted growth days"""
    if predicted_days < 15:
        return "Very fast growth - Excellent conditions"
    elif predicted_days < 25:
        return "Fast growth - Good conditions"
    elif predicted_days < 35:
        return "Moderate growth - Acceptable conditions"
    else:
        return "Slow growth - Suboptimal conditions"

# Test the function
if __name__ == "__main__":
    print("="*70)
    print(" MOSS GROWTH PREDICTION SYSTEM ".center(70, "="))
    print("="*70)

    model, scaler, model_info = load_model()

    if model:
        print(f"\nModel: {model_info['model_name']}")
        print(f"Features: {model_info['features']}")
        print(f"R² Score: {model_info['test_r2']:.4f}")

        print("\n" + "="*70)
        print("Example Prediction:")
        print("="*70)

        pred, details = predict_growth_days(22.5, 70, 600, 6.4)
        if pred:
            print(f"Predicted: {pred:.2f} days")
            print(f"{get_interpretation(pred)}")
