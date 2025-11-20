@echo off
REM ============================================================================
REM Start the Moss Growth Prediction API
REM ============================================================================

echo.
echo ========================================================================
echo  Starting Moss Growth Prediction API
echo ========================================================================
echo.

REM Activate virtual environment if it exists
if exist "..\venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call ..\venv\Scripts\activate.bat
)

REM Start the FastAPI application
echo Starting server at http://localhost:8000
echo.
echo Access the API documentation at:
echo   - Swagger UI: http://localhost:8000/docs
echo   - ReDoc: http://localhost:8000/redoc
echo.
echo Press Ctrl+C to stop the server
echo ========================================================================
echo.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
