-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres g ON tv_shows.id = g.show_id
INNER JOIN tv_genres t ON g.genre_id = t.id
WHERE t.name = 'Comedy'
ORDER BY tv_shows.title ASC;
