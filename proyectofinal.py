# Calculadora de IMC 

def pedir_texto(mensaje):
    valor = ""
    while valor.strip() == "":
        valor = input(mensaje)
        if valor.strip() == "":
            print("❌ Este campo no puede quedar vacío. Intenta de nuevo.")
    return valor

def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() == "":
            print("❌ Este campo no puede quedar vacío. Intenta de nuevo.")
            continue
        try:
            return float(valor)
        except ValueError:
            print("❌ Debes ingresar una cifra válida. Intenta de nuevo.")

#Captura de datos 
nombre = pedir_texto("Nombre: ")
apellido_p = pedir_texto("Apellido paterno: ")
apellido_m = pedir_texto("Apellido materno: ")
edad = pedir_numero("Edad: ")
peso = pedir_numero("Peso en kilogramos: ")
estatura = pedir_numero("Estatura en metros (ej. 1.70): ")

#Cálculo del IMC
imc = peso / (estatura ** 2)

#Clasificación del IMC
if imc < 18.5:
    categoria = "Usted tiene Bajo peso"
elif 18.5 <= imc < 25:
    categoria = "Usted tiene Peso normal"
elif 25 <= imc < 30:
    categoria = "Usted tiene Sobrepeso"
else:
    categoria = "Usted tiene Obesidad"

#Salida de datos
print("\n--- RESULTADOS ---")
print(f"Nombre completo: {nombre} {apellido_p} {apellido_m}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
print(f"Clasificación: {categoria}")