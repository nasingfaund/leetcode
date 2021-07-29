with cte as (
    select account_id,
           sum(case when income < 20000 then 1 else 0 end)                      low,
           sum(case when income >= 20000 and income <= 50000 then 1 else 0 end) average,
           sum(case when income > 50000 then 1 else 0 end)                      high
    from accounts
    group by account_id)
select 'Low Salary' as category, sum(cte.low) as accounts_count from cte
union
select 'Average Salary' as category, sum(cte.average) as accounts_count
from cte
union
select 'High Salary' as category, sum(cte.high) as accounts_count
from cte;

