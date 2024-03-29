select seller_id
from (
         select seller_id, rank() over (order by sum(price) desc) as rnk from sales group by seller_id) T
where T.rnk = 1;
