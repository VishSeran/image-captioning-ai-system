from typing import Optional
from modules.logger import get_logger
import requests
import base64

logger = get_logger("data-extraction")

def get_image_from_url(url):
    
    if not url:
            raise ValueError ("URL is empty or none")
    
    try:
    
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        return response
         
    except requests.RequestException as e:
        logger.error(f"Failed to fetch image: {e}")
        raise

def encode_image(image_path:Optional[str] = None,
                                url:Optional[str] = None):
    
    try:
        
        image = None
    
        if url:
            image = get_image_from_url(url).content
        
        elif image_path:
            with open(image_path, "rb") as f:
                image = f.read()
        
        else:
            raise ValueError("Either image_path or url must be provided.")
        
        # encode raw bytes into bytes object and again decode bytes object into python string
        encoded_image = base64.b64encode(image).decode("utf-8")
        
        return encoded_image
    
    except ValueError as e:
        print(f"Value error: {e}")
        
    except Exception as e:
        print(f"Error in image encoding: {e}")