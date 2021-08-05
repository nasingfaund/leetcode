select seller_id
from (
         select seller_id, rank() over (order by t.m desc) as rnk
         from (select seller_id, sum(price) as m from Sales group by seller_id order by m desc) T) TT
where TT.rnk = 1;
