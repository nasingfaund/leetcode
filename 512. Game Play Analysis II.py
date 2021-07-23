# Write your MySQL query statement below
select player_id, device_id from Activity where (player_id, event_date) in (select player_id, min(event_date) as event_date from Activity group by player_id);


select distinct player_id, first_value(device_id) over (partition by player_id order by event_date) as device_id
from activity;
