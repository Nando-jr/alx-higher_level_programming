-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres AS s ON tv_genres.id = s.genre_id
INNER JOIN tv_shows AS t ON s.show_id = t.id
WHERE t.title = "Dexter"
ORDER BY tv_genres.name;
