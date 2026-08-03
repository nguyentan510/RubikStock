$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$logsDir = Join-Path $repoRoot "logs"
New-Item -ItemType Directory -Force -Path $logsDir | Out-Null

docker compose up -d postgres
if ($LASTEXITCODE -ne 0) {
  throw "Starting PostgreSQL failed with exit code $LASTEXITCODE"
}

$apiDir = Join-Path $repoRoot "apps/api"
$webDir = Join-Path $repoRoot "apps/web"

$apiLog = Join-Path $logsDir "api.log"
$webLog = Join-Path $logsDir "web.log"

$uvPath = (Get-Command uv).Source
$npmPath = (Get-Command npm).Source

Start-Process -FilePath $uvPath -ArgumentList @(
  "run",
  "uvicorn",
  "rubikstock_api.main:app",
  "--reload",
  "--host",
  "0.0.0.0",
  "--port",
  "8000"
) -WorkingDirectory $apiDir -WindowStyle Hidden -RedirectStandardOutput $apiLog -RedirectStandardError $apiLog | Out-Null

Start-Process -FilePath $npmPath -ArgumentList @("run", "dev") -WorkingDirectory $webDir -WindowStyle Hidden -RedirectStandardOutput $webLog -RedirectStandardError $webLog | Out-Null

Write-Host "RubikStock dev services started."
Write-Host "API  -> http://localhost:8000"
Write-Host "Web  -> http://localhost:3000"
Write-Host "Logs -> $logsDir"
