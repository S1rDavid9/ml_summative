/// Model class for the API prediction response
class PredictionResponse {
  final int predictedGrowthDays;
  final String interpretation;
  final String modelUsed;

  PredictionResponse({
    required this.predictedGrowthDays,
    required this.interpretation,
    required this.modelUsed,
  });

  /// Create PredictionResponse from JSON
  factory PredictionResponse.fromJson(Map<String, dynamic> json) {
    return PredictionResponse(
      predictedGrowthDays: (json['predicted_growth_days'] is int) 
          ? json['predicted_growth_days'] as int
          : (json['predicted_growth_days'] as num).toInt(),
      interpretation: json['interpretation'] as String,
      modelUsed: json['model_used'] as String,
    );
  }

  /// Convert PredictionResponse to JSON
  Map<String, dynamic> toJson() {
    return {
      'predicted_growth_days': predictedGrowthDays,
      'interpretation': interpretation,
      'model_used': modelUsed,
    };
  }

  @override
  String toString() {
    return 'PredictionResponse{predictedGrowthDays: $predictedGrowthDays, interpretation: $interpretation, modelUsed: $modelUsed}';
  }
}

/// Model class for the API prediction request
class PredictionRequest {
  final double temperature;
  final double humidity;
  final double tds;
  final double ph;

  PredictionRequest({
    required this.temperature,
    required this.humidity,
    required this.tds,
    required this.ph,
  });

  /// Convert PredictionRequest to JSON
  Map<String, dynamic> toJson() {
    return {
      'temperature': temperature,
      'humidity': humidity,
      'tds': tds,
      'ph': ph,
    };
  }

  @override
  String toString() {
    return 'PredictionRequest{temperature: $temperature, humidity: $humidity, tds: $tds, ph: $ph}';
  }
}
