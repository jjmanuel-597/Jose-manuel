/*
Enunciado: Verifica si un número (ej. 28) es igual a la suma de sus divisores.
Requerimientos: Usa un for para buscar divisores con %, acumula la suma y compara al final con ===.
*/

let n = 28; // Cambia este valor para probar
let suma = 0;

for (let i = 1; i <= n - 1; i++) {
	if (n % i === 0) {
		suma += i;
	}
}

if (suma === n) {
	console.log(n + ' es un número perfecto.');
} else {
	console.log(n + ' no es un número perfecto. Suma de divisores = ' + suma);
}

