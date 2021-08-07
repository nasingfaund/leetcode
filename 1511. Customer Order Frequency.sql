select customer_id, name
from Customers
where customer_id in (
    select customer_id
    from product
             inner join Orders O on Product.product_id = O.product_id
    where extract(month from order_date) = 6
       or extract(month from order_date) = 7
        and extract(year from order_date) = 2020
    group by customer_id
    having sum(case when extract(month from order_date) = 6 then quantity * Product.price else 0 end) >= 100
       and sum(case when extract(month from order_date) = 7 then quantity * Product.price else 0 end) >= 100);
