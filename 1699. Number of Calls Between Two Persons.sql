select from_id as person1, to_id as person2, count(*) as call_count, sum(duration) as total_duration
from (select *
      from Calls
      union all
      select C1.to_id as from_id, C1.from_id as to_id, C1.duration
      from Calls C1) T
where T.from_id < T.to_id
group by from_id, to_id;
