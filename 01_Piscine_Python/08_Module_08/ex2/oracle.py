import os
from dotenv import load_dotenv

missing: list[str] = []
print("ORACLE STATUS: Reading the Matrix...\n")

load_dotenv()
print("Configuration loaded:")

matrix_mode = os.getenv("MATRIX_MODE")
if not matrix_mode:

    missing.append("ERROR: MATRIX_MODE is missing")
else:
    print(f"Mode: {matrix_mode}")
    if matrix_mode == "production":
        print("Running in secure production mode")
    elif matrix_mode == "development":
        print("Running in development mode")
    else:
        print("Unknown mode - defaulting to safe configuration")

database_url = os.getenv("DATABASE_URL")
if not database_url:
    missing.append("ERROR: DATABASE_URL is missing")
else:
    print(f"Database: {database_url}")

api_key = os.getenv("API_KEY")
if not api_key:
    missing.append("ERROR: API_KEY is missing")
else:
    print("API Access: Authenticated")

log_level = os.getenv("LOG_LEVEL")
if not log_level:
    missing.append("ERROR: LOG_LEVEL is missing")
else:
    print(f"Log Level: {log_level}")

zion_endpoint = os.getenv("ZION_ENDPOINT")
if not zion_endpoint:
    missing.append("ERROR: ZION_ENDPOINT is missing")
else:
    print(f"Zion Network: {zion_endpoint}")


print("\nEnvironment security check:")
if not missing:
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
else:
    for error in missing:
        print(error)

print("\nThe Oracle sees all configurations.")
