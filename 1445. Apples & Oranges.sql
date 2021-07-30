select sale_date,
       sum(case when fruit = 'apples' then sold_num else -sold_num end) diff
from sales
group by sale_date order by sale_date;

SELECT sale_date,
SUM(CASE WHEN fruit = 'apples' THEN sold_num END) - SUM(CASE WHEN fruit = 'oranges' THEN sold_num END) as diff
FROM Sales GROUP BY sale_date ORDER BY sale_date
