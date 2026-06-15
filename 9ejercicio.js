/*
Enunciado: Determina si un número dado es primo.
Requerimientos: Usa una bandera booleana (true/false), un for hasta la mitad del número, el operador % y un break.
*/
let n = 29; // Cambia este valor para probar
let esPrimo = true;

if (n <= 1) {
	esPrimo = false;
} else {
	for (let i = 2; i <= Math.floor(n / 2); i++) {
		if (n % i === 0) {
			esPrimo = false;
			break;
		}
	}
}

if (esPrimo) {
	console.log(n + ' es primo');
} else {
	console.log(n + ' no es primo');
}

