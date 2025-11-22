# 🌱 Moss Growth Predictor - Flutter App

A beautiful, modern Flutter mobile application that predicts moss growth days based on environmental conditions using a machine learning API.

## 📱 Features

- **Clean & Modern UI**: Professional moss/nature-themed interface with green color scheme
- **Real-time Input Validation**: Validates all inputs with visual feedback
- **API Integration**: Connects to deployed FastAPI backend on Render
- **Beautiful Animations**: Smooth transitions and fade-in effects
- **Error Handling**: Comprehensive error messages and user feedback
- **Responsive Design**: Works on different screen sizes (phones and tablets)
- **Material Design 3**: Follows latest Flutter and Material Design principles

## 🎨 Screenshots

### Main Screen
- Input form with 4 environmental parameters
- Floating action labels and validation
- Info tooltips for each parameter

### Result Display
- Large, easy-to-read prediction
- Color-coded interpretation
- Model information

### Error States
- Network error handling
- Validation error display
- User-friendly messages

## 🚀 Getting Started

### Prerequisites

- Flutter SDK (3.0 or higher)
- Dart SDK (3.0 or higher)
- Android Studio / VS Code with Flutter extension
- Android device/emulator or iOS device/simulator

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/S1rDavid9/ml_summative.git
   cd ml_summative/flutter_app/moss_growth_app
   ```

2. **Install dependencies:**
   ```bash
   flutter pub get
   ```

3. **Configure API endpoint (if needed):**
   
   Open `lib/constants/app_constants.dart` and update the API URL:
   ```dart
   static const String apiBaseUrl = 'https://moss-growth-api.onrender.com';
   ```

4. **Run the app:**
   
   **For Android:**
   ```bash
   flutter run
   ```
   
   **For iOS:**
   ```bash
   flutter run
   ```
   
   **For specific device:**
   ```bash
   flutter devices  # List all devices
   flutter run -d <device_id>
   ```

## 📦 Project Structure

```
lib/
├── main.dart                           # App entry point
├── constants/
│   └── app_constants.dart             # App-wide constants (colors, URLs, strings)
├── models/
│   └── prediction_response.dart       # Data models for API
├── screens/
│   └── prediction_screen.dart         # Main prediction screen
└── services/
    └── api_service.dart               # API communication layer
```

## 🔧 Configuration

### API Endpoint Configuration

The app connects to a FastAPI backend deployed on Render. To change the API endpoint:

1. Open `lib/constants/app_constants.dart`
2. Modify the `apiBaseUrl` constant:

```dart
class AppConstants {
  static const String apiBaseUrl = 'https://moss-growth-api.onrender.com';
  static const String predictEndpoint = '/predict';
  // ...
}
```

### Input Validation Ranges

All input ranges are defined in `app_constants.dart`:

```dart
// Input Validation Ranges
static const double minTemperature = 18.0;
static const double maxTemperature = 35.0;
static const double minHumidity = 50.0;
static const double maxHumidity = 80.0;
static const double minTds = 400.0;
static const double maxTds = 800.0;
static const double minPh = 6.0;
static const double maxPh = 7.0;
```

### Color Scheme

Customize the app's color scheme in `app_constants.dart`:

```dart
// Color Scheme - Moss/Nature Theme
static const Color primaryGreen = Color(0xFF2D5016);
static const Color secondaryGreen = Color(0xFF1B4332);
static const Color accentGreen = Color(0xFF52B788);
static const Color lightBackground = Color(0xFFF1FAEE);
// ...
```

## 📚 Dependencies

The app uses the following packages:

```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.8
  http: ^1.1.0              # For API calls
  google_fonts: ^6.1.0      # For custom typography
```

To update dependencies:
```bash
flutter pub upgrade
```

## 🎯 Usage

### Making a Prediction

1. **Enter Environmental Parameters:**
   - Temperature (18-35°C)
   - Humidity (50-80%)
   - TDS - Total Dissolved Solids (400-800 ppm)
   - pH Level (6.0-7.0)

2. **Tap Info Icons** (ℹ️) next to each field for parameter descriptions

3. **Press "PREDICT GROWTH"** button

4. **View Results:**
   - Predicted growth days (large number)
   - Interpretation with color-coded feedback
   - Model information

5. **Make Another Prediction:**
   - Tap "CLEAR ALL" to reset form
   - Enter new values

### Interpretation Guide

- **< 15 days** 🟢 Very fast growth - Excellent conditions
- **15-20 days** 🟢 Fast growth - Good conditions
- **20-25 days** 🟠 Moderate growth - Acceptable conditions
- **25+ days** 🔴 Slow growth - Suboptimal conditions

## 🔍 API Details

### Endpoint
```
POST https://moss-growth-api.onrender.com/predict
```

### Request Format
```json
{
  "temperature": 22.5,
  "humidity": 70.0,
  "tds": 600.0,
  "ph": 6.4
}
```

### Response Format
```json
{
  "predicted_growth_days": 16,
  "interpretation": "Fast growth - Good conditions",
  "model_used": "Random Forest"
}
```

## 🐛 Troubleshooting

### Common Issues

**1. "Unable to connect to server"**
- Check your internet connection
- Verify API endpoint URL in `app_constants.dart`
- Ensure the Render API is running (may take 30-60s to wake up on free tier)

**2. "Request timed out"**
- API may be slow on first request (Render free tier cold start)
- Wait and try again

**3. "Validation error"**
- Ensure all values are within valid ranges
- Check for decimal formatting (use . not ,)

**4. Build errors**
- Run `flutter clean`
- Run `flutter pub get`
- Restart your IDE

**5. Hot reload not working**
- Press `R` (capital R) for hot restart
- Or restart the app completely

## 🧪 Testing

### Manual Testing Checklist

- [ ] All input fields accept valid numbers
- [ ] Validation shows errors for out-of-range values
- [ ] Validation shows errors for empty fields
- [ ] Predict button disabled when form invalid
- [ ] Loading indicator shows during API call
- [ ] Success result displays correctly
- [ ] Error messages show for network issues
- [ ] Clear button resets all fields
- [ ] Info dialogs work for each parameter
- [ ] App works on different screen sizes

### Test Cases

**Valid Input:**
```
Temperature: 22.5°C
Humidity: 70%
TDS: 600 ppm
pH: 6.4
Expected: Success with prediction
```

**Invalid Input (Out of Range):**
```
Temperature: 40°C  (too high)
Expected: Validation error
```

**Network Error Test:**
- Turn off internet
- Try to predict
- Expected: Network error message

## 📱 Building for Release

### Android

1. **Build APK:**
   ```bash
   flutter build apk --release
   ```
   APK location: `build/app/outputs/flutter-apk/app-release.apk`

2. **Build App Bundle (for Play Store):**
   ```bash
   flutter build appbundle --release
   ```

### iOS

1. **Build for iOS:**
   ```bash
   flutter build ios --release
   ```

2. **Open in Xcode for signing and publishing**

## 🎨 Customization

### Changing Colors

Edit `lib/constants/app_constants.dart`:
```dart
static const Color primaryGreen = Color(0xFF2D5016);  // Main app color
static const Color accentGreen = Color(0xFF52B788);   // Buttons, highlights
```

### Changing Fonts

Edit `lib/main.dart`:
```dart
textTheme: GoogleFonts.robotoTextTheme(  // Change from poppinsTextTheme
  Theme.of(context).textTheme,
),
```

### Adding New Input Fields

1. Add field to `prediction_screen.dart`
2. Update `PredictionRequest` model
3. Update validation logic
4. Update API service

## 📊 Performance

- **Cold Start**: ~1-2 seconds
- **API Call**: 1-3 seconds (depends on Render API response)
- **Animations**: 60 FPS smooth animations
- **App Size**: ~15-20 MB (release build)

## 🔐 Security

- No sensitive data stored locally
- HTTPS communication with API
- Input validation on both client and server
- No authentication required (public API)

## 🤝 Contributing

This is a school project, but suggestions are welcome!

## 📄 License

This project is part of an ML summative assessment.

## 👤 Author

**GitHub**: [@S1rDavid9](https://github.com/S1rDavid9)  
**Repository**: [ml_summative](https://github.com/S1rDavid9/ml_summative)

## 🙏 Acknowledgments

- FastAPI backend for ML predictions
- Flutter team for the amazing framework
- Material Design for UI guidelines
- Google Fonts for typography

---

**For more information about the ML model and API, see the [API Documentation](../../moss_growth_api/README.md)**

## 📞 Support

If you encounter issues:
1. Check this README
2. Review error messages carefully
3. Verify API is running: https://moss-growth-api.onrender.com/health
4. Check Flutter and Dart versions

---

**Built with ❤️ using Flutter**
