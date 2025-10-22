# start.ps1 - simple startup for Tic Tac Toe (Windows PowerShell)
# Usage: Right-click -> Run with PowerShell, or open PowerShell in project and run: .\start.ps1

$venvPath = Join-Path $PSScriptRoot '.venv'
$python = Join-Path $venvPath 'Scripts\python.exe'
$activate = Join-Path $venvPath 'Scripts\Activate.ps1'

# Create venv if missing
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtualenv..."
    python -m venv .venv
}

# Activate venv
Write-Host "Activating virtualenv..."
. $activate

# Install requirements if missing
if (Test-Path "$PSScriptRoot\requirements.txt") {
    Write-Host "Installing requirements..."
    pip install -r "$PSScriptRoot\requirements.txt"
}

# Run tests optionally
$runTests = Read-Host "Run tests before starting? (y/N)"
if ($runTests -match '^(y|Y)') {
    Write-Host "Running tests..."
    python -m pytest -q
}

# Start the app bound to all interfaces so LAN devices can reach it
Write-Host "Starting app on 0.0.0.0:5000..."
Start-Process -NoNewWindow -FilePath $python -ArgumentList 'app.py'

Write-Host "App started. Visit http://<your-lan-ip>:5000 from other devices on your network."

$useNgrok = Read-Host "Do you want to start ngrok (if installed) to share externally? (y/N)"
if ($useNgrok -match '^(y|Y)') {
    if (Get-Command ngrok -ErrorAction SilentlyContinue) {
        Start-Process -NoNewWindow -FilePath ngrok -ArgumentList 'http 5000'
        Write-Host "ngrok started. See ngrok console for the public URL."
    } else {
        Write-Host "ngrok is not installed or not in PATH. Visit https://ngrok.com/ to install."
    }
}
