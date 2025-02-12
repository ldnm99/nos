-- create_database.sql

-- Create the 'cars' table
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symboling INTEGER, 
    normalized_losses REAL,
    make              TEXT,
    fuel_type         TEXT,
    aspiration        TEXT,
    num_of_doors      INTEGER,
    body_style        TEXT,
    drive_wheels      TEXT,
    engine_location   TEXT,
    wheel_base        REAL,
    length            REAL,
    width             REAL,
    height            REAL,
    curb_weight       REAL,
    engine_type       TEXT,
    num_of_cylinders  INTEGER,
    engine_size       REAL,
    fuel_system       TEXT,
    bore              REAL,
    stroke            REAL,
    compression_ratio REAL,
    horsepower        REAL,
    peak_rpm          REAL,
    city_mpg          REAL,
    highway_mpg       REAL,
    price             REAL
);

-- Example data insertions (you can add more rows as needed)
INSERT INTO cars (symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, price)
VALUES 
(3, 165, 'alfa-romero', 'gas', 'std', 'four', 'convertible','rwd', 'front', 88.6, 168.8, 64.1, 48.8, 2548, 'dohc', 'four', 130, 'mpfi', 3.47, 2.68, 9.0, 111, 5000, 21, 27, 13495),
(1, 164, 'audi',        'gas', 'std', 'two', 'sedan',       'fwd', 'front', 94.5, 168.5, 64.1, 48.6, 2335, 'ohc',  'four', 152, 'mpfi', 3.31, 2.56, 9.0, 154, 5200, 19, 25, 16500),
(2, 130, 'bmw',         'gas', 'std', 'four', 'sedan',      'rwd', 'front', 99.0, 169.7, 65.7, 52.0, 2824, 'ohcv', 'six',  109, 'mpfi', 3.19, 3.40, 8.0, 115, 4800, 18, 22, 13950),
(0, 122, 'chevrolet',   'gas', 'std', 'four', 'hatchback',  'fwd', 'front', 96.1, 176.6, 66.5, 53.1, 2655, 'ohc',  'four', 95,  '1bbl', 3.19, 2.87, 8.5, 95,  5100, 21, 27, 14250),
(1, 121, 'dodge',       'gas', 'std', 'four', 'wagon',      'rwd', 'front', 88.9, 171.2, 65.4, 52.0, 2490, 'dohc', 'four', 140, 'mpfi', 3.19, 2.87, 9.0, 130, 5300, 20, 27, 15500);