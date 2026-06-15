/*
Enunciado: Dado un número, si es par se divide entre 2; si es impar se multiplica por 3 y suma 1. Repetir hasta llegar a 1.
Requerimientos: Usa while (!= 1), if-else para la paridad y los operadores aritméticos.
*/

let n = 27; // Cambia este valor para probar
console.log('Inicio:', n);

while (n != 1) {
	if (n % 2 === 0) {
		n = n / 2;
	} else {
		n = n * 3 + 1;
	}
	console.log(n);
}

