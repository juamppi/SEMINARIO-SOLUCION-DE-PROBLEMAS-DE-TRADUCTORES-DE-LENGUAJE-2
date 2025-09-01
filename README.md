# Seminario - Solución de Problemas de Traductores de Lenguaje II

Este repositorio contiene ejemplos y herramientas para el análisis léxico y sintáctico, así como una aplicación de checkpointing para un sistema de órdenes de restaurante.

## Estructura del Proyecto

- **lib/**  
  Contiene la aplicación web para checkpointing de órdenes en restaurante, desarrollada con Next.js y React.

- **cadena/**  
  Incluye ejemplos de manejo de cadenas y la implementación de un analizador sintáctico, con clases como pila, terminal, no terminal, estado, etc.

- **analizador lexico/**  
  Carpeta dedicada al desarrollo de un analizador léxico en Python, con ejemplos y pruebas.

## Uso

### Analizador Léxico

Ejecuta el lexer con:

```sh
python analizador lexico/test_lexer.py
```

### Analizador Sintáctico

Ejecuta el ejemplo de pila:

```sh
python cadena/Analizador sintactico/main.py
```

### Aplicación Restaurante

Instala dependencias y ejecuta Next.js:

```sh
cd lib/checkpointing
npm install
npm run dev
```

## Créditos

- Juan Pablo
- Seminario Traductores de Lenguaje II

---