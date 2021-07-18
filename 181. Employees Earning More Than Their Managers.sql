select Employee.Name as Employee  from Employee inner join Employee E on E.Id = Employee.Managerid where Employee.Salary > E.Salary;
