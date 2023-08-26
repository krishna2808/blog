from dotenv import load_dotenv
import os
load_dotenv()

# to check if .env file available in system then we will use production.py file setting variable otherwise staging.py variable use.

if os.environ.get('ENV_FILE_EXISTS', False):
   from .production import *
   print("------------------  env file exists in your system -----------------------")
else:
   from .staging import *
   print("------------------  env file not exists in your system -----------------------")

