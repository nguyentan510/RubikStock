$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

function Invoke-Checked {
  param(
    [Parameter(Mandatory = $true)][scriptblock]$Command,
    [Parameter(Mandatory = $true)][string]$Description
  )

  & $Command
  if ($LASTEXITCODE -ne 0) {
    throw "$Description failed with exit code $LASTEXITCODE"
  }
}

if (-not (Test-Path (Join-Path $repoRoot ".env"))) {
  Copy-Item -LiteralPath (Join-Path $repoRoot ".env.example") -Destination (Join-Path $repoRoot ".env")
}

function Set-EnvLine {
  param(
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$Name,
    [Parameter(Mandatory = $true)][string]$Value
  )

  $content = Get-Content -LiteralPath $Path -Raw
  if ($content -match "(?m)^$Name=") {
    $content = [regex]::Replace($content, "(?m)^$Name=.*$", "$Name=$Value")
  } else {
    $content = $content.TrimEnd() + "`r`n$Name=$Value`r`n"
  }

  Set-Content -LiteralPath $Path -Value $content
}

$envPath = Join-Path $repoRoot ".env"
Set-EnvLine -Path $envPath -Name "DATABASE_URL" -Value "postgresql+psycopg://rubikstock:rubikstock@localhost:5433/rubikstock"

Invoke-Checked -Description "Starting PostgreSQL" -Command { docker compose up -d postgres }

Push-Location (Join-Path $repoRoot "apps/api")
try {
  Invoke-Checked -Description "Syncing API dependencies" -Command { uv sync --extra dev }
  Invoke-Checked -Description "Applying database migrations" -Command { uv run alembic upgrade head }
} finally {
  Pop-Location
}

Push-Location (Join-Path $repoRoot "apps/web")
try {
  Invoke-Checked -Description "Installing web dependencies" -Command { npm install }
} finally {
  Pop-Location
}
