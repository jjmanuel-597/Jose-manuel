/*
Enunciado: Dibuja un cuadrado de 5x5 hecho de asteriscos * en la consola.
Requerimientos: Usa bucles for anidados y concatena strings por cada fila.
*/

const size = 5; // tamaño del cuadrado

for (let row = 0; row < size; row++) {
	let fila = '';
	for (let col = 0; col < size; col++) {
		fila += '*';
	}
	console.log(fila);
}

