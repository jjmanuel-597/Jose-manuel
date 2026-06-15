// SQL statement stored in a C++ raw string literal to avoid compiler errors
const char* create_table_sql = R"SQL(
CREATE TABLE Empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    fecha_contratacion DATE NOT NULL)SQL";
    