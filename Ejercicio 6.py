#6 Programa para calcular el descuento de una compra

compra = float(input("Introduce el monto de la compra: $"))

if compra > 100:

    descuento = compra * 0.30

    total = compra - descuento

    print(f"felicidades! usted tiene un monto final con descuento que es del 30% = ${descuento:.2f}")

else:
    
    total = compra

    print(f"No se aplica descuento. El monto final tiene que ser mayor a $100: ${total:.2f}")    

    print(f"El monto final a pagar es: ${total:.2f}") 



