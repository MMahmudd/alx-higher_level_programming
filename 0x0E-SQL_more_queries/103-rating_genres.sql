-- Query: List all genres from the hbtn_0d_tvshows_rate database, grouped by their rating sum.
-- Each record should display: Genre Name and Rating Sum.
-- Results must be sorted in descending order by the rating sum.
-- The database name "hbtn_0d_tvshows_rate" will be passed as an argument of the mysql command.

SELECT tv_genres.name AS 'Genre Name', SUM(tv_show_ratings.rate) AS 'Rating Sum'
FROM hbtn_0d_tvshows_rate.tv_genres
INNER JOIN hbtn_0d_tvshows_rate.tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN hbtn_0d_tvshows_rate.tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY 'Rating Sum' DESC;
