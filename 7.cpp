-- 1. Crear tabla Departamentos
CREATE TABLE Departamentos (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_departamento VARCHAR(100) NOT NULL
);

-- 2. Modificar Empleados para añadir la columna de relación
ALTER TABLE Empleados 
ADD COLUMN id_departamento INT;

-- 3. Crear la restricción de Clave Foránea
ALTER TABLE Empleados 
ADD CONSTRAINT fk_empleados_departamentos
FOREIGN KEY (id_departamento) REFERENCES Departamentos(id_departamento);

-- 4. Insertar datos en Departamentos
INSERT INTO Departamentos (nombre_departamento) VALUES
('Recursos Humanos'),
('Tecnología'),
('Ventas'),
('Marketing');
