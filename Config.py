import os
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")
HANDLER = os.environ.get("HANDLER")
OWNER_ID = int(os.environ.get("OWNER_ID"))
SUDO_HANDLER = os.environ.get("SUDO_HANDLER")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2068551800").split()))
