$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$apiUrl = "http://127.0.0.1:8000/api/v1/readyz"
$webUrl = "http://127.0.0.1:3000"

Push-Location $repoRoot
try {
  docker compose up -d --build
  if ($LASTEXITCODE -ne 0) {
    throw "docker compose up failed with exit code $LASTEXITCODE"
  }

  $deadline = (Get-Date).AddSeconds(90)
  $apiReady = $false
  $webReady = $false

  while ((Get-Date) -lt $deadline -and -not ($apiReady -and $webReady)) {
    try {
      $api = Invoke-RestMethod -Uri $apiUrl -TimeoutSec 3
      $apiReady = $api.database -eq "ok"
    } catch {
      $apiReady = $false
    }

    try {
      $web = Invoke-WebRequest -Uri $webUrl -TimeoutSec 3 -UseBasicParsing
      $webReady = $web.StatusCode -eq 200
    } catch {
      $webReady = $false
    }

    if (-not ($apiReady -and $webReady)) {
      Start-Sleep -Seconds 2
    }
  }

  if (-not $apiReady) {
    throw "API readiness did not become healthy: $apiUrl"
  }
  if (-not $webReady) {
    throw "Web did not become healthy: $webUrl"
  }

  docker compose ps
  if ($LASTEXITCODE -ne 0) {
    throw "docker compose ps failed with exit code $LASTEXITCODE"
  }

  Write-Output "RUBIKSTOCK_STACK_SMOKE_OK"
} finally {
  Pop-Location
}
