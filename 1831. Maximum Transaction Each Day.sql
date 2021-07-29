select transaction_id from (select *, max(amount) over (partition by date(day)) as mx
from transactions order by day) T where T.amount = T.mx order by transaction_id;
