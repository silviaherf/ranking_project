from src.app import app
import src.api as api 
from dotenv import load_dotenv
load_dotenv()

PORT = os.getenv("PORT")
app.run("0.0.0.0", PORT, debug=True)