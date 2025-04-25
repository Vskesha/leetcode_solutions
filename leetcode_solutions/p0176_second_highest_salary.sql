-- Write your PostgreSQL query statement below
select(
    select distinct salary
    from Employee
    order by salary desc
    offset 1 limit 1
) as SecondHighestSalary;

-- Write your PostgreSQL query statement below
select max(salary) as SecondHighestSalary
from Employee
where salary < (select max(salary) from Employee);
