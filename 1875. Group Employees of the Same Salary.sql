select employee_id, name, salary, dense_rank() over (order by salary) as team_id from (select *, count(*) over (partition by salary order by salary ) as ct from employees) T where T.ct > 1;
