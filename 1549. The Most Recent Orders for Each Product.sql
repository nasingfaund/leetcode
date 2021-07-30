select product_name, Orders.product_id, order_id, order_date
from Orders
         inner join Products on Orders.product_id = Products.product_id
where (Orders.product_id, Orders.order_date) in (select product_id, max(order_date) as order_date
                                                 from Orders
                                                 group by product_id)
order by product_name, product_id, order_id;
