/*
Enunciado: Calcula el factorial de un número (ej. 5! = 120).
Requerimientos: Inicia un resultado en 1, usa un for decreciente y el operador *=.
*/
let n = 5; // Cambia este valor para probar
let resultado = 1;

for (let i = n; i >= 1; i--) {
	resultado *= i;
}

console.log(n + "! = " + resultado);

