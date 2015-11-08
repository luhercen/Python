/*is211
assignment 10
luis hernandez
*/

CREATE DATABASE Music
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'English_United States.1252'
       LC_CTYPE = 'English_United States.1252'
       CONNECTION LIMIT = -1;


select * from Artiststbl
select * from Albumstbl
select * from Songstbl


CREATE TABLE Artiststbl
(
  
  artistname varchar PRIMARY KEY
);


CREATE TABLE Albumstbl
(
  albumname varchar PRIMARY KEY,
  artistname varchar references Artiststbl(artistname)
);


CREATE TABLE Songstbl
(
  Id int not null,
  Songname varchar NOT NULL,
  Length int NOT NULL,
  albumname varchar references Albumstbl(albumname)
);

