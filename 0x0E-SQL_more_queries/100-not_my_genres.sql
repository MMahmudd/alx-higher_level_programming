-- Query: List all genres not linked to the TV show "DEXTER" from the database.
-- Each record should display: Genre Name.
-- Results must be sorted in ascending order by the genre name.
-- The database name will be passed as an argument of the mysql command.

SELECT tv_genres.name AS 'Genre Name'
FROM hbtn_0d_tvshows.tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM hbtn_0d_tvshows.tv_genres
      JOIN hbtn_0d_tvshows.tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
      JOIN hbtn_0d_tvshows.tv_shows ON tv_shows.id = tv_show_genres.show_id
      WHERE tv_shows.title = 'DEXTER')
ORDER BY tv_genres.name;
