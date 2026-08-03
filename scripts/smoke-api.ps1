param(
  [int]$Port = 18000
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$apiDir = Resolve-Path (Join-Path $repoRoot "apps/api")
$logsDir = Join-Path $repoRoot "logs"
New-Item -ItemType Directory -Force -Path $logsDir | Out-Null

$pythonPath = Join-Path $apiDir ".venv/Scripts/python.exe"
if (-not (Test-Path -LiteralPath $pythonPath)) {
  throw "API virtual environment is missing. Run npm run setup first."
}

$stdoutPath = Join-Path $logsDir "api-smoke.out.log"
$stderrPath = Join-Path $logsDir "api-smoke.err.log"
$apiProcess = Start-Process -FilePath $pythonPath -ArgumentList @(
  "-m",
  "uvicorn",
  "rubikstock_api.main:app",
  "--host",
  "127.0.0.1",
  "--port",
  $Port
) -WorkingDirectory $apiDir -WindowStyle Hidden -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath -PassThru

try {
  $deadline = (Get-Date).AddSeconds(30)
  $response = $null

  do {
    try {
      $response = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/api/v1/readyz" -TimeoutSec 3
      break
    } catch {
      Start-Sleep -Seconds 1
    }
  } while ((Get-Date) -lt $deadline)

  if ($null -eq $response) {
    $stderr = if (Test-Path -LiteralPath $stderrPath) {
      Get-Content -LiteralPath $stderrPath -Raw
    } else {
      ""
    }
    throw "API readiness smoke timed out. $stderr"
  }

  if ($response.status -ne "ok" -or $response.database -ne "ok") {
    throw "Unexpected readiness response: $($response | ConvertTo-Json -Compress)"
  }

  Write-Output "RUBIKSTOCK_API_SMOKE_OK"
  Write-Output ($response | ConvertTo-Json -Compress)
} finally {
  if (-not $apiProcess.HasExited) {
    Stop-Process -Id $apiProcess.Id
    $apiProcess.WaitForExit()
  }
}
