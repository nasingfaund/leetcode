# Write your MySQL query statement below
with recursive cte (n) as (
    select 1
    union
    select n + 1
    from cte
    where n < 100
)
select n as ids
from cte where n <= (select max(customer_id) from Customers) and n not in (select customer_id from Customers);
