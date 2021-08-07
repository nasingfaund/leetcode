select sell_date, count(*) as num_sold, string_agg(distinct product, ',') as products from Activities group by sell_date order by products;
