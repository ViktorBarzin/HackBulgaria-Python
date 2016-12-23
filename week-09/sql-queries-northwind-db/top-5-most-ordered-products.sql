-- top 5 most ordered items

select p.productname, count(p.productname) as "Times ordered"
from products as p
left join "order details" as od
on p.productid = od.productid
group by productname
order by "Times ordered" desc
limit 5