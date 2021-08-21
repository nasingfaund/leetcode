# Write your MySQL query statement below
select sum(apple_count) as apple_count, sum(orange_count) as orange_count
from (
         select B1.apple_count + case when B1.chest_id = C.chest_id then C.apple_count else 0 end   as apple_count,
                B1.orange_count + case when B1.chest_id = C.chest_id then C.orange_count else 0 end as orange_count
         from boxes B1
                  left join Chests C on B1.chest_id = C.chest_id) T;
