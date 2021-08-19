
select activity from Friends group by activity having count(activity) not  in
(select min(ct)
from (
         select count(activity) as ct
         from Friends
         group by activity) T
union
select max(ct)
from (
         select count(activity) as ct
         from Friends
         group by activity) T);


select activity
from friends
group by activity
having count(*)> (select count(*) from friends group by activity order by 1 limit 1)
   and count(*)< (select count(*) from friends group by activity order by 1 desc limit 1)
