-- actors who have not starred in any film

select distinct moviestar.name
from moviestar, starsin
where moviestar.name not in (select s.starname
								from starsin as s)