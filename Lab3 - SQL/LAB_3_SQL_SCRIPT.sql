-- Mile Stosic, Liam Salass, and Charlotte Lombard.
-- 2023-02-16

-- Uses the given employees data base.
USE employees;

-- Question 1, Selects all the data from the salaries and employees table columns
SELECT * FROM salaries, employees;

-- Question 2, Retreives the data from salaries where individuals that have a salary over 10000 when multipled by 1.7.
SELECT * FROM salaries WHERE salary * 1.7 > 100000;

-- Question 3, Gets the average salary for the employees with an ID greater than 1510.
SELECT avg(salary) from salaries where emp_no > 1510;

-- Question 4, Groups specific employee numbers with there appropriate salaries.
SELECT emp_no, avg(salary) from salaries GROUP BY emp_no, salary;

-- Question 5, Joins the first name and last name of an employee and there specifc salary in one table.
SELECT employees.first_name, employees.last_name, salaries.salary FROM employees JOIN salaries ON employees.emp_no=salaries.emp_no;

-- Question 6, This procedure accepts an employee number as an input, and shows the average salary associated with this employee number.
DELIMITER $$
CREATE PROCEDURE emp_avg_salary(IN p_emp_no INT)
BEGIN
	SELECT AVG(salary) FROM salaries where p_emp_no = emp_no;
END $$
DELIMITER ;

-- Example Showing the Prodecure above executes correctly, the correct output should be '48193.8000'.
CALL emp_avg_salary(11300);