# Seminario - Solución de Problemas de Traductores de Lenguaje II

Este repositorio contiene ejemplos y herramientas para el **análisis léxico y sintáctico**, así como una **aplicación de checkpointing para un sistema de órdenes de restaurante**.  
El proyecto forma parte del curso **Seminario: Solución de Problemas de Traductores de Lenguaje II**.

---

## 📂 Estructura del Proyecto

- **`lib/`**  
  Contiene la aplicación web para **checkpointing de órdenes en restaurante**, desarrollada con **Next.js** y **React**.

- **`cadena/`**  
  Ejemplos de **manejo de cadenas** y la implementación de un **analizador sintáctico** con pilas de objetos (`ElementoPila`, `Terminal`, `NoTerminal`, `Estado`, etc.).

- **`analizador lexico/`**  
  Implementación de un **analizador léxico en Python**, que reconoce tokens como identificadores, palabras reservadas, operadores, literales, etc.

---

## Uso

###  Analizador Léxico

Ejecuta el lexer con:

```sh
cd "analizador lexico"
python test_lexer.py
