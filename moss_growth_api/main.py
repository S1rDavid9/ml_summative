"""
MOSS GROWTH PREDICTION API
FastAPI application for deploying machine learning model
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import Dict
import os
import json
from pathlib import Path

# Import the prediction function
from predict import predict_growth_days, load_model

# ============================================================================
# API METADATA
# ============================================================================
app = FastAPI(
    title="Moss Growth Prediction API",
    description="""
    ## 🌱 Moss Growth Prediction System
    
    This API predicts the number of days required for moss growth based on 
    environmental conditions using a trained Random Forest machine learning model.
    
    ### Features:
    - **Real-time predictions** based on temperature, humidity, TDS, and pH
    - **Data validation** with appropriate range constraints
    - **Model performance metrics** included in responses
    - **Health check** endpoint for monitoring
    
    ### Model Information:
    - **Algorithm**: Random Forest Regressor
    - **Training Accuracy**: R² Score ~0.624
    - **Input Features**: 4 environmental parameters
    
    ### Usage:
    1. Use the `/predict` endpoint with POST request
    2. Provide JSON body with environmental parameters
    3. Receive prediction with model details
    
    ---
    Built with FastAPI and scikit-learn
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ============================================================================
# CORS MIDDLEWARE CONFIGURATION
# ============================================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ============================================================================
# PYDANTIC MODELS FOR DATA VALIDATION
# ============================================================================

class PredictionInput(BaseModel):
    """
    Input model for moss growth prediction with validation constraints.
    
    All parameters must fall within scientifically valid ranges for moss growth.
    """
    
    temperature: float = Field(
        ...,
        ge=18.0,
        le=35.0,
        description="Temperature in degrees Celsius",
        example=22.5
    )
    
    humidity: float = Field(
        ...,
        ge=50.0,
        le=80.0,
        description="Relative humidity percentage",
        example=70.0
    )
    
    tds: float = Field(
        ...,
        ge=400.0,
        le=800.0,
        description="Total Dissolved Solids in parts per million (ppm)",
        example=600.0
    )
    
    ph: float = Field(
        ...,
        ge=6.0,
        le=7.0,
        description="pH level of the growing medium",
        example=6.4
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "temperature": 22.5,
                "humidity": 70.0,
                "tds": 600.0,
                "ph": 6.4
            }
        }
    
    @validator('temperature')
    def validate_temperature(cls, v):
        """Ensure temperature is within optimal range"""
        if v < 18.0 or v > 35.0:
            raise ValueError('Temperature must be between 18.0°C and 35.0°C')
        return round(v, 2)
    
    @validator('humidity')
    def validate_humidity(cls, v):
        """Ensure humidity is within optimal range"""
        if v < 50.0 or v > 80.0:
            raise ValueError('Humidity must be between 50.0% and 80.0%')
        return round(v, 2)
    
    @validator('tds')
    def validate_tds(cls, v):
        """Ensure TDS is within optimal range"""
        if v < 400.0 or v > 800.0:
            raise ValueError('TDS must be between 400.0 ppm and 800.0 ppm')
        return round(v, 2)
    
    @validator('ph')
    def validate_ph(cls, v):
        """Ensure pH is within optimal range"""
        if v < 6.0 or v > 7.0:
            raise ValueError('pH must be between 6.0 and 7.0')
        return round(v, 2)


class PredictionOutput(BaseModel):
    """
    Output model for prediction results with comprehensive details.
    """
    
    predicted_growth_days: float = Field(
        ...,
        description="Predicted number of days for moss growth",
        example=18.45
    )
    
    input_conditions: Dict[str, float] = Field(
        ...,
        description="Echo of the input environmental conditions",
        example={
            "temperature": 22.5,
            "humidity": 70.0,
            "tds": 600.0,
            "ph": 6.4
        }
    )
    
    model_used: str = Field(
        ...,
        description="Name of the machine learning model used for prediction",
        example="Random Forest"
    )
    
    model_accuracy_r2: float = Field(
        ...,
        description="R² score of the model on test data (coefficient of determination)",
        example=0.624
    )
    
    interpretation: str = Field(
        ...,
        description="Human-readable interpretation of the prediction",
        example="Fast growth - Good conditions"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "predicted_growth_days": 18.45,
                "input_conditions": {
                    "temperature": 22.5,
                    "humidity": 70.0,
                    "tds": 600.0,
                    "ph": 6.4
                },
                "model_used": "Random Forest",
                "model_accuracy_r2": 0.624,
                "interpretation": "Fast growth - Good conditions"
            }
        }


class HealthResponse(BaseModel):
    """Response model for health check endpoint"""
    status: str
    model_loaded: bool
    model_name: str = None
    model_accuracy: float = None
    message: str


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_interpretation(predicted_days: float) -> str:
    """
    Provide interpretation of predicted growth days
    
    Args:
        predicted_days: Predicted number of days for moss growth
        
    Returns:
        Human-readable interpretation string
    """
    if predicted_days < 15:
        return "Very fast growth - Excellent conditions"
    elif predicted_days < 25:
        return "Fast growth - Good conditions"
    elif predicted_days < 35:
        return "Moderate growth - Acceptable conditions"
    else:
        return "Slow growth - Suboptimal conditions"


def check_model_files() -> tuple:
    """
    Check if all required model files exist
    
    Returns:
        Tuple of (all_exist: bool, missing_files: list)
    """
    required_files = ['best_model.pkl', 'scaler.pkl', 'model_info.json']
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    return len(missing_files) == 0, missing_files


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """
    **Root endpoint - API Welcome Message**
    
    Returns basic information about the API and links to documentation.
    
    - **Returns**: Welcome message with API details and navigation links
    """
    return {
        "message": "🌱 Welcome to the Moss Growth Prediction API",
        "version": "1.0.0",
        "description": "Predict moss growth days based on environmental conditions",
        "model": "Random Forest Regressor",
        "documentation": {
            "swagger_ui": "/docs",
            "redoc": "/redoc"
        },
        "endpoints": {
            "predict": "POST /predict - Make growth predictions",
            "health": "GET /health - Check API and model status",
            "docs": "GET /docs - Interactive API documentation"
        },
        "usage": "Send POST request to /predict with temperature, humidity, tds, and ph values"
    }


@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
async def health_check():
    """
    **Health Check Endpoint**
    
    Checks the status of the API and verifies that all required model files are present.
    Use this endpoint for monitoring and deployment health checks.
    
    - **Returns**: Health status including model availability and accuracy metrics
    """
    # Check if model files exist
    files_exist, missing_files = check_model_files()
    
    if not files_exist:
        return HealthResponse(
            status="unhealthy",
            model_loaded=False,
            message=f"Missing required files: {', '.join(missing_files)}"
        )
    
    # Try to load the model
    try:
        model, scaler, model_info = load_model()
        
        if model is None:
            return HealthResponse(
                status="unhealthy",
                model_loaded=False,
                message="Failed to load model files"
            )
        
        return HealthResponse(
            status="healthy",
            model_loaded=True,
            model_name=model_info['model_name'],
            model_accuracy=round(model_info['test_r2'], 4),
            message="API is operational and model is loaded successfully"
        )
        
    except Exception as e:
        return HealthResponse(
            status="unhealthy",
            model_loaded=False,
            message=f"Error loading model: {str(e)}"
        )


@app.post("/predict", response_model=PredictionOutput, tags=["Predictions"])
async def predict(input_data: PredictionInput):
    """
    **Make Moss Growth Prediction**
    
    Predicts the number of days required for moss growth based on environmental conditions.
    
    The model uses Random Forest regression trained on historical moss growth data.
    All input parameters are validated against scientifically valid ranges.
    
    **Parameters:**
    - **temperature**: Temperature in Celsius (18.0 - 35.0°C)
    - **humidity**: Relative humidity percentage (50.0 - 80.0%)
    - **tds**: Total Dissolved Solids in ppm (400.0 - 800.0 ppm)
    - **ph**: pH level of growing medium (6.0 - 7.0)
    
    **Returns:**
    - **predicted_growth_days**: Predicted number of days for moss growth
    - **input_conditions**: Echo of input parameters
    - **model_used**: Name of the ML model
    - **model_accuracy_r2**: R² score of the model
    - **interpretation**: Human-readable interpretation of the result
    
    **Example Request:**
    ```json
    {
        "temperature": 22.5,
        "humidity": 70.0,
        "tds": 600.0,
        "ph": 6.4
    }
    ```
    
    **Error Responses:**
    - **422**: Validation error - input values outside valid ranges
    - **500**: Model loading or prediction error
    """
    try:
        # Make prediction using the imported function
        prediction, result = predict_growth_days(
            temperature=input_data.temperature,
            humidity=input_data.humidity,
            tds=input_data.tds,
            ph=input_data.ph
        )
        
        # Check if prediction was successful
        if prediction is None or result is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to load model or make prediction. Please check model files."
            )
        
        # Add interpretation to the result
        interpretation = get_interpretation(prediction)
        
        # Prepare response
        response = PredictionOutput(
            predicted_growth_days=round(prediction, 2),
            input_conditions=result['input_conditions'],
            model_used=result['model_used'],
            model_accuracy_r2=result['model_accuracy_r2'],
            interpretation=interpretation
        )
        
        return response
        
    except ValueError as ve:
        # Handle validation errors
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Validation error: {str(ve)}"
        )
        
    except FileNotFoundError as fe:
        # Handle missing model files
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Model file not found: {str(fe)}"
        )
        
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction error: {str(e)}"
        )


# ============================================================================
# APPLICATION STARTUP
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """
    Actions to perform on application startup
    """
    print("=" * 70)
    print(" MOSS GROWTH PREDICTION API ".center(70, "="))
    print("=" * 70)
    
    # Verify model files exist
    files_exist, missing_files = check_model_files()
    
    if files_exist:
        print("✓ All model files found")
        
        # Try to load model
        try:
            model, scaler, model_info = load_model()
            if model is not None:
                print(f"✓ Model loaded: {model_info['model_name']}")
                print(f"✓ R² Score: {model_info['test_r2']:.4f}")
                print(f"✓ Features: {len(model_info['features'])}")
            else:
                print("✗ Failed to load model")
        except Exception as e:
            print(f"✗ Error loading model: {e}")
    else:
        print("✗ Missing model files:")
        for file in missing_files:
            print(f"  - {file}")
    
    print("=" * 70)
    print("API is ready to accept requests")
    print("Documentation available at: /docs")
    print("=" * 70)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform on application shutdown
    """
    print("\nShutting down Moss Growth Prediction API...")


# ============================================================================
# MAIN ENTRY POINT (for local development)
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment variable or use default
    port = int(os.environ.get("PORT", 8000))
    
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Bind to all interfaces for deployment
        port=port,
        reload=True  # Enable auto-reload for development
    )
