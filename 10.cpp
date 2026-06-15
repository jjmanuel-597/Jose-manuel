SELECT d.nombre_departamento, 
       AVG(e.salario) AS salario_promedio
FROM Empleados e
INNER JOIN Departamentos d ON e.id_departamento = d.id_departamento
GROUP BY d.nombre_departamento
HAVING AVG(e.salario) > 4000.00;
