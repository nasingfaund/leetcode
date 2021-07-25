SELECT u.user_id         AS buyer_id,
       join_date,
       COUNT(order_date) AS orders_in_2019
FROM Users as u
         LEFT JOIN
     Orders as o
     ON u.user_id = o.buyer_id
         AND extract(year  from order_date) = '2019'
GROUP BY u.user_id, join_date;
