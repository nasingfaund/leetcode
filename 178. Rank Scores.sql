select  score, dense_rank() over (order by score desc) as Rank from Scores;
SELECT
    score,
    (SELECT count(distinct score) FROM scores WHERE score >= s.score) Rank
FROM scores s
ORDER BY score desc
