-- Query: List all shows from the hbtn_0d_tvshows_rate database, grouped by their rating sum.
-- Each record should display: TV Show Title and Rating Sum.
-- Results must be sorted in ascending order by the rating sum.
-- The database name "hbtn_0d_tvshows_rate" will be passed as an argument of the mysql command.

SELECT tv_shows.title AS 'TV Show Title', SUM(tv_show_ratings.rate) AS 'Rating Sum'
FROM hbtn_0d_tvshows_rate.tv_shows
INNER JOIN hbtn_0d_tvshows_rate.tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY `Rating Sum` ASC;
