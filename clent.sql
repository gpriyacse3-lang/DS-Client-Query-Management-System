CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            hashed_password TEXT NOT NULL,
            role TEXT CHECK(role IN ('Client','Support')) NOT NULL
        )

CREATE TABLE IF NOT EXISTS queries (
            query_id SERIAL PRIMARY KEY,
            mail_id TEXT NOT NULL,
            mobile_number TEXT NOT NULL,
            query_heading TEXT NOT NULL,
            query_description TEXT NOT NULL,
            status TEXT CHECK(status IN ('Open','Closed')) NOT NULL DEFAULT 'Open',
            query_created_time TIMESTAMP NOT NULL,
            query_closed_time TIMESTAMP,
            closed_by TEXT
        )
		CREATE TABLE IF NOT EXISTS users_backup (
            username TEXT,
            hashed_password TEXT,
            role TEXT
        )
		SELECT * FROM USERS 
		SELECT * FROM QUERIES