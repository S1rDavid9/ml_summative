"""
Simple Python script to test the Moss Growth Prediction API
Run this file to test all endpoints
"""

import requests
import json

# Base URL - change this when deployed to Render
BASE_URL = "http://localhost:8000"

def test_root():
    """Test the root endpoint"""
    print("\n" + "="*70)
    print("Testing Root Endpoint")
    print("="*70)
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.status_code == 200

def test_health():
    """Test the health check endpoint"""
    print("\n" + "="*70)
    print("Testing Health Check")
    print("="*70)
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.status_code == 200

def test_prediction(temperature, humidity, tds, ph):
    """Make a prediction request"""
    print("\n" + "="*70)
    print(f"Testing Prediction")
    print("="*70)
    
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "tds": tds,
        "ph": ph
    }
    
    print(f"Input: {json.dumps(payload, indent=2)}")
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"\nStatus Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ Prediction Results:")
        print(f"  🌱 Predicted Growth Days: {result['predicted_growth_days']} days")
        print(f"  📊 Interpretation: {result['interpretation']}")
        print(f"  🤖 Model Used: {result['model_used']}")
        print(f"  📈 Model Accuracy (R²): {result['model_accuracy_r2']}")
        return True
    else:
        print(f"\n❌ Error: {response.json()}")
        return False

def test_invalid_input():
    """Test validation with invalid input"""
    print("\n" + "="*70)
    print("Testing Invalid Input (should fail)")
    print("="*70)
    
    # Temperature too low
    payload = {
        "temperature": 15.0,  # Below minimum (18.0)
        "humidity": 70.0,
        "tds": 600.0,
        "ph": 6.4
    }
    
    print(f"Input (invalid temperature): {json.dumps(payload, indent=2)}")
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"\nStatus Code: {response.status_code}")
    if response.status_code == 422:
        print("✅ Validation working correctly - rejected invalid input")
        return True
    else:
        print("❌ Validation failed to catch invalid input")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*70)
    print(" MOSS GROWTH PREDICTION API - TEST SUITE ".center(70, "="))
    print("="*70)
    print(f"\nTesting API at: {BASE_URL}")
    
    results = []
    
    try:
        # Test 1: Root endpoint
        results.append(("Root Endpoint", test_root()))
        
        # Test 2: Health check
        results.append(("Health Check", test_health()))
        
        # Test 3: Valid prediction
        results.append(("Valid Prediction", test_prediction(22.5, 70.0, 600.0, 6.4)))
        
        # Test 4: Another prediction with different values
        results.append(("Hot & Humid", test_prediction(30.0, 75.0, 550.0, 6.5)))
        
        # Test 5: Invalid input
        results.append(("Invalid Input", test_invalid_input()))
        
        # Summary
        print("\n" + "="*70)
        print(" TEST RESULTS SUMMARY ".center(70, "="))
        print("="*70)
        
        for test_name, passed in results:
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"{test_name}: {status}")
        
        total = len(results)
        passed = sum(1 for _, p in results if p)
        
        print("\n" + "="*70)
        print(f"Total: {passed}/{total} tests passed")
        print("="*70)
        
        if passed == total:
            print("\n🎉 All tests passed! Your API is working perfectly!")
        else:
            print(f"\n⚠️  {total - passed} test(s) failed. Check the output above.")
        
    except requests.exceptions.ConnectionError:
        print("\n" + "="*70)
        print("❌ ERROR: Could not connect to the API")
        print("="*70)
        print(f"\nMake sure the server is running at {BASE_URL}")
        print("\nTo start the server, run:")
        print("  python main.py")
        print("or")
        print("  uvicorn main:app --reload")

if __name__ == "__main__":
    main()
