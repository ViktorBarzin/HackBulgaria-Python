-- all movies whose length is greater than "Gone With the Wind" 's

select m1.title
from movie as m1
where m1.length < (select m2.length 
					from movie as m2
					where m2.title = "Gone With the Wind")