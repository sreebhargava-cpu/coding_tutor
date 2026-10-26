# AI-Powered Adaptive Coding Tutor - Launcher
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Starting AI-Powered Adaptive Coding Tutor" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# Set environment
$env:PYTHONPATH = "$PSScriptRoot\backend"

Write-Host "Starting server on http://localhost:8000..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server." -ForegroundColor Yellow

python "$PSScriptRoot\backend\run.py"
