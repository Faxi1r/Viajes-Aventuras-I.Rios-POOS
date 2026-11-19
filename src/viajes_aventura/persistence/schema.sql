-- Physical model v1 (SQLite) derived from docs/uml_classes_v1.drawio
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL DEFAULT 'client'
                  CHECK (role IN ('client', 'admin'))
);

CREATE TABLE IF NOT EXISTS destinations (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    description TEXT,
    location    TEXT NOT NULL,
    status      TEXT NOT NULL DEFAULT 'active'
                CHECK (status IN ('active', 'inactive'))
);

CREATE TABLE IF NOT EXISTS tour_packages (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    description TEXT,
    start_date  TEXT NOT NULL,  -- ISO 8601 (YYYY-MM-DD)
    end_date    TEXT NOT NULL,
    available   INTEGER NOT NULL DEFAULT 1 CHECK (available IN (0, 1)),
    CHECK (end_date >= start_date)
);

-- Association class PackageDestination: a package contains 2..* destinations.
-- The minimum of 2 is enforced in the business layer, not here.
CREATE TABLE IF NOT EXISTS package_destinations (
    package_id       INTEGER NOT NULL,
    destination_id   INTEGER NOT NULL,
    associated_cost  NUMERIC NOT NULL CHECK (associated_cost >= 0),
    PRIMARY KEY (package_id, destination_id),
    FOREIGN KEY (package_id)     REFERENCES tour_packages (id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations (id)
);

CREATE TABLE IF NOT EXISTS reservations (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id       INTEGER NOT NULL,
    package_id    INTEGER NOT NULL,
    reserved_at   TEXT NOT NULL,
    people_count  INTEGER NOT NULL CHECK (people_count > 0),
    total_price   NUMERIC NOT NULL CHECK (total_price >= 0),
    status        TEXT NOT NULL DEFAULT 'pending'
                  CHECK (status IN ('pending', 'confirmed', 'cancelled')),
    FOREIGN KEY (user_id)    REFERENCES users (id),
    FOREIGN KEY (package_id) REFERENCES tour_packages (id)
);
