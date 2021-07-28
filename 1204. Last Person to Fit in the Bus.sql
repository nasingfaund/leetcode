select person_name  from (select *, sum(weight) over (order by turn) as cum_sum
from Queue order by turn desc ) T where T.cum_sum <= 1000 limit 1;
