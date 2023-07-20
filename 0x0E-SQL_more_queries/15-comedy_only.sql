-- Query: List all Comedy shows from the hbtn_0d_tvshows database
-- and display the number of shows linked to each Comedy genre.
-- Each record should display: Show Title.
-- Results must be sorted in ascending order by the show title.
-- The database name "hbtn_0d_tvshows" will be passed as an argument of the mysql command.

SELECT tv_shows.title AS 'Show Title'
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN hbtn_0d_tvshows.tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
