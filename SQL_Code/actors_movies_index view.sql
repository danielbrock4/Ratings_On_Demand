 SELECT DISTINCT upper("left"(am.actor_name, 1)) AS actorindex
   FROM actors_movies am;