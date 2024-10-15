
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env_template')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class conf():
    def __init__(self):
        self.mexc_host = os.getenv('MEXC_HOST')
        self.api_key = os.getenv('API_KEY')
        self.secret_key = os.getenv('SECRET_KEY')
