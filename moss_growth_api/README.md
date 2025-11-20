# 🌱 Moss Growth Prediction API

A production-ready FastAPI application for predicting moss growth days based on environmental conditions using machine learning.

## 📋 Overview

This API uses a trained **Random Forest Regressor** model to predict the number of days required for moss growth based on four environmental parameters:
- Temperature (°C)
- Humidity (%)
- Total Dissolved Solids - TDS (ppm)
- pH Level

**Model Performance:**
- R² Score: ~0.624
- RMSE: ~8.06 days
- MAE: ~4.83 days

---

## 🚀 Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```
   
   Or with uvicorn:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Access the API:**
   - **Swagger UI**: http://localhost:8000/docs
   - **ReDoc**: http://localhost:8000/redoc
   - **API Root**: http://localhost:8000/

---

## 📡 API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns welcome message and API information.

### 2. Health Check
```
GET /health
```
Checks API status and model availability.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_name": "Random Forest",
  "model_accuracy": 0.624,
  "message": "API is operational and model is loaded successfully"
}
```

### 3. Make Prediction
```
POST /predict
```

**Request Body:**
```json
{
  "temperature": 22.5,
  "humidity": 70.0,
  "tds": 600.0,
  "ph": 6.4
}
```

**Validation Ranges:**
- `temperature`: 18.0 - 35.0 °C
- `humidity`: 50.0 - 80.0 %
- `tds`: 400.0 - 800.0 ppm
- `ph`: 6.0 - 7.0

**Response:**
```json
{
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
```

---

## 🧪 Testing the API

### Using curl

**Make a prediction:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 22.5,
    "humidity": 70.0,
    "tds": 600.0,
    "ph": 6.4
  }'
```

**Health check:**
```bash
curl -X GET "http://localhost:8000/health"
```

### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "temperature": 22.5,
        "humidity": 70.0,
        "tds": 600.0,
        "ph": 6.4
    }
)

print(response.json())
```

### Using the Test Suite

Run the comprehensive test suite:
```bash
python test_api.py
```

---

## 📦 Project Structure

```
moss_growth_api/
├── main.py                 # FastAPI application
├── predict.py              # Prediction logic
├── requirements.txt        # Python dependencies
├── best_model.pkl          # Trained ML model
├── scaler.pkl              # Data scaler
├── model_info.json         # Model metadata
├── test_api.py             # API testing suite
├── DEPLOYMENT_GUIDE.md     # Deployment instructions
└── README.md               # This file
```

---

## 🌐 Deployment

### Deploy to Render

See **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** for detailed deployment instructions.

**Quick steps:**
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect your repository
4. Set root directory to `moss_growth_api`
5. Use build command: `pip install -r requirements.txt`
6. Use start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Deploy!

Your API will be live at: `https://your-app-name.onrender.com`

---

## 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Port to run the server | 8000 |

---

## 📚 Documentation

Once the server is running:
- **Interactive API Docs (Swagger UI)**: `/docs`
- **Alternative Docs (ReDoc)**: `/redoc`
- **OpenAPI Schema**: `/openapi.json`

---

## 🛠️ Technologies Used

- **FastAPI** - Modern web framework
- **Pydantic** - Data validation
- **scikit-learn** - Machine learning
- **pandas** - Data manipulation
- **joblib** - Model serialization
- **uvicorn** - ASGI server

---

## 📊 Model Information

- **Algorithm**: Random Forest Regressor
- **Features**: Temperature, Humidity, TDS, pH
- **Target**: Growth Days
- **Training Data**: Historical moss growth measurements
- **Preprocessing**: StandardScaler for feature normalization

---

## ⚠️ Error Handling

The API includes comprehensive error handling:

- **422 Unprocessable Entity**: Invalid input (out of range values)
- **500 Internal Server Error**: Model loading or prediction errors
- **Automatic validation**: Pydantic validates all inputs

---

## 🔒 CORS Configuration

CORS is enabled to allow cross-origin requests from any domain. For production, update `main.py` to specify allowed origins:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourfrontend.com"],  # Specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📈 Growth Interpretation

The API provides interpretation based on predicted days:

| Days | Interpretation |
|------|----------------|
| < 15 | Very fast growth - Excellent conditions |
| 15-25 | Fast growth - Good conditions |
| 25-35 | Moderate growth - Acceptable conditions |
| > 35 | Slow growth - Suboptimal conditions |

---

## 🐛 Troubleshooting

### Model files not found
Ensure all `.pkl` files are in the same directory as `main.py`

### Import errors
Install all dependencies: `pip install -r requirements.txt`

### Port already in use
Change port: `uvicorn main:app --port 8001`

### Validation errors
Check input ranges match the validation constraints

---

## 📝 License

This project is part of an ML summative assessment.

---

## 👤 Author

**GitHub**: [@S1rDavid9](https://github.com/S1rDavid9)  
**Repository**: ml_summative

---

## 🙏 Acknowledgments

- Built with FastAPI framework
- Machine learning with scikit-learn
- Deployed on Render

---

**For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**

**For API testing examples, see [test_api.py](test_api.py)**
