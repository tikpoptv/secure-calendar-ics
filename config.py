from enum import Enum
import os

class DataSource(Enum):
    JSON = "json"
    DATABASE = "database"

class Config:
    # Data source configuration
    DATA_SOURCE: DataSource = DataSource(os.getenv("DATA_SOURCE", "json"))
    
    # JSON configuration
    JSON_FILE_PATH: str = "data/events.json"
    
    # Security
    ALLOWED_TOKENS: set = set(os.getenv("ALLOWED_TOKENS", "").split(","))
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 5555
    DEBUG: bool = True 