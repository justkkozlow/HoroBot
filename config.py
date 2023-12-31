import os
import dotenv

dotenv.load_dotenv('.env')
TOKEN = os.environ['API_TOKEN']
DB = os.environ['DB_NAME']