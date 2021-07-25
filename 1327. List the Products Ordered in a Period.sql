select product_name, sum(unit) as unit
from products
         inner join Orders O on Products.product_id = O.product_id and extract(month from order_date) = 2
group by O.product_id, product_name
having sum(unit) >= 100;

