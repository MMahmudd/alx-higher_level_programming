-- Query: List all shows and their linked genres from the hbtn_0d_tvshows database.
-- If a show doesn’t have a genre, display NULL in the genre column.
-- Each record should display: TV Show Title and Genre Name.
-- Results must be sorted in ascending order by the show title and genre.
-- The database name "hbtn_0d_tvshows" will be passed as an argument of the mysql command.

SELECT tv_shows.title AS 'TV Show Title', tv_genres.name AS 'Genre Name'
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN hbtn_0d_tvshows.tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
