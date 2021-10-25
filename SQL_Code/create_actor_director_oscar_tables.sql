-- Create two seperate tables to use with main data set including oscar nominated actors and oscar nominated directors

--Create new table for the count of oscar nominated actors that played in each movie

CREATE TABLE NumberOf_Oscar_Nominated_Actors As

Select

tp.imdb_title_id,
sum(COALESCE(oscar_nominated.oscar,0)) as Number_Of_Oscar_Nominee_Actors


From imdb_titles_principals as tp

Left Join oscar_nominated on  tp.imdb_name_id = oscar_nominated.id


Where category in ('actor' , 'actress')

Group By tp.imdb_title_id

--Create new table for the oscar_nominated directors who directed each movie

CREATE TABLE Oscar_Nominated_Directors As

Select

tp.imdb_title_id,
sum(COALESCE(oscar_nominated.oscar,0)) as Oscar_Nominated_Directors


From imdb_titles_principals as tp

Left Join oscar_nominated on  tp.imdb_name_id = oscar_nominated.id


Where category in ('director')

Group By tp.imdb_title_id

