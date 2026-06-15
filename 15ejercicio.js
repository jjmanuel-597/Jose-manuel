/*
Enunciado: Imprime un triángulo donde la fila 1 tiene "1", la fila 2 tiene "1 2", etc.
Requerimientos: Usa bucles for anidados donde el límite del interno dependa del externo.
*/

const filas = 5; // Cambia este valor para más/menos filas

for (let i = 1; i <= filas; i++) {
	let fila = '';
	for (let j = 1; j <= i; j++) {
		fila += j;
		if (j < i) fila += ' ';
	}
	console.log(fila);
}

