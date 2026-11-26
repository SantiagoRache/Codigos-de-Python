# C-digos-de-Python
Bienvenidos a este repositorio, el cual muestra códigos de programación en Python, desarrollando problemas en la vida real.
---
# Problema 1: Nivel de compromiso de sesiones de clientes

**Autor:** Santiago Rache
**Programa:** Ingeniería de Sistemas, UNAD
**Curso:** Fundamentos de Programación (213022_470)

## Descripción
Programa en Python que evalúa el nivel de compromiso de sesiones de clientes en una plataforma digital. Cada sesión se guarda en una matriz con el formato `[ID del cliente, duración (segundos), número de clics]` y se clasifica como **Alto**, **Medio** o **Bajo**.

## Reglas de clasificación
- **Alto:** duración > 180 segundos y clics > 8.
- **Bajo:** duración < 60 segundos o clics < 3.
- **Medio:** cualquier otro caso.

## Características
- Exige registrar mínimo 5 sesiones.
- Valida que cada dato sea un número entero no negativo (el 0 es válido).
- Muestra un informe con el ID de cada cliente y su clasificación.

## Cómo ejecutarlo
1. Instalar Python.
2. Descargar el archivo `problema 1 Nivel de Compromiso.py`.
3. Ejecutar en la terminal:
```
python problema 1 Nivel de Compromiso.py
```

## Ejemplo de uso
```
Número de sesiones (mínimo 5): 5

Sesión 1
ID del cliente: 101
Duración (segundos): 240
Número de clics: 12
...

INFORME DE COMPROMISO DE SESIONES
-----------------------------------
Cliente 101: Alto
```

## Sustentación
Video en YouTube:
