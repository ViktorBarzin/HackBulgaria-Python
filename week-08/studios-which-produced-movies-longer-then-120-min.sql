-- studios which produced movies longer than 120 min

select m.title, m.year, s.name, s.address
from movie as m
left join studio as s
on m.studioname = s.name
where length > 120;