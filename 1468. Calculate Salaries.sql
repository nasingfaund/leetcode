select T.company_id, employee_id, employee_name, round(salary * (1 - tax)) as salary
from (
         select s1.company_id,
                case
                    when max(salary) < 1000 then 0
                    when 1000 <= max(salary) and max(salary) <= 10000 then 0.24
                    when max(salary) >= 10000 then 0.49 end as tax
         from salaries S1
         group by s1.company_id) T
         inner join Salaries S2 on T.company_id = s2.company_id

