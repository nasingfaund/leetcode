select distinct T.num as ConsecutiveNums
from (
         select *,
                row_number() over (order by id)                  as rw,
                row_number() over (partition by Num order by id) as rn
         from logs
     ) T
group by rw - rn, T.num
having count(*) >= 3;
