select customer_name, customer_id, order_id, order_date
from (
         select C.customer_id,
                name                                                                    as customer_name,
                order_date,
                order_id,
                row_number() over (partition by C.customer_id order by order_date desc) as rk
         from Orders
                  inner join Customers C on Orders.customer_id = C.customer_id) T
where T.rk < 4
order by customer_name, customer_id, order_date desc;

