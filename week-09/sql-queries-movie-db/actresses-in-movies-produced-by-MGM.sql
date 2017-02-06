-- actresses in movies produced by MGM

select mstar.name
from moviestar as mstar
left join starsin
on mstar.name = starsin.starname
left join movie
on starsin.movietitle = movie.title
join studio
on movie.studioname = studio.name
where studio.name = 'MGM' and mstar.gender = 'F';
