SELECT e.name
FROM Employee AS e
JOIN Employee AS r
ON e.id = r.managerId
GROUP BY e.id, e.name
HAVING COUNT(r.id) >= 5;

    



#select name from Employee
#where id in (select managerId from Employee group by managerId having count(managerId)>=5)



