import os
import sqlite3
from pathlib import Path


class Database:
    def __init__(self, dir: str | None = None, env_var: str = "FLET_APP_STORAGE_DATA", filename: str = ""):
        # Check if the user has provided a valid path to the database directory
        try:
            storage_dir = Path(dir)
        except TypeError:
            # Check if the user/flet has provided valid env_var
            dir = os.getenv(env_var)
            if dir == None:
                raise ValueError("Must provide a valid directory path or environment variable")
            
            storage_dir = Path(dir)

        # Check if the path points to a directory
        if not storage_dir.is_dir():
            raise ValueError("Path must point to a directory")
                    
        # Fallback for filename
        if not filename:
            filename = "lifevector.db"

        self.database_path = storage_dir / filename
    
    def connect(self) -> sqlite3.Connection:
        """Connect to the LifeVector Database"""

        return sqlite3.connect(self.database_path)

    def init_db(self):
        ...
        