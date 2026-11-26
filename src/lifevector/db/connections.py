import os
import sqlite3
from pathlib import Path


class Database:
    def __init__(
        self,
        dir: str | None = None,
        env_var: str = "FLET_APP_STORAGE_DATA",
        filename: str = "",
    ):
        # Check if the user has provided a valid path to the database directory
        try:
            storage_dir = Path(dir)
        except TypeError:
            # Check if the user/flet has provided valid env_var
            dir = os.getenv(env_var)
            if dir == None:
                raise ValueError(
                    "Must provide a valid directory path or environment variable"
                )

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

    def init_db(self) -> None:
        """Initialize the LifeVector Database"""

        db = self.connect()
        db = db.cursor()

        # Initializ the goal table
        db.execute(
            """
                CREATE TABLE IF NOT EXISTS roles (

                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

                    name TEXT UNIQUE NOT NULL,

                    description TEXT,

                    sort_order TEXT COLLATE BINARY UNIQUE NOT NULL,

                    is_active INTEGER DEFAULT 1

                );
            """
        )

        # Initialize the goals table
        db.execute(
            """
                CREATE TABLE IF NOT EXISTS goals(

                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

                    role_id INTEGER NOT NULL,

                    parent_goal_id INTEGER,

                    title TEXT NOT NULL,

                    description TEXT,

                    priority_quadrant INTEGER DEFAULT 0,

                    status TEXT NOT NULL DEFAULT 'not_completed',

                    created_at NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,

                    completed_at NUMERIC,

                    FOREIGN KEY (role_id) REFERENCES roles(id),

                    FOREIGN KEY (parent_goal_id) REFERENCES goals(id) ON DELETE CASCADE

                );                
            """
        )

        # Initialize the goal schedules table
        db.execute(
            """
                CREATE TABLE IF NOT EXISTS scheduled_activities (

                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

                    goal_id INTEGER NOT NULL,

                    estimated_duration INTEGER,

                    start_date NUMERIC,

                    start_time NUMERIC,

                    FOREIGN KEY (goal_id) REFERENCES goals(id)

                );
            """
        )

        # Closing the connection
        db.close()