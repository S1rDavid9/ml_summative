# 🌱 Moss Growth Prediction System

## 📋 Mission & Problem Statement

This project addresses the challenge of predicting moss growth time based on environmental conditions. Moss cultivation requires careful monitoring of temperature, humidity, total dissolved solids (TDS), and pH levels. This machine learning system provides accurate growth time predictions (in days) to help cultivators optimize growing conditions and plan harvests efficiently. The solution includes a trained Random Forest model, a REST API deployed on Render, and a mobile application for easy access.

---

## 🎥 Video Demo

📺 **[Demo Video](#)** https://www.loom.com/share/b2815d47085f4d1c97c9f5b14528d632

The demo video covers:
- Mobile app making predictions
- Flutter API integration code walkthrough
- Swagger UI testing (valid inputs and validation errors)
- Model training and comparison (Linear Regression, Decision Tree, Random Forest)
- Performance metrics (R², MSE) and model selection justification

---

## 🚀 Live API Endpoint

**Base URL:** `https://moss-growth-api.onrender.com`

### Available Endpoints:

- **Root:** `GET /` - Welcome message
- **Health Check:** `GET /health` - API status and model info
- **Prediction:** `POST /predict` - Make growth predictions
- **Interactive Documentation:** `GET /docs` - Swagger UI for testing

### Test the API (Swagger UI):
🔗 **[https://moss-growth-api.onrender.com/docs](https://moss-growth-api.onrender.com/docs)**

### Sample API Request:
```bash
curl -X POST "https://moss-growth-api.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 22.5,
    "humidity": 70.0,
    "tds": 600.0,
    "ph": 6.4
  }'
```

### Sample API Response:
```json
{
  "predicted_growth_days": 16,
  "interpretation": "Fast growth - Good conditions",
  "model_used": "Random Forest"
}
```

### Input Validation Ranges:
- **Temperature:** 18-35°C
- **Humidity:** 50-80%
- **TDS:** 400-800 ppm
- **pH:** 6.0-7.0

---


## 📦 Project Structure

```
ml_summative/
├── linear_regression/
│   └── Moss_growth_model.ipynb      # Model training notebook
├── moss_growth_api/
│   ├── main.py                       # FastAPI application
│   ├── predict.py                    # Prediction logic
│   ├── requirements.txt              # Python dependencies
│   ├── best_model.pkl                # Trained Random Forest model
│   ├── scaler.pkl                    # Feature scaler
│   ├── model_info.json               # Model metadata
│   ├── README.md                     # API documentation
│   ├── DEPLOYMENT_GUIDE.md           # Deployment instructions
│   └── QUICK_REFERENCE.md            # API quick reference
└── flutter_app/
    └── moss_growth_app/
        ├── lib/
        │   ├── main.dart             # App entry point
        │   ├── constants/            # App constants
        │   ├── models/               # Data models
        │   ├── screens/              # UI screens
        │   └── services/             # API service
        ├── pubspec.yaml              # Flutter dependencies
        └── README.md                 # Flutter app documentation
```

---

## 📱 How to Run the Mobile App

### Prerequisites

Before running the app, ensure you have:

1. **Flutter SDK** (version 3.0 or higher)
   - Download from: https://flutter.dev/docs/get-started/install
   - Verify installation: `flutter --version`

2. **Dart SDK** (comes with Flutter)

3. **IDE** (choose one):
   - Android Studio with Flutter plugin
   - VS Code with Flutter extension
   - IntelliJ IDEA with Flutter plugin

4. **Device/Emulator** (choose one):
   - Android device with USB debugging enabled
   - Android emulator (via Android Studio)
   - iOS device (Mac only)
   - iOS simulator (Mac only)
   - Chrome browser (for web version)
   - Windows (for desktop version)

---

### Installation Steps

#### Step 1: Clone the Repository
```bash
git clone https://github.com/S1rDavid9/ml_summative.git
cd ml_summative/flutter_app/moss_growth_app
```

#### Step 2: Install Flutter Dependencies
```bash
flutter pub get
```

This will download all required packages:
- `http` - For API communication
- `google_fonts` - For custom typography
- `cupertino_icons` - For iOS-style icons

#### Step 3: Verify Flutter Setup
```bash
flutter doctor
```

This command checks your environment and displays a report of the status of your Flutter installation. Fix any issues reported.

#### Step 4: Check Available Devices
```bash
flutter devices
```

This lists all connected devices and emulators.

---

### Running the App

#### Option 1: Run on Android Device/Emulator

1. **Connect your Android device** via USB (with USB debugging enabled) or **start an Android emulator**

2. **Verify device is detected:**
   ```bash
   flutter devices
   ```

3. **Run the app:**
   ```bash
   flutter run
   ```
   
   Or specify the device:
   ```bash
   flutter run -d <device_id>
   ```

4. The app will compile and launch on your device (first build may take 2-5 minutes)

#### Option 2: Run on iOS Device/Simulator (Mac only)

1. **Open Xcode** and accept license agreements

2. **Start iOS simulator** or connect iOS device

3. **Run the app:**
   ```bash
   flutter run
   ```

#### Option 3: Run on Chrome (Web Version)

1. **Ensure Chrome is installed**

2. **Run the app:**
   ```bash
   flutter run -d chrome
   ```

3. A Chrome window will open with your app

#### Option 4: Run on Windows Desktop

1. **Run the app:**
   ```bash
   flutter run -d windows
   ```

2. A Windows desktop application will launch

---

### Using the App

1. **Enter Environmental Parameters:**
   - Temperature: 18-35°C
   - Humidity: 50-80%
   - TDS: 400-800 ppm
   - pH: 6.0-7.0

2. **Tap Info Icons (ℹ️)** for parameter descriptions

3. **Press "PREDICT GROWTH"** button

4. **View Results:**
   - Predicted growth days
   - Interpretation (color-coded)
   - Model information

5. **Make Another Prediction:**
   - Tap "CLEAR ALL" to reset
   - Enter new values

---

### Building Release Versions

#### Android APK (for distribution)
```bash
flutter build apk --release
```
Output: `build/app/outputs/flutter-apk/app-release.apk`

#### Android App Bundle (for Google Play Store)
```bash
flutter build appbundle --release
```

#### iOS (for App Store - Mac only)
```bash
flutter build ios --release
```

---

### Troubleshooting

**Issue: "Unable to connect to server"**
- Check internet connection
- Verify API is awake (first request may take 30-60s on Render free tier)
- Visit: https://moss-growth-api.onrender.com/health

**Issue: "Request timed out"**
- API may be cold starting
- Wait and try again

**Issue: Build errors**
```bash
flutter clean
flutter pub get
flutter run
```

**Issue: No devices found**
- Start an emulator: `flutter emulators --launch <emulator_id>`
- Or enable USB debugging on physical device

**Issue: Hot reload not working**
- Press `R` (capital R) for hot restart in terminal
- Or restart the app completely

---

## 🤖 Machine Learning Model

### Models Trained & Compared:
1. **Linear Regression** - R² = 0.52
2. **Decision Tree** - R² = 0.58
3. **Random Forest** - R² = 0.624 ✅ (Selected)

### Why Random Forest?
- Best performance (R² = 0.624, lowest MSE)
- Handles non-linear relationships between environmental factors
- Reduces overfitting compared to single decision tree
- Robust to feature interactions

### Model Files:
- `best_model.pkl` - Trained Random Forest regressor
- `scaler.pkl` - StandardScaler for feature normalization
- `model_info.json` - Model metadata and performance metrics

For detailed model training process, see: `linear_regression/Moss_growth_model.ipynb`

---

## 🛠️ Technology Stack

### Backend:
- **Python 3.13**
- **FastAPI** - REST API framework
- **Scikit-learn** - Machine learning
- **Pandas & NumPy** - Data processing
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### Frontend:
- **Flutter 3.x** - Cross-platform mobile framework
- **Dart** - Programming language
- **HTTP package** - API communication
- **Google Fonts** - Typography
- **Material Design 3** - UI components

### Deployment:
- **Render.com** - API hosting
- **GitHub** - Version control

---

## 📊 API Documentation

For complete API documentation, see:
- **[moss_growth_api/README.md](./moss_growth_api/README.md)** - Full API guide
- **[moss_growth_api/DEPLOYMENT_GUIDE.md](./moss_growth_api/DEPLOYMENT_GUIDE.md)** - Deployment steps
- **[moss_growth_api/QUICK_REFERENCE.md](./moss_growth_api/QUICK_REFERENCE.md)** - Quick reference

---

## 📱 Flutter App Documentation

For complete Flutter app documentation, see:
- **[flutter_app/moss_growth_app/README.md](./flutter_app/moss_growth_app/README.md)** - Comprehensive guide

---

## 🧪 Testing the System

### Test the API (Swagger UI):
1. Visit: https://moss-growth-api.onrender.com/docs
2. Click on `/predict` endpoint
3. Click "Try it out"
4. Enter test values:
   ```json
   {
     "temperature": 22.5,
     "humidity": 70.0,
     "tds": 600.0,
     "ph": 6.4
   }
   ```
5. Click "Execute"
6. View the prediction response

### Test Input Validation:
Try invalid values (e.g., temperature: 45) to see validation errors (422 response)

### Test the Mobile App:
1. Follow installation steps above
2. Run the app on your device
3. Enter test values and make predictions
4. Verify results match API predictions

---

## 📄 Files Included

### Machine Learning:
- ✅ Jupyter notebook with model training
- ✅ Comparison of 3 models (Linear, Decision Tree, Random Forest)
- ✅ Performance metrics (R², MSE)
- ✅ Trained model files (.pkl)

### API:
- ✅ FastAPI application code
- ✅ Prediction logic
- ✅ Input validation
- ✅ Error handling
- ✅ Deployed on Render (public URL)

### Mobile App:
- ✅ Complete Flutter application
- ✅ API integration
- ✅ Input validation
- ✅ Error handling
- ✅ Beautiful UI with animations

### Documentation:
- ✅ README files for each component
- ✅ Deployment guides
- ✅ Demo video script

---

## 🎓 Academic Context

This project demonstrates:
- End-to-end machine learning pipeline
- Model training, evaluation, and selection
- REST API development and deployment
- Mobile application development
- Full-stack integration
- Production-ready code with error handling
- Professional documentation

---

## 👤 Author

**GitHub:** [@S1rDavid9](https://github.com/S1rDavid9)  
**Repository:** [ml_summative](https://github.com/S1rDavid9/ml_summative)

---

## 📞 Support & Contact

For issues or questions:
1. Check the documentation in respective README files
2. Verify API status: https://moss-growth-api.onrender.com/health
3. Review error messages carefully
4. Ensure Flutter and dependencies are up to date

---

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Flutter team for the amazing cross-platform toolkit
- Render for free API hosting
- Scikit-learn for machine learning tools

---

**Built with ❤️ for ML Summative**

*Last Updated: November 2025*