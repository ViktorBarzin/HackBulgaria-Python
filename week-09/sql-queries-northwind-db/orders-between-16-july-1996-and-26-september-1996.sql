-- orders between 16-ти юли 1996 и 26 септемви 1996 with employees names
-- how are dates compared in sqlite wtf?

select e.firstname, e.lastname, o.orderid, o.orderdate
from employees as e
left join orders as o
on o.employeeid = e.employeeid
where   o.orderdate <= Datetime('1996-07-16 12:00:00')
order by datetime(o.orderdate) desc