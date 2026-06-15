/*
Enunciado: Imprime del 1 al 100. Múltiplos de 3 son "Fizz", de 5 son "Buzz", y de ambos "FizzBuzz".
Requerimientos: Usa for, if - else if - else, el operador % y el lógico &&.
*/

for (let i = 1; i <= 100; i++) {
	if (i % 3 === 0 && i % 5 === 0) {
		console.log('FizzBuzz');
	} else if (i % 3 === 0) {
		console.log('Fizz');
	} else if (i % 5 === 0) {
		console.log('Buzz');
	} else {
		console.log(i);
	}
}

