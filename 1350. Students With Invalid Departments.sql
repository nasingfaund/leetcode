select id, name from Students where department_id not in (select id from Departments);

select Students.id, Students.name from Students left join Departments on Students.department_id=Departments.id where Departments.id is null;
