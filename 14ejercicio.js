/*
Enunciado: Convierte un número decimal a texto binario a base de pura matemática.
Requerimientos: Usa while, saca el bit con %, reduce el número con división y Math.floor(), y concatena strings al revés.
*/

let numero = 156; // Cambia este valor para probar

if (numero === 0) {
	console.log('0');
} else {
	let n = Math.floor(Math.abs(numero));
	let binarioReves = '';

	while (n > 0) {
		const bit = n % 2;
		binarioReves += bit; // concatenando al revés
		n = Math.floor(n / 2);
	}

	const binario = binarioReves.split('').reverse().join('');
	console.log(binario);
}

