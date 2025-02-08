@echo off

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    exit /b 1
)

:: Upgrade pip
echo Upgrading pip to the latest version...
python -m pip install --upgrade pip

:: Starting installation
echo Installing required libraries...

:: Install the requirements
pip install -r requirements.txt

:: Check if the installation was successful
IF %ERRORLEVEL% EQU 0 (
    echo Requirements installed successfully!
) ELSE (
    echo Failed to install requirements.
)

:: Completion message
echo Completed installation of required libraries!

echo Press the space bar to close...
pause >nul
