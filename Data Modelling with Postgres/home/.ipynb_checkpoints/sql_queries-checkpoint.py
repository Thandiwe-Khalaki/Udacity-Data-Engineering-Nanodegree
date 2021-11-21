# DROP TABLES
"""Query to drop  tables if they exist."""

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES
"""Query to create tables.
Fact table: songplay
Dimension tables: users, song, artists, time
"""

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
    (songplay_id SERIAL NOT NULL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    level TEXT NOT NULL,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT,
    location VARCHAR,
    user_agent VARCHAR);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
    (user_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    gender VARCHAR,
    level VARCHAR);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
    (song_id VARCHAR PRIMARY KEY,
    title VARCHAR NOT NULL,
    artist_id VARCHAR NOT NULL,
    year INT,
    duration FLOAT NOT NULL)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
    (artist_id varchar NOT NULL PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR,
    latitude FLOAT,
    longitude FLOAT);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
    (start_time TIMESTAMP NOT NULL PRIMARY KEY,
    hour INT NOT NULL,
    day INT NOT NULL,
    week INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    weekday INT NOT NULL);
""")

# INSERT RECORDS
"""Query to insert values into tables."""

songplay_table_insert = ("""INSERT INTO songplays 
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT (songplay_id) DO NOTHING ;
""")

user_table_insert = ("""INSERT INTO users 
    (user_id, first_name, last_name, gender, level) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs 
    (song_id, title, artist_id, year, duration)  
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists 
    (artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""INSERT INTO time 
    (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS
"""Query which finds song_id and artist_id for songplays table."""

song_select = ("""SELECT songs.song_id, artists.artist_id 
     FROM (songs JOIN artists ON songs.artist_id=artists.artist_id)
     WHERE title=(%s) AND name=(%s) AND duration=(%s);
 """)

# QUERY LISTS
"""Lists which are passed to create_tables.py when tables are dropped or created."""

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]