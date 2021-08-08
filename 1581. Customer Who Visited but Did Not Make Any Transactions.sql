select customer_id, sum( case when transaction_id is null then 1 else 0 end) as count_no_trans
from visits
         left join Transactions T on Visits.visit_id = T.visit_id
group by customer_id having  sum( case when transaction_id is null then 1 else 0 end) >0;


select customer_id, count(visit_id) as count_no_trans
from visits
where visit_id not in (select visit_id from transactions)
group by customer_id
