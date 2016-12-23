-- producer name and movies produced by the producer of star wars

select me.name, movie.title
from movieexec as me
left join movie
on movie.producer = me.cert
where me.name = (select e.name
					from movie
					left join movieexec as e
					on movie.producer = e.cert
					where movie.title = "Star Wars");
				