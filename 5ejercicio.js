/*
Enunciado: Dada una letra, evalúa si es vocal o consonante.
Requerimientos: Usa if-else y operadores lógicos como || (OR), o un switch múltiple.
*/
let letra = 'A'; // Cambia este valor para probar

if (typeof letra === 'string' && letra.length === 1 && /[a-zA-Z]/.test(letra)) {
	const l = letra.toLowerCase();
	if (l === 'a' || l === 'e' || l === 'i' || l === 'o' || l === 'u') {
		console.log('Vocal');
	} else {
		console.log('Consonante');
	}
} else {
	console.log('Entrada inválida: introduce una sola letra.');
}

