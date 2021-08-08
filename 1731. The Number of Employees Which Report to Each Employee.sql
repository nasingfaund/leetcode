select E1.employee_id, E1.name, count(*) as reports_count, round(avg(E2.age)) as average_age
from Employees E1
         inner join employees E2 on E1.employee_id = E2.reports_to
group by E1.employee_id, E1.name
order by employee_id;
