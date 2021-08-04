select username, activity, startDate, endDate
from (
         select *, count(activity) over(partition by username) cnt,
                ROW_NUMBER() over(partition by username order by startdate desc) n from UserActivity) tbl
where n=2 or cnt<2;


select username, activity, startDate, endDate from (
select
    username,
    activity,
    startDate,
    endDate,
    row_number() over (partition by username order by startDate desc) as ranks,
    count(username) over (partition by username) as counts
from UserActivity) as t
where counts = 1 or ranks = 2;
