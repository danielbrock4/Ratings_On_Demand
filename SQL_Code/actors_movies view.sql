 SELECT n.imdb_name_id AS actor_movie_id,
    n.name AS actor_name,
    m.title AS movie_title
   FROM "Names" n
     JOIN title_principals tp ON n.imdb_name_id = tp.imdb_name_id
     JOIN "Movies" m ON tp.imdb_title_id = m.imdb_title_id
  WHERE upper("left"(n.name, 1)) !~ '^.*[^A-Za-z].*$'::text
  ORDER BY (upper("left"(n.name, 1)));