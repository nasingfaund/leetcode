select left(order_date::text, 7) as month, count(distinct order_id) order_count, count(distinct customer_id) customer_count
from orders
where invoice > 20
group by month;
