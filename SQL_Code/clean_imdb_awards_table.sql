--Clean IMDB_Awards table for relevant OSCAR info to be used to join with other tables
--Filter awards table to oscar nominated best director and actor/actress awards

CREATE TABLE Oscar_Nominated AS 
 SELECT Distinct
   const as ID,
   1 as Oscar
  FROM imdb_awards
  
    where eventname = 'Academy Awards, USA'and
	      awardname = 'Oscar' and
		  categoryname in ('Best Director', 'Best Actor in a Leading Role', 'Best Actor in a Supporting Role', 'Best Actress in a Leading Role' , 'Best Actress in a Supporting Role')
		  and left(const, 2) = 'nm'
;
