select product_name, Orders.product_id, order_id, order_date
from Orders
         inner join Products on Orders.product_id = Products.product_id
         inner join Customers on Orders.customer_id = Customers.customer_id
where (Orders.product_id, Orders.order_date) in (select Orders.product_id, max(order_date)
                                                 from orders
                                                          inner join Products P on Orders.product_id = P.product_id
                                                 group by orders.product_id) order by product_name,product_id,order_id;
