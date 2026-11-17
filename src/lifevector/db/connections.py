import os
import sqlite3
from pathlib import Path

class Database:
    def __init__(self, env_var: str = "FLET_APP_STORAGE_DATA"):
        self.storage_dir = Path(os.getenv(env_var))
        self.database_path = self.storage_dir / "lifevector.db"
    
    def connect(self) -> sqlite3.Connection:
        """Connect to the LifeVector Database"""

        return sqlite3.connect(self.database_path)

    def init_db(self):
        """Initialize the LifeVector Database"""
        
        pass

        