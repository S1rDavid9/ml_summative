# ============================================================================
# QUICK REFERENCE GUIDE
# ============================================================================

## 🚀 STARTING THE API

### Option 1: Using Python directly
```bash
python main.py
```

### Option 2: Using uvicorn
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 3: Using the batch file (Windows)
```bash
start_server.bat
```

---

## 📡 TESTING ENDPOINTS

### 1. Open Swagger UI
Navigate to: http://localhost:8000/docs

### 2. Test Health Endpoint
**PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET
```

**Browser:**
```
http://localhost:8000/health
```

### 3. Make a Prediction
**PowerShell:**
```powershell
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
```

**Python:**
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

---

## 📊 EXAMPLE PREDICTIONS

### Optimal Conditions
```json
{
  "temperature": 22.5,
  "humidity": 70.0,
  "tds": 600.0,
  "ph": 6.4
}
```
Expected: ~18-20 days (Fast growth)

### Hot and Humid
```json
{
  "temperature": 30.0,
  "humidity": 75.0,
  "tds": 550.0,
  "ph": 6.5
}
```
Expected: Variable (depends on model training)

### Cool Conditions
```json
{
  "temperature": 20.0,
  "humidity": 60.0,
  "tds": 650.0,
  "ph": 6.2
}
```
Expected: Moderate growth

---

## 🔧 TROUBLESHOOTING

### Port already in use
```bash
uvicorn main:app --port 8001
```

### Virtual environment not activated
```bash
# Windows
..\venv\Scripts\activate

# Then run the server
python main.py
```

### Missing packages
```bash
pip install -r requirements.txt
```

### Model files not found
Ensure these files are in the moss_growth_api folder:
- best_model.pkl
- scaler.pkl
- model_info.json

---

## 📦 VALIDATION RANGES

| Parameter | Min | Max | Unit |
|-----------|-----|-----|------|
| Temperature | 18.0 | 35.0 | °C |
| Humidity | 50.0 | 80.0 | % |
| TDS | 400.0 | 800.0 | ppm |
| pH | 6.0 | 7.0 | - |

---

## 🌐 DEPLOYMENT CHECKLIST

- [ ] All required packages installed
- [ ] Model files (.pkl) present
- [ ] API runs locally without errors
- [ ] /health endpoint returns "healthy"
- [ ] /predict endpoint accepts test data
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Web service configured
- [ ] Environment variables set (if any)
- [ ] Deployment successful
- [ ] Production URL working

---

## 📚 USEFUL COMMANDS

### Check Python version
```bash
python --version
```

### List installed packages
```bash
pip list
```

### Run tests
```bash
python test_api.py
```

### View API logs (when running)
Watch the terminal output for request logs

---

## 🔗 IMPORTANT URLS

**Local Development:**
- API Root: http://localhost:8000/
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

**Production (Render):**
- Replace `localhost:8000` with your Render URL
- Example: `https://moss-growth-api.onrender.com`

---

## 💡 TIPS

1. **Always test locally first** before deploying
2. **Use /docs** for interactive API testing
3. **Check /health** to verify model is loaded
4. **Monitor logs** for debugging issues
5. **Use virtual environment** to avoid conflicts
6. **Commit .pkl files** to git for deployment

---

## 📞 NEED HELP?

- Check README.md for detailed documentation
- See DEPLOYMENT_GUIDE.md for deployment steps
- Review test_api.py for usage examples
- Visit FastAPI docs: https://fastapi.tiangolo.com
