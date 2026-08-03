const fallbackAppName = "RubikStock"
const fallbackApiBaseUrl = "http://localhost:8000"

export const publicEnv = {
  appName: process.env.NEXT_PUBLIC_APP_NAME?.trim() || fallbackAppName,
  apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL?.trim() || fallbackApiBaseUrl,
}

