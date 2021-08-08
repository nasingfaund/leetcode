select machine_id,
       round((sum(case when activity_type = 'end' then timestamp else 0 end -
        case when activity_type = 'start' then timestamp else 0 end) / count(distinct activity_type))::numeric, 3) as processing_time
from Activity
group by machine_id;


select machine_id,
       round((sum(case when activity_type = 'end' then timestamp else -timestamp end) / count(distinct activity_type))::numeric, 3) as processing_time
from Activity
group by machine_id;
