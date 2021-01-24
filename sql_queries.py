import psycopg2
    
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkify user=student password=student")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get cursor to the Database")
    print(e)
conn.set_session(autocommit=True)

# DROP TABLES

songplay_table_drop = cur.execute("DROP TABLE IF EXISTS songplays")
user_table_drop = cur.execute("DROP TABLE IF EXISTS users")
song_table_drop = cur.execute("DROP TABLE IF EXISTS songs")
artist_table_drop = cur.execute("DROP TABLE IF EXISTS  artists")
time_table_drop = cur.execute("DROP TABLE IF EXISTS  time")

# CREATE TABLES

songplay_table_create = cur.execute("CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time varchar, user_id int, level varchar, song_id int, artist_id varchar, session_id int, location varchar, user_agent varchar);")

user_table_create = cur.execute("CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);")

song_table_create = cur.execute("CREATE TABLE IF NOT EXISTS songs (song_id int, title varchar, artist_id int, year int, duration double);")

artist_table_create = cur.execute("CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name varchar, location varchar, latitude double, longitude double);")

time_table_create = cur.execute("CREATE TABLE IF NOT EXISTS time (start_time varchar, hour int, day int, week int, month int, year int, weekday varchar);")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
