-- get studio name and actors in movies produced by this studio

select s.name as "Studio name", starsin.starname as "Moviestar name"
from studio as s
left join movie
on movie.studioname = s.name
left join starsin
on starsin.movietitle = movie.title
order by s.name;