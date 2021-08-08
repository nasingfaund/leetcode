select name as warehouse_name, sum(width*length*height*units) as volume from Warehouse W inner join Products P on W.product_id = P.product_id group by name;
