/*
Enunciado: Con tres variables (num1, num2 y operador como texto "+", "-", "*", "/"), imprime el resultado matemático.
Requerimientos: Usa switch para evaluar el operador y un if para evitar dividir entre cero.
*/
let num1 = 10;
let num2 = 2;
let operador = '/'; // '+', '-', '*', '/'

if (operador === '/' && num2 === 0) {
	console.log('Error: División por cero no permitida.');
} else {
	switch (operador) {
		case '+':
			console.log(num1 + num2);
			break;
		case '-':
			console.log(num1 - num2);
			break;
		case '*':
			console.log(num1 * num2);
			break;
		case '/':
			console.log(num1 / num2);
			break;
		default:
			console.log('Operador inválido. Usa "+", "-", "*" o "/".');
	}
}

