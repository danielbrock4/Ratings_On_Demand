 SELECT ma."eventName" AS eventname,
    ma."awardName",
    m.title
   FROM "Movie_Award" ma
     JOIN "Movies" m ON ma.const = m.imdb_title_id
  GROUP BY ma."eventName", ma."awardName", m.title;