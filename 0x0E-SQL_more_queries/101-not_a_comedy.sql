-- Query: List all shows without the genre "Comedy" from the hbtn_0d_tvshows database.
-- Each record should display: TV Show Title.
-- Results must be sorted in ascending order by the show title.
-- The database name "hbtn_0d_tvshows" will be passed as an argument of the mysql command.

SELECT tv_shows.title AS 'TV Show Title'
FROM hbtn_0d_tvshows.tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM hbtn_0d_tvshows.tv_shows
      JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
      JOIN hbtn_0d_tvshows.tv_genres ON tv_genres.id = tv_show_genres.genre_id
      WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title;
