select star.name
from moviestar as star, starsin
where starsin.movietitle like "%Terms%" and star.name==starsin.starname and star.gender="M"

