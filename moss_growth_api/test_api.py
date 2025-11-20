# ============================================================================
# API TESTING EXAMPLES
# ============================================================================
# Various ways to test and interact with your Moss Growth Prediction API
# ============================================================================

# ----------------------------------------------------------------------------
# 1. CURL COMMAND EXAMPLES
# ----------------------------------------------------------------------------

# Basic prediction request
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 22.5,
    "humidity": 70.0,
    "tds": 600.0,
    "ph": 6.4
  }'

# Health check
curl -X GET "http://localhost:8000/health"

# Root endpoint
curl -X GET "http://localhost:8000/"

# For production URL (replace with your Render URL)
curl -X POST "https://your-app-name.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 25.0,
    "humidity": 65.0,
    "tds": 550.0,
    "ph": 6.5
  }'


# ----------------------------------------------------------------------------
# 2. WINDOWS POWERSHELL EXAMPLES
# ----------------------------------------------------------------------------

# Using Invoke-RestMethod (PowerShell)
$body = @{
    temperature = 22.5
    humidity = 70.0
    tds = 600.0
    ph = 6.4
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/predict" `
  -Method POST `
  -Body $body `
  -ContentType "application/json"

# Health check (PowerShell)
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET


# ----------------------------------------------------------------------------
# 3. PYTHON REQUESTS LIBRARY
# ----------------------------------------------------------------------------

"""
Complete Python script to interact with the API
"""

import requests
import json

# Base URL (change for production)
BASE_URL = "http://localhost:8000"
# BASE_URL = "https://your-app-name.onrender.com"  # For production

def test_root():
    """Test the root endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print("Root Endpoint:")
    print(json.dumps(response.json(), indent=2))
    print("\n" + "="*70 + "\n")

def test_health():
    """Test the health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print("Health Check:")
    print(json.dumps(response.json(), indent=2))
    print("\n" + "="*70 + "\n")

def make_prediction(temperature, humidity, tds, ph):
    """
    Make a prediction request
    
    Args:
        temperature: float - Temperature in Celsius (18.0 - 35.0)
        humidity: float - Humidity percentage (50.0 - 80.0)
        tds: float - Total Dissolved Solids in ppm (400.0 - 800.0)
        ph: float - pH level (6.0 - 7.0)
    
    Returns:
        dict - Prediction results
    """
    
    # Prepare the request payload
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "tds": tds,
        "ph": ph
    }
    
    # Send POST request
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    # Check if request was successful
    if response.status_code == 200:
        result = response.json()
        print("Prediction Results:")
        print(f"  Temperature: {result['input_conditions']['temperature']}°C")
        print(f"  Humidity: {result['input_conditions']['humidity']}%")
        print(f"  TDS: {result['input_conditions']['tds']} ppm")
        print(f"  pH: {result['input_conditions']['ph']}")
        print(f"\n  🌱 Predicted Growth Days: {result['predicted_growth_days']} days")
        print(f"  📊 Interpretation: {result['interpretation']}")
        print(f"  🤖 Model Used: {result['model_used']}")
        print(f"  📈 Model Accuracy (R²): {result['model_accuracy_r2']}")
        return result
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

def batch_predictions():
    """Test multiple predictions with different conditions"""
    
    test_cases = [
        {
            "name": "Optimal Conditions",
            "temperature": 22.5,
            "humidity": 70.0,
            "tds": 600.0,
            "ph": 6.4
        },
        {
            "name": "Hot and Humid",
            "temperature": 30.0,
            "humidity": 75.0,
            "tds": 550.0,
            "ph": 6.5
        },
        {
            "name": "Cool Conditions",
            "temperature": 20.0,
            "humidity": 60.0,
            "tds": 650.0,
            "ph": 6.2
        },
        {
            "name": "High TDS",
            "temperature": 25.0,
            "humidity": 65.0,
            "tds": 750.0,
            "ph": 6.8
        }
    ]
    
    print("Batch Predictions Test")
    print("="*70)
    
    for case in test_cases:
        print(f"\n{case['name']}:")
        print("-"*70)
        make_prediction(
            temperature=case['temperature'],
            humidity=case['humidity'],
            tds=case['tds'],
            ph=case['ph']
        )
        print()

def test_validation_errors():
    """Test validation with invalid inputs"""
    
    print("Testing Validation Errors:")
    print("="*70)
    
    # Test invalid temperature
    print("\n1. Invalid Temperature (too low):")
    response = requests.post(
        f"{BASE_URL}/predict",
        json={"temperature": 15.0, "humidity": 70.0, "tds": 600.0, "ph": 6.4}
    )
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json()['detail']}")
    
    # Test invalid humidity
    print("\n2. Invalid Humidity (too high):")
    response = requests.post(
        f"{BASE_URL}/predict",
        json={"temperature": 22.5, "humidity": 90.0, "tds": 600.0, "ph": 6.4}
    )
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json()['detail']}")
    
    # Test missing parameter
    print("\n3. Missing Parameter:")
    response = requests.post(
        f"{BASE_URL}/predict",
        json={"temperature": 22.5, "humidity": 70.0, "tds": 600.0}
    )
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json()['detail'][0]['msg']}")

# ----------------------------------------------------------------------------
# MAIN EXECUTION
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    print("="*70)
    print(" MOSS GROWTH PREDICTION API - TEST SUITE ".center(70, "="))
    print("="*70)
    print()
    
    try:
        # Test 1: Root endpoint
        test_root()
        
        # Test 2: Health check
        test_health()
        
        # Test 3: Single prediction
        print("Single Prediction Test:")
        print("="*70)
        make_prediction(
            temperature=22.5,
            humidity=70.0,
            tds=600.0,
            ph=6.4
        )
        print("\n" + "="*70 + "\n")
        
        # Test 4: Batch predictions
        batch_predictions()
        print("="*70 + "\n")
        
        # Test 5: Validation errors
        test_validation_errors()
        print("\n" + "="*70)
        
        print("\n✅ All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API")
        print("Make sure the server is running at", BASE_URL)
        print("\nTo start the server, run:")
        print("  python main.py")
        print("or")
        print("  uvicorn main:app --reload")


# ----------------------------------------------------------------------------
# 4. JAVASCRIPT/FETCH API EXAMPLE
# ----------------------------------------------------------------------------

"""
// JavaScript example for frontend integration

// Function to make prediction
async function predictGrowthDays(temperature, humidity, tds, ph) {
    const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            temperature: temperature,
            humidity: humidity,
            tds: tds,
            ph: ph
        })
    });
    
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
}

// Usage example
predictGrowthDays(22.5, 70.0, 600.0, 6.4)
    .then(result => {
        console.log('Predicted Growth Days:', result.predicted_growth_days);
        console.log('Interpretation:', result.interpretation);
        console.log('Model Used:', result.model_used);
        console.log('Model Accuracy:', result.model_accuracy_r2);
    })
    .catch(error => {
        console.error('Error:', error);
    });

// React example with hooks
import React, { useState } from 'react';

function MossGrowthPredictor() {
    const [formData, setFormData] = useState({
        temperature: 22.5,
        humidity: 70.0,
        tds: 600.0,
        ph: 6.4
    });
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        
        try {
            const response = await fetch('http://localhost:8000/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            setPrediction(data);
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Moss Growth Predictor</h2>
            <form onSubmit={handleSubmit}>
                <input 
                    type="number" 
                    value={formData.temperature}
                    onChange={(e) => setFormData({...formData, temperature: parseFloat(e.target.value)})}
                    placeholder="Temperature"
                />
                {/* Add other inputs... *\/}
                <button type="submit" disabled={loading}>
                    {loading ? 'Predicting...' : 'Predict'}
                </button>
            </form>
            
            {prediction && (
                <div>
                    <h3>Prediction: {prediction.predicted_growth_days} days</h3>
                    <p>{prediction.interpretation}</p>
                </div>
            )}
        </div>
    );
}
"""
