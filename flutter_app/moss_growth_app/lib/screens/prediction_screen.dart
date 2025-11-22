import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../constants/app_constants.dart';
import '../models/prediction_response.dart';
import '../services/api_service.dart';

class PredictionScreen extends StatefulWidget {
  const PredictionScreen({super.key});

  @override
  State<PredictionScreen> createState() => _PredictionScreenState();
}

class _PredictionScreenState extends State<PredictionScreen> with SingleTickerProviderStateMixin {
  // Form key for validation
  final _formKey = GlobalKey<FormState>();

  // Text controllers for input fields
  final _temperatureController = TextEditingController();
  final _humidityController = TextEditingController();
  final _tdsController = TextEditingController();
  final _phController = TextEditingController();

  // State management
  bool _isLoading = false;
  PredictionResponse? _predictionResult;
  String? _errorMessage;
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;

  @override
  void initState() {
    super.initState();
    // Initialize animation controller
    _animationController = AnimationController(
      vsync: this,
      duration: AppConstants.mediumAnimation,
    );
    _fadeAnimation = CurvedAnimation(
      parent: _animationController,
      curve: Curves.easeIn,
    );
  }

  @override
  void dispose() {
    _temperatureController.dispose();
    _humidityController.dispose();
    _tdsController.dispose();
    _phController.dispose();
    _animationController.dispose();
    super.dispose();
  }

  /// Validate input value against range
  String? _validateInput(
    String? value,
    double min,
    double max,
    String fieldName,
  ) {
    if (value == null || value.isEmpty) {
      return 'Please enter $fieldName';
    }

    final numValue = double.tryParse(value);
    if (numValue == null) {
      return 'Please enter a valid number';
    }

    if (numValue < min || numValue > max) {
      return '$fieldName must be between $min and $max';
    }

    return null;
  }

  /// Handle prediction button press
  Future<void> _handlePrediction() async {
    // Validate form
    if (!_formKey.currentState!.validate()) {
      return;
    }

    // Hide keyboard
    FocusScope.of(context).unfocus();

    // Clear previous results
    setState(() {
      _isLoading = true;
      _errorMessage = null;
      _predictionResult = null;
    });

    try {
      // Parse input values
      final temperature = double.parse(_temperatureController.text);
      final humidity = double.parse(_humidityController.text);
      final tds = double.parse(_tdsController.text);
      final ph = double.parse(_phController.text);

      // Make API call
      final result = await ApiService.makePrediction(
        temperature: temperature,
        humidity: humidity,
        tds: tds,
        ph: ph,
      );

      // Update state with result
      setState(() {
        _predictionResult = result;
        _isLoading = false;
      });

      // Animate result card
      _animationController.forward(from: 0.0);

      // Show success feedback
      HapticFeedback.mediumImpact();
    } on ApiException catch (e) {
      setState(() {
        _errorMessage = e.message;
        _isLoading = false;
      });

      // Show error feedback
      HapticFeedback.heavyImpact();
    } catch (e) {
      setState(() {
        _errorMessage = AppConstants.errorUnknown;
        _isLoading = false;
      });

      // Show error feedback
      HapticFeedback.heavyImpact();
    }
  }

  /// Clear all input fields
  void _clearAll() {
    _temperatureController.clear();
    _humidityController.clear();
    _tdsController.clear();
    _phController.clear();

    setState(() {
      _predictionResult = null;
      _errorMessage = null;
    });

    HapticFeedback.lightImpact();
  }

  /// Build input text field widget
  Widget _buildInputField({
    required TextEditingController controller,
    required String label,
    required String hint,
    required IconData icon,
    required String suffix,
    required String infoText,
    required double min,
    required double max,
  }) {
    return Padding(
      padding: const EdgeInsets.only(bottom: AppConstants.textFieldSpacing),
      child: TextFormField(
        controller: controller,
        keyboardType: const TextInputType.numberWithOptions(decimal: true),
        decoration: InputDecoration(
          labelText: label,
          hintText: hint,
          suffixText: suffix,
          prefixIcon: Icon(icon, color: AppConstants.accentGreen),
          suffixIcon: IconButton(
            icon: const Icon(Icons.info_outline, size: 20),
            onPressed: () {
              _showInfoDialog(label, infoText, min, max);
            },
          ),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(AppConstants.borderRadius),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(AppConstants.borderRadius),
            borderSide: BorderSide(color: Colors.grey.shade300),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(AppConstants.borderRadius),
            borderSide: const BorderSide(color: AppConstants.accentGreen, width: 2),
          ),
          errorBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(AppConstants.borderRadius),
            borderSide: const BorderSide(color: AppConstants.errorRed),
          ),
          filled: true,
          fillColor: Colors.white,
        ),
        validator: (value) => _validateInput(value, min, max, label),
        inputFormatters: [
          FilteringTextInputFormatter.allow(RegExp(r'^\d*\.?\d{0,2}')),
        ],
      ),
    );
  }

  /// Show info dialog for parameter
  void _showInfoDialog(String title, String description, double min, double max) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(title),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(description),
            const SizedBox(height: 12),
            Text(
              'Valid Range: $min - $max',
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                color: AppConstants.accentGreen,
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('OK'),
          ),
        ],
      ),
    );
  }

  /// Build result card widget
  Widget _buildResultCard() {
    if (_predictionResult == null) {
      return const SizedBox.shrink();
    }

    return FadeTransition(
      opacity: _fadeAnimation,
      child: Card(
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppConstants.cardBorderRadius),
        ),
        color: AppConstants.cardBackground,
        child: Padding(
          padding: const EdgeInsets.all(AppConstants.cardPadding),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Title
              Row(
                children: [
                  Icon(
                    Icons.eco,
                    color: AppConstants.primaryGreen,
                    size: 28,
                  ),
                  const SizedBox(width: 12),
                  const Text(
                    AppConstants.resultTitle,
                    style: TextStyle(
                      fontSize: AppConstants.sectionHeaderSize,
                      fontWeight: FontWeight.bold,
                      color: AppConstants.primaryGreen,
                    ),
                  ),
                ],
              ),
              const Divider(height: 24),

              // Predicted days - Large number
              Center(
                child: Column(
                  children: [
                    Text(
                      '${_predictionResult!.predictedGrowthDays}',
                      style: const TextStyle(
                        fontSize: AppConstants.resultNumberSize,
                        fontWeight: FontWeight.bold,
                        color: AppConstants.primaryGreen,
                      ),
                    ),
                    const Text(
                      'Days',
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w500,
                        color: AppConstants.textLight,
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 16),

              // Interpretation
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: _getInterpretationColor().withValues(alpha: 0.1),
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(
                    color: _getInterpretationColor(),
                    width: 2,
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      _getInterpretationIcon(),
                      color: _getInterpretationColor(),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(
                        _predictionResult!.interpretation,
                        style: TextStyle(
                          fontSize: AppConstants.resultTextSize,
                          fontWeight: FontWeight.w500,
                          color: _getInterpretationColor(),
                        ),
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 16),

              // Model used
              Row(
                children: [
                  const Icon(
                    Icons.psychology,
                    size: 20,
                    color: AppConstants.textLight,
                  ),
                  const SizedBox(width: 8),
                  Text(
                    'Model: ${_predictionResult!.modelUsed}',
                    style: const TextStyle(
                      fontSize: 14,
                      color: AppConstants.textLight,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  /// Get color based on interpretation
  Color _getInterpretationColor() {
    final days = _predictionResult!.predictedGrowthDays;
    if (days < 15) {
      return AppConstants.successGreen;
    } else if (days < 20) {
      return const Color(0xFF66BB6A);
    } else if (days < 25) {
      return AppConstants.warningOrange;
    } else {
      return AppConstants.errorRed;
    }
  }

  /// Get icon based on interpretation
  IconData _getInterpretationIcon() {
    final days = _predictionResult!.predictedGrowthDays;
    if (days < 15) {
      return Icons.sentiment_very_satisfied;
    } else if (days < 20) {
      return Icons.sentiment_satisfied;
    } else if (days < 25) {
      return Icons.sentiment_neutral;
    } else {
      return Icons.sentiment_dissatisfied;
    }
  }

  /// Build error card widget
  Widget _buildErrorCard() {
    if (_errorMessage == null) {
      return const SizedBox.shrink();
    }

    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppConstants.cardBorderRadius),
      ),
      color: AppConstants.errorRed.withValues(alpha: 0.1),
      child: Padding(
        padding: const EdgeInsets.all(AppConstants.cardPadding),
        child: Row(
          children: [
            const Icon(
              Icons.error_outline,
              color: AppConstants.errorRed,
              size: 32,
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                _errorMessage!,
                style: const TextStyle(
                  fontSize: AppConstants.errorTextSize,
                  color: AppConstants.errorRed,
                  fontWeight: FontWeight.w500,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppConstants.lightBackground,
      appBar: AppBar(
        title: Row(
          children: [
            Icon(Icons.eco, color: Colors.white),
            const SizedBox(width: 8),
            const Text(
              AppConstants.appTitle,
              style: TextStyle(
                fontSize: AppConstants.appTitleSize,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ],
        ),
        backgroundColor: AppConstants.primaryGreen,
        elevation: 0,
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(
            horizontal: AppConstants.screenPaddingHorizontal,
            vertical: AppConstants.screenPaddingVertical,
          ),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Input Section Title
                const Text(
                  AppConstants.inputSectionTitle,
                  style: TextStyle(
                    fontSize: AppConstants.sectionHeaderSize,
                    fontWeight: FontWeight.bold,
                    color: AppConstants.primaryGreen,
                  ),
                ),
                const SizedBox(height: AppConstants.elementSpacing),

                // Temperature Input
                _buildInputField(
                  controller: _temperatureController,
                  label: AppConstants.temperatureLabel,
                  hint: AppConstants.temperatureHint,
                  icon: Icons.thermostat,
                  suffix: AppConstants.temperatureSuffix,
                  infoText: AppConstants.temperatureInfo,
                  min: AppConstants.minTemperature,
                  max: AppConstants.maxTemperature,
                ),

                // Humidity Input
                _buildInputField(
                  controller: _humidityController,
                  label: AppConstants.humidityLabel,
                  hint: AppConstants.humidityHint,
                  icon: Icons.water_drop,
                  suffix: AppConstants.humiditySuffix,
                  infoText: AppConstants.humidityInfo,
                  min: AppConstants.minHumidity,
                  max: AppConstants.maxHumidity,
                ),

                // TDS Input
                _buildInputField(
                  controller: _tdsController,
                  label: AppConstants.tdsLabel,
                  hint: AppConstants.tdsHint,
                  icon: Icons.science,
                  suffix: AppConstants.tdsSuffix,
                  infoText: AppConstants.tdsInfo,
                  min: AppConstants.minTds,
                  max: AppConstants.maxTds,
                ),

                // pH Input
                _buildInputField(
                  controller: _phController,
                  label: AppConstants.phLabel,
                  hint: AppConstants.phHint,
                  icon: Icons.analytics,
                  suffix: AppConstants.phSuffix,
                  infoText: AppConstants.phInfo,
                  min: AppConstants.minPh,
                  max: AppConstants.maxPh,
                ),

                const SizedBox(height: AppConstants.elementSpacing),

                // Predict Button
                SizedBox(
                  height: AppConstants.buttonHeight,
                  child: ElevatedButton(
                    onPressed: _isLoading ? null : _handlePrediction,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppConstants.primaryGreen,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(AppConstants.borderRadius),
                      ),
                      elevation: 4,
                    ),
                    child: _isLoading
                        ? const SizedBox(
                            height: 24,
                            width: 24,
                            child: CircularProgressIndicator(
                              color: Colors.white,
                              strokeWidth: 3,
                            ),
                          )
                        : const Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(Icons.biotech),
                              SizedBox(width: 8),
                              Text(
                                AppConstants.predictButtonText,
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ],
                          ),
                  ),
                ),

                const SizedBox(height: 12),

                // Clear Button
                TextButton.icon(
                  onPressed: _isLoading ? null : _clearAll,
                  icon: const Icon(Icons.clear_all),
                  label: const Text(AppConstants.clearButtonText),
                  style: TextButton.styleFrom(
                    foregroundColor: AppConstants.textLight,
                  ),
                ),

                const SizedBox(height: AppConstants.elementSpacing),

                // Error Card
                _buildErrorCard(),

                // Result Card
                _buildResultCard(),

                const SizedBox(height: AppConstants.elementSpacing),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
