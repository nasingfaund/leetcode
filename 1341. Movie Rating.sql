(select name as results from (
select *, dense_rank() over (order by num_rated desc) as rk
from (
         select user_id, count(rating) as num_rated
         from Movie_Rating
         group by user_id
         order by num_rated desc) T) TT inner join Users on Users.user_id=TT.user_id where rk=1 order by name limit 1)
union all
(select title from (select movie_id, avg(rating) as av from Movie_Rating  where extract(year from created_at)=2020 and extract(month from created_at)=2 group by movie_id  ) T inner join Movies on Movies.movie_id = T.movie_id order by av desc, title limit 1);
