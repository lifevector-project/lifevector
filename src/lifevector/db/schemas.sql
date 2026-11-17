--- Schemas for tables in LifeVector database:


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

CREATE TABLE IF NOT EXISTS scheduled_activities (

    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

    goal_id INTEGER NOT NULL,

    estimated_duration INTEGER,

    start_date NUMERIC,

    start_time NUMERIC,

    FOREIGN KEY (goal_id) REFERENCES goals(id)

);


CREATE TABLE IF NOT EXISTS roles (

    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

    name TEXT NOT NULL,

    description TEXT,

    sort_order INTEGER NOT NULL,

    is_active INTEGER DEFAULT 1

);

