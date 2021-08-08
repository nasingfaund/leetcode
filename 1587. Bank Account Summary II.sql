select name, sum(amount) as balance from Users inner join Transactions T on Users.account = T.account group by T.account, name having sum(amount) > 10000;
