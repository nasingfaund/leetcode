select distinct Customers.customer_id, Customers.customer_name
from Customers
         inner join Orders on Customers.customer_id = Orders.customer_id
where 'A' in (select product_name from Orders where Orders.customer_id = Customers.customer_id)
  and 'B' in (select product_name from Orders where Orders.customer_id = Customers.customer_id)
  and 'C' not in (select product_name from Orders where Orders.customer_id = Customers.customer_id);
