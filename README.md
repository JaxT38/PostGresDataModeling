# PostGresDataModeling

PostGres Data Modeling with Normalization and Database Creation

The purpose of the database is to analyze the JSON metadata on songs and user activity on their new music streaming app. The database will allow the analytics team to see the songs that users are listening to.

The primary key is the songplay_id from the songplays table. The songplays table is connected to the users table through the user_id, the time table through start_time, the songs table through song_id, and the artists table through the artist_id. Below is the architecture for the data tables:

![ER Diagram](https://github.com/JaxT38/PostGresDataModeling/blob/main/Images/ERDiag.PNG)

To run the project, implement create_tables.py. To test the etl load, run the etl.ipynb.


