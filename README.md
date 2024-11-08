# Barebears guess the number
Esta es una aplicación web simple creada con Flask en Python que permite al usuario adivinar un número aleatorio entre 0 y 9. La aplicación responde con diferentes mensajes y GIFs dependiendo de si la adivinanza es demasiado alta, demasiado baja o correcta.

## Descripción
Cuando el usuario visita la ruta principal (`/`), verá un mensaje y una imagen de bienvenida, invitándolo a adivinar un número entre 0 y 9. Para realizar la adivinanza, el usuario debe agregar un número al final de la URL (por ejemplo, `/3`). Dependiendo del número introducido, la aplicación responderá si la adivinanza es demasiado alta, demasiado baja o correcta.

Cada vez que el usuario adivina correctamente, el número se reinicia, y el juego puede comenzar de nuevo.

## Requisitos
Python 3.x
Flask (instalable con `pip install flask`)

## Instalación
1. Clona el repositorio o descarga el archivo server.py.
2. Asegúrate de que Flask esté instalado ejecutando:
```bash
pip install flask
```
3. Ejecuta la aplicación:
```bash
python app.py
```
La aplicación debería estar corriendo en `http://127.0.0.1:5000/` por defecto.

## Cómo jugar
1. Abre tu navegador y navega a `http://127.0.0.1:5000/`.
2. Verás un mensaje de bienvenida que te pide adivinar un número entre 0 y 9.
3. Para adivinar, agrega un número al final de la URL, como `http://127.0.0.1:5000/5`.
4. La aplicación te dirá si tu número es demasiado bajo, demasiado alto o correcto.
5. Si aciertas, el juego se reinicia con un nuevo número aleatorio.

## Rutas
* `/` - Muestra la página principal con un mensaje de bienvenida e instrucciones.
* `/<int:number>/` - Ruta de adivinanza del número. Evalúa si el número ingresado es correcto, demasiado bajo o demasiado alto.

## Ejemplo
1. Ir a `http://127.0.0.1:5000/` para ver el mensaje de bienvenida.
2. Si intentas `http://127.0.0.1:5000/3` y el número es demasiado bajo, la aplicación mostrará un mensaje y un GIF indicando que es "Demasiado bajo!".
3. Si el número es correcto, recibirás una felicitación y la oportunidad de intentarlo nuevamente con un nuevo número.

## Créditos
* GIFs obtenidos de Giphy.
* Día 55 de 100 días de código.
---
¡Disfruta de adivinar el número!
