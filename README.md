# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Deja acá el link a tu video explicando tu solución con tus palabras

https://drive.google.com/file/d/1nD-kodD_MnUbScxIk0-8ALCEgyN837ot/view


Documentacion:

    Para resolver el problema, en primera instancia se plantean la capacidad fisica de poder colocar un panel en las dimensiones del techo. por lo cual primero se verifica que el panel, no sea mas grande que las medidas del techo. para que no quede sobrando.
    luego al ser un techo cuadrado, se puede calcular el area de los paneles como del techo y ver cuantas veces enteras cabe el area del panel en el area del techo, retornando el valor entero de cuantos paneles caben.

    primero se valida que las dimenciones del panel, no sean mayores a las del roof

    posterior se crean variables para poder resolver los calculos matematicos: 
    area_panel se encarga de calcular el area del panel
    area_roof se encarga de calcular el area del roof o techo

    finalmente, se retorna el valor de la division entera entre area_roof / area_panel
    en caso de que el panel sea mayor a las dimensiones del roof, devulve 0 (es la cantidad de paneles que caben)


    

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
*[Indica cuál bonus implementaste: Opción 1 (techo triangular) o Opción 2 (rectángulos superpuestos)]*
Implementé techo Triangulo

### Explicación del Bonus
*[Explica cómo adaptaste tu algoritmo para resolver el bonus]*

Para el caso del triangulo es un poco mas complejo, ya que la altura varia linealmente, por lo cual no tenemos la misma area que en la base como en la punta. lo mejor es ir diviendo el triangulo en filas, dependiendo de cuantas quepan en la altura del triangulo.
En cada fila, el ancho disponible se va reduciendo. 
por lo cual en cada iteracion nuestro alto disponible sera el disponible menos la altura del panel, en la segunda iteraciones, el disponible menos la altura de 2 paneles, etc.

En este caso solo se intento e implemento posicionar los objetos verticalmente, ya que tambien podria haber algunas formas geometricas en las que se deba calcular la cantidad pero de costado, b x a

Para este test, se implemento un 4 test_cases. En la funcion, se condicionó a cuando el roof fuese como el test 4 osea (6 x 6)


---

## 🤔 Supuestos y Decisiones

*[Si tuviste que tomar algún supuesto o decisión de diseño, explícalo aquí]*
En primera instancia me cuestione si era la forma correcta, asi como en el ejemplo visual entraban 5, pero de costado cabian 2 mas y sobraba la mitad de otro. pero al ser cuadrados y rectangulos, con angulos rectos, es bastante mas facil calcular las areas. como cuando compramos ceramica para el piso (salen los metros que rinde por caja)

