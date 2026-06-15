#include <iostream>

int main() {
	std::cout << "-- SQL to run on the database:\n";
	std::cout << "UPDATE Empleados\nSET salario = salario * 1.10\nWHERE id_empleado = 2;\n";
	return 0;
}
