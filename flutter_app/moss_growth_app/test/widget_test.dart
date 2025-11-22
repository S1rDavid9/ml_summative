// Basic widget test for Moss Growth Predictor App
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter_test/flutter_test.dart';

import 'package:moss_growth_app/main.dart';

void main() {
  testWidgets('App loads prediction screen', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MossGrowthApp());

    // Verify that the prediction screen loads
    expect(find.text('Moss Growth Predictor'), findsOneWidget);
    expect(find.text('PREDICT GROWTH'), findsOneWidget);
    
    // Verify input fields exist
    expect(find.text('Temperature (°C)'), findsOneWidget);
    expect(find.text('Humidity (%)'), findsOneWidget);
    expect(find.text('TDS (ppm)'), findsOneWidget);
    expect(find.text('pH Level'), findsOneWidget);
  });
}
