/*
Enunciado: Imprime los primeros 15 términos de la sucesión de Fibonacci.
Requerimientos: Declara variables para los términos, usa un for y reasigna los valores sumándolos secuencialmente.
*/

let a = 0;
let b = 1;
console.log(a);
console.log(b);

for (let i = 3; i <= 15; i++) {
	let c = a + b;
	console.log(c);
	a = b;
	b = c;
}

