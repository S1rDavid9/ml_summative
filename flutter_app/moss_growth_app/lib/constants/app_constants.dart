import 'package:flutter/material.dart';

/// Application-wide constants for colors, URLs, and strings
class AppConstants {
  // API Configuration
  static const String apiBaseUrl = 'https://moss-growth-api.onrender.com';
  static const String predictEndpoint = '/predict';
  static const Duration apiTimeout = Duration(seconds: 15);

  // Color Scheme - Moss/Nature Theme
  static const Color primaryGreen = Color(0xFF2D5016); // Deep moss green
  static const Color secondaryGreen = Color(0xFF1B4332); // Dark green/black
  static const Color accentGreen = Color(0xFF52B788); // Light green
  static const Color lightBackground = Color(0xFFF1FAEE); // Light cream
  static const Color cardBackground = Color(0xFFD8F3DC); // Very light green
  static const Color errorRed = Color(0xFFD32F2F);
  static const Color successGreen = Color(0xFF4CAF50);
  static const Color warningOrange = Color(0xFFFF9800);
  static const Color textDark = Color(0xFF212121);
  static const Color textLight = Color(0xFF757575);

  // Input Validation Ranges
  static const double minTemperature = 18.0;
  static const double maxTemperature = 35.0;
  static const double minHumidity = 50.0;
  static const double maxHumidity = 80.0;
  static const double minTds = 400.0;
  static const double maxTds = 800.0;
  static const double minPh = 6.0;
  static const double maxPh = 7.0;

  // Spacing & Sizing
  static const double screenPaddingHorizontal = 24.0;
  static const double screenPaddingVertical = 16.0;
  static const double elementSpacing = 16.0;
  static const double cardPadding = 20.0;
  static const double buttonHeight = 56.0;
  static const double textFieldSpacing = 12.0;
  static const double borderRadius = 12.0;
  static const double cardBorderRadius = 16.0;

  // Typography Sizes
  static const double appTitleSize = 24.0;
  static const double sectionHeaderSize = 18.0;
  static const double inputLabelSize = 14.0;
  static const double resultTextSize = 16.0;
  static const double resultNumberSize = 48.0;
  static const double errorTextSize = 14.0;

  // Strings
  static const String appTitle = 'Moss Growth Predictor';
  static const String inputSectionTitle = 'Environmental Parameters';
  static const String predictButtonText = 'PREDICT GROWTH';
  static const String clearButtonText = 'CLEAR ALL';
  static const String resultTitle = 'Prediction Result';

  // Error Messages
  static const String errorEmptyFields = 'Please fill in all fields';
  static const String errorInvalidRange = 'Value is out of valid range';
  static const String errorNetwork = 'Unable to connect to server. Please check your internet connection.';
  static const String errorApi = 'Prediction failed. Please try again.';
  static const String errorTimeout = 'Request timed out. Please try again.';
  static const String errorUnknown = 'An unexpected error occurred. Please try again.';

  // Input Field Labels
  static const String temperatureLabel = 'Temperature';
  static const String temperatureHint = 'Enter temperature (18-35°C)';
  static const String temperatureSuffix = '°C';
  static const String temperatureInfo = 'Ambient temperature for moss growth';

  static const String humidityLabel = 'Humidity';
  static const String humidityHint = 'Enter humidity (50-80%)';
  static const String humiditySuffix = '%';
  static const String humidityInfo = 'Relative humidity percentage';

  static const String tdsLabel = 'TDS (Total Dissolved Solids)';
  static const String tdsHint = 'Enter TDS value (400-800 ppm)';
  static const String tdsSuffix = 'ppm';
  static const String tdsInfo = 'Mineral content in water/growing medium';

  static const String phLabel = 'pH Level';
  static const String phHint = 'Enter pH level (6.0-7.0)';
  static const String phSuffix = '';
  static const String phInfo = 'Acidity/alkalinity of growing medium';

  // Animation Durations
  static const Duration shortAnimation = Duration(milliseconds: 200);
  static const Duration mediumAnimation = Duration(milliseconds: 300);
  static const Duration longAnimation = Duration(milliseconds: 500);
}
