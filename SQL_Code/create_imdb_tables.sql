--Create IMDB_Awards table

CREATE TABLE IMDB_Awards ( 
	
eventId text,
eventName text,
awardName text,
year text,
categoryName text,
isWinner text,
isPrimary text,
isSecondary text,
isPerson text,
isTitle text,
isCompany text,
const text

 )
 
--Create IMDB_Names table

 CREATE TABLE IMDB_Names ( 
	
imdb_name_id text,
name text,

PRIMARY KEY (imdb_name_id)
 )

--Create IMDB_Titles_Principals table
CREATE TABLE IMDB_Titles_Principals ( 

	
imdb_title_id varchar(255),
ordering integer,
imdb_name_id varchar(255),
category varchar(255)
)