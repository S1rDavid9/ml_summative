import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import '../models/prediction_response.dart';
import '../constants/app_constants.dart';

/// Service class for handling API communication
class ApiService {
  /// Make a prediction by calling the API endpoint
  static Future<PredictionResponse> makePrediction({
    required double temperature,
    required double humidity,
    required double tds,
    required double ph,
  }) async {
    final url = Uri.parse('${AppConstants.apiBaseUrl}${AppConstants.predictEndpoint}');
    
    // Create request body
    final requestBody = PredictionRequest(
      temperature: temperature,
      humidity: humidity,
      tds: tds,
      ph: ph,
    ).toJson();

    try {
      // Make HTTP POST request with timeout
      final response = await http
          .post(
            url,
            headers: {
              'Content-Type': 'application/json',
            },
            body: json.encode(requestBody),
          )
          .timeout(AppConstants.apiTimeout);

      // Handle different response status codes
      if (response.statusCode == 200) {
        // Success - parse and return response
        final Map<String, dynamic> responseData = json.decode(response.body);
        return PredictionResponse.fromJson(responseData);
      } else if (response.statusCode == 422) {
        // Validation error
        final Map<String, dynamic> errorData = json.decode(response.body);
        throw ApiException(
          'Validation error: ${errorData['detail'] ?? 'Invalid input values'}',
          statusCode: 422,
        );
      } else if (response.statusCode == 500) {
        // Server error
        throw ApiException(
          'Server error occurred. Please try again later.',
          statusCode: 500,
        );
      } else {
        // Other errors
        throw ApiException(
          'Request failed with status: ${response.statusCode}',
          statusCode: response.statusCode,
        );
      }
    } on SocketException {
      // Network error
      throw ApiException(
        AppConstants.errorNetwork,
        statusCode: -1,
      );
    } on http.ClientException {
      // HTTP client error
      throw ApiException(
        AppConstants.errorNetwork,
        statusCode: -1,
      );
    } on FormatException {
      // JSON parsing error
      throw ApiException(
        'Invalid response format from server.',
        statusCode: -2,
      );
    } on TimeoutException {
      // Timeout error
      throw ApiException(
        AppConstants.errorTimeout,
        statusCode: -3,
      );
    } catch (e) {
      // Unknown error
      throw ApiException(
        '${AppConstants.errorUnknown}\nDetails: ${e.toString()}',
        statusCode: -999,
      );
    }
  }

  /// Test connection to the API
  static Future<bool> testConnection() async {
    try {
      final url = Uri.parse('${AppConstants.apiBaseUrl}/health');
      final response = await http.get(url).timeout(const Duration(seconds: 5));
      return response.statusCode == 200;
    } catch (e) {
      return false;
    }
  }
}

/// Custom exception class for API errors
class ApiException implements Exception {
  final String message;
  final int statusCode;

  ApiException(this.message, {required this.statusCode});

  @override
  String toString() => message;
}
