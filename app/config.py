import os
from dotenv import load_dotenv

# load values from .env file
load_dotenv()

# This controls if the openapi urls like /docs are accessible
# In the .env in dev set this to "/openapi.json"
# In production set it to an empty string or do not set it at all
OPENAPI_URL = os.getenv("OPENAPI_URL")
