select requester_id as id, count(*) as num from (
select accepter_id as requester_id, requester_id as accepter_id,  accept_date from request_accepted
union
select * from request_accepted order by requester_id) T group by requester_id order by num desc limit 1;
