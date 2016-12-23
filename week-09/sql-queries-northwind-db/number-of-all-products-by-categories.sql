-- number of all products by categories

select c.categoryname, count(c.categoryname)
from categories as c
left join products as p
on p.categoryid = c.categoryid
group by categoryname