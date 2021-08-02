select Department.Name as Department, T.name as Employee, Salary
from (select *, dense_rank() over (partition by DepartmentId order by Salary desc ) as rnk from Employee) T
         inner join Department on Department.id = T.DepartmentId
where T.rnk <= 3
order by Department, Salary desc;
