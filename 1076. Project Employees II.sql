select project_id  from Project group by project_id having count(project_id)=(  SELECT count(project_id)
    FROM project
    GROUP BY project_id
    ORDER BY count(employee_id) desc
    LIMIT 1)
