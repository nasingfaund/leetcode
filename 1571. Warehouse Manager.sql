select name as warehouse_name, sum(units*T.volume) as volume
from (
         select  name, units, Width * Length * Height as volume
         from Warehouse W
                  inner join Products P on W.product_id = P.product_id) T
group by name;
