select dept_name,  count(student_id) as student_number from department left join student s on department.dept_id = s.dept_id group by department.dept_id, dept_name order by student_number desc;
