SELECT e.nombre AS 'Nombre Empleado', d.nombre_departamento AS 'Nombre Departamento'
FROM Empleados e
INNER JOIN Departamentos d ON e.id_departamento = d.id_departamento;
