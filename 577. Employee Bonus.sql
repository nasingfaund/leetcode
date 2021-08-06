select name, Bonus from Employee left join Bonus B on Employee.EmpId = B.EmpId where Bonus < 1000 or Bonus is null;
