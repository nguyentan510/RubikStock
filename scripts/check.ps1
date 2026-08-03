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

Invoke-Checked -Description "Starting PostgreSQL" -Command { docker compose up -d postgres }

Push-Location $repoRoot
try {
  Invoke-Checked -Description "Validating documentation" -Command { python scripts/validate_docs.py }
} finally {
  Pop-Location
}

Push-Location (Join-Path $repoRoot "apps/api")
try {
  Invoke-Checked -Description "Syncing API dependencies" -Command { uv sync --extra dev }
  Invoke-Checked -Description "Applying database migrations" -Command { uv run alembic upgrade head }
  Invoke-Checked -Description "Running API tests" -Command { uv run pytest }
} finally {
  Pop-Location
}

Push-Location (Join-Path $repoRoot "apps/web")
try {
  Invoke-Checked -Description "Installing web dependencies" -Command { npm ci }
  Invoke-Checked -Description "Linting web app" -Command { npm run lint }
  Invoke-Checked -Description "Type-checking web app" -Command { npm run typecheck }
  Invoke-Checked -Description "Building web app" -Command { npm run build }
} finally {
  Pop-Location
}
