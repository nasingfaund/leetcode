# Write your MySQL query statement below
select E1.name
from employee E1
         left join employee E2 on E1.Id = E2.managerid
group by E1.name
having count(*) >= 5;
