-- all movies whose prodcution cost is greater than "Merv Griffin" 's

select m1.title
from movie as m1
join movieexec as me
on m1.producer = me.cert
where me.networth > (select me2.networth
						from movieexec as me2
						where me2.name = "Merv Griffin" );