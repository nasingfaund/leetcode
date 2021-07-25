select Countries.country_name,
       case
           when avg(weather_state) <= 15 then 'Cold'
           when avg(weather_state) >= 25 then 'Hot'
           else 'Warm'
           end weather_type
from Countries
         inner join weather w on Countries.country_id = w.country_id
where extract(month from day) = 11
group by country_name;
