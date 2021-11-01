SELECT 
	mov.original_title,
	mov.votes,
	length(mov.title) AS title_length,
    "substring"(mov.date_published, 6, 2)::integer AS month_number,
    mov.genre,
    mov.duration,
    mov.avg_vote AS imdb_rating,
    CAST(substring(mov.budget, 2, 100) as bigint)/1000000 as budget_millions  ,
    ona.number_of_oscar_nominee_actors AS oscar_nominated_actors_count,
    ond.oscar_nominated_directors AS is_oscar_directed,
	CASE When mpa.mpaa = 'Crap' or mpa.mpaa = 'Not Rated' or mpa.mpaa = 'Unrated' Then 'Unrated' Else mpa.mpaa End as mpa_rating
   FROM "IMDb_Movies_Raw" mov
     LEFT JOIN "Oscar_Nominated_Actor" ona ON mov.imdb_title_id = ona.imdb_title_id
     LEFT JOIN "Oscar_Nominated_Director" ond ON mov.imdb_title_id = ond.imdb_title_id
	 LEFT JOIN "mpaa_rating" mpa ON mov.imdb_title_id = mpa.imdb_title_id
  WHERE mov.language ~~ 'English%'::text AND 
  mov.country ~~ 'USA%'::text AND 
  mov.budget ~~ '$%'::text AND 
  "right"(mov.year, 4)::integer >= 2000 AND 
  "substring"(mov.date_published, 6, 2) <> ''::text AND 
  mov.votes >= 5000 AND 
  mov.budget IS NOT NULL AND 
  CAST(substring(mov.budget, 2, 100) as bigint) > 1000000 AND
  ona.number_of_oscar_nominee_actors IS NOT NULL AND 
  ond.oscar_nominated_directors IS NOT NULL and
  mpa.mpaa IS NOT NULL and
  mpa.mpaa <> 'TV-MA'