select unique_id, name from Employees left join EmployeeUNI on Employees.id= EmployeeUNI.id order by  unique_id desc ;
