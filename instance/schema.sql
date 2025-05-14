-- enforce foreign keys
PRAGMA foreign_keys = ON;

CREATE TABLE user (
  id   INTEGER PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);

-- 1. Styles lookup
CREATE TABLE style (
  id   INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

INSERT INTO style(name) VALUES
  ('Modern'),
  ('Classic'),
  ('Professional');

-- 2. CVs (skills as a TEXT column)
CREATE TABLE cv (
  id                   INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_id             INTEGER NOT NULL,     -- FK into your user table
  full_name            TEXT    NOT NULL,
  job_title            TEXT    NOT NULL,
  email                TEXT    NOT NULL,
  phone_number         TEXT    NOT NULL,
  address              TEXT,
  professional_summary TEXT,
  skills               TEXT,                 -- comma-separated list
  style_id             INTEGER NOT NULL,     -- FK into style

  FOREIGN KEY(owner_id) REFERENCES user(id) ON DELETE CASCADE,
  FOREIGN KEY(style_id) REFERENCES style(id)
);

-- 3. Work Experience (one-to-many CV → work entries)
CREATE TABLE work_experience (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  cv_id         INTEGER NOT NULL,
  job_title     TEXT    NOT NULL,
  company       TEXT    NOT NULL,
  start_date    TEXT    NOT NULL,  -- ISO YYYY-MM-DD
  end_date      TEXT,               -- NULL if current
  is_current    INTEGER NOT NULL    -- 0 = no, 1 = yes
    CHECK(is_current IN (0,1)),
  description   TEXT,

  FOREIGN KEY(cv_id) REFERENCES cv(id) ON DELETE CASCADE
);

-- 4. Education (one-to-many CV → education entries)
CREATE TABLE education (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  cv_id              INTEGER NOT NULL,
  degree_certificate TEXT    NOT NULL,
  institution        TEXT    NOT NULL,
  start_date         TEXT    NOT NULL,  -- ISO YYYY-MM-DD
  end_date           TEXT,               -- NULL if current
  is_current         INTEGER NOT NULL    -- 0 = no, 1 = yes
    CHECK(is_current IN (0,1)),
  description        TEXT,

  FOREIGN KEY(cv_id) REFERENCES cv(id) ON DELETE CASCADE
);
