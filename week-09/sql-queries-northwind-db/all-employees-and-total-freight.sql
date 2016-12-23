-- select employee name and total freight
-- todo: everyone has the same frieght?!

select e.firstname, e.lastname , sum(freight)
 from orders, employees as e
 group by e.firstname, e.lastname