# Tarea-TDD
## Integrantes
| Nombre                             | Username         |
|------------------------------------|------------------|
| Gustavo Alonso González Anabalon   | SkullKarl        |
| Sebastian Emir Garcias Cabrera     | SebaGc123        |
| Sofía Ignacia López Aguilera       | lulunkaii        |

## Descripción del proyecto
Este proyecto implementa la lógica y pruebas para el juego de dados **Dudo** utilizando la metodología de Desarrollo Guiado por Pruebas (TDD). Toda la lógica implementada fue obtenida de la página: https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho

## Instrucciones de instalación

1. **Clone el repositorio:**

   ```sh
   git clone https://github.com/SkullKarl/Tarea-TDD.git
   cd Tarea-TDD
2. **Instale las dependencias:**
    ```sh
    pip install -r requirements.txt
3. **Ejecute los test para verificar la instalación:**
    ```sh
    pytest
## Estructura del proyecto
```text
src/
├── juego/
│   ├── dado.py
│   ├── cacho.py
│   ├── validador_apuesta.py
│   ├── contador_pintas.py
│   ├── arbitro_ronda.py
│   └── gestor_partida.py
├── servicios/
│   └── generador_aleatorio.py
tests/
├── test_dado.py
├── test_cacho.py
├── test_validador_apuesta.py
├── test_contador_pintas.py
├── test_arbitro_ronda.py
└── test_gestor_partida.py
