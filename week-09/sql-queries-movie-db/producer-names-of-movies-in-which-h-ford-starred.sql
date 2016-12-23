-- producer name of movies in which Harisson Ford starred

select distinct e.name
from movieexec as e
left join movie
on movie.producer
left join  starsin
on starsin.movietitle = movie.title
where starsin.starname = 'Harrison Ford';