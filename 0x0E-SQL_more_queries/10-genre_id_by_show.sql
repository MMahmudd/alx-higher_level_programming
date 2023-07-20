-- Query: List all shows from the hbtn_0d_tvshows database that have at least one genre linked.
-- Each record should display: TV Show Title and Genre ID.
-- Results must be sorted in ascending order by TV Show Title and Genre ID.
-- The database name "hbtn_0d_tvshows" will be passed as an argument of the mysql command.

SELECT tv_shows.title AS 'TV Show Title', tv_show_genres.genre_id AS 'Genre ID'
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
