from modules.logger import get_logger
import requests

logger = get_logger("data-extraction")

def get_image_from_url(url):
    
    try:
        if not url:
            raise ValueError ("URL is empty or none")
        
        response = requests.get(url)
        
        if response.status_code == 200:
            return response
        else:
            raise ValueError("Error in response fetching")
            
    except ValueError as e:
        print(f"Value error: {e}")
        
    except Exception as e:
        print(f"Error in get image from url: {e}")