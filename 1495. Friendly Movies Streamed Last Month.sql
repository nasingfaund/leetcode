select title
from Content
         inner join TVProgram on Content.content_id::int = TVProgram.content_id::int
where extract(month from program_date) = 6 and extract(year from program_date) = 2020
  and Kids_content = 'Y' and content_type='Movies';
