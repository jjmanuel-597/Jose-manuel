/*
Enunciado: Haz un conteo desde 10 hasta 0 y al final imprime "¡Despegue!".
Requerimientos: Usa un bucle while, el operador -- y un if final.
*/
let contador = 10;

while (contador >= 0) {
	console.log(contador);
	contador--;
}

if (contador < 0) {
	console.log("¡Despegue!");
}

