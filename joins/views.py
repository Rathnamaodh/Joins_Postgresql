from django.shortcuts import render

# Create your views here.


"""
select * from joins_shop_a;
select * from joins_shop_b;

--inner join
select * from joins_shop_a inner join joins_shop_b on joins_shop_a.fruit=joins_shop_b.fruit;
--left outer join
select * from joins_shop_a left outer join joins_shop_b on joins_shop_a.fruit=joins_shop_b.fruit;
--right outer join
select * from joins_shop_a right outer join joins_shop_b on joins_shop_a.fruit=joins_shop_b.fruit;
--full outer join
select * from joins_shop_a full outer join joins_shop_b on joins_shop_a.fruit=joins_shop_b.fruit;

source = https://www.youtube.com/watch?v=4_Q2pnmo1tM&ab_channel=SDET-QAAutomationTechie



select * from joins_employee;
select * from joins_salary;
--------------------inner join

SELECT table1.column1, table2.column2...
FROM table1
INNER JOIN table2
ON table1.common_filed = table2.common_field;

select * from joins_employee inner join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
-- specify columns
		
select emp_name,dept,joins_employee.emp_no from joins_employee inner join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
-------------------- left join

SELECT columns
FROM table1
LEFT OUTER JOIN table2
ON table1.column = table2.column;


select * from joins_employee left join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
--specified
select emp_name,dept,joins_employee.emp_no from joins_employee left join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
-------------------- right join

SELECT columns
FROM table1
RIGHT OUTER JOIN table2
ON table1.column = table2.column;

select * from joins_employee right join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
--specified
select emp_name,dept,joins_employee.emp_no from joins_employee right join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
-------------------------------- full outer join
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;



select * from joins_employee full outer join joins_salary on joins_employee.emp_no=joins_salary.emp_no;
--specified
select emp_name,dept,joins_employee.emp_no from joins_employee full outer join joins_salary on joins_employee.emp_no=joins_salary.emp_no;






"""