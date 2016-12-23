-- get studio name and actors in movies produced by this studio

select s.name, moviestar.name
from studio as s
left join movie
on movie.studioname = studio.name
left join starsin 
on starsin.movietitle = movie.title
left join moviestar
on starsin.starname = moviestar.name;