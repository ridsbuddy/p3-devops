CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

INSERT INTO books (title)
VALUES
    ('Clean Code'),
    ('The Phoenix Project');
