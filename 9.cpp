#SELECT d.nombre_departamento, 
       SUM(e.salario) AS total_salarios, 
       COUNT(e.id_empleado) AS total_empleados
FROM Empleados e
INNER JOIN Departamentos d ON e.id_departamento = d.id_departamento
GROUP BY d.nombre_departamento;
