# Mi_contador | Aplicación gráfica con Python y Flet

## 1. Información general

- **Nombre del proyecto:** Mi_contador
- **Lenguaje de programación:** Python
- **Biblioteca:** Flet 1.1.0
- **Paradigma:** Programación orientada a objetos (POO)
- **Tipo de aplicación:** Interfaz gráfica interactiva
- **Archivo principal:** `main.py`

## 2. ¿Qué es Flet?

Flet es un framework de Python que permite desarrollar interfaces gráficas interactivas sin necesidad de utilizar HTML, CSS o JavaScript directamente.

Su propósito principal es facilitar la creación de aplicaciones con interfaces modernas utilizando Python.

Permite desarrollar aplicaciones para escritorio, web y dispositivos móviles.

## 3. Instalación y requisitos

Para utilizar Flet se necesita:

- Python instalado.
- pip para administrar paquetes.
- Un editor de código, como Visual Studio Code.
- Una terminal para ejecutar los comandos.

### Instalación

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 4. Componentes gráficos principales

Flet dispone de diferentes controles para construir interfaces gráficas.

| Componente | Función |
|---|---|
| `ft.Page` | Representa la página principal de la aplicación. |
| `ft.Text` | Permite mostrar textos. |
| `ft.Button` | Crea botones interactivos. |
| `ft.Image` | Permite mostrar imágenes. |
| `ft.Container` | Organiza y agrupa elementos visuales. |
| `ft.Row` | Organiza elementos horizontalmente. |
| `ft.Column` | Organiza elementos verticalmente. |

## 5. Programación orientada a eventos

Flet utiliza un modelo basado en eventos para detectar las interacciones del usuario.

Por ejemplo, la propiedad `on_click` permite asociar una función o método a un botón. Cuando el usuario hace clic, se ejecuta el método correspondiente.

En este proyecto se utilizan dos eventos:

- **Incrementar:** aumenta el valor del contador.
- **Reiniciar:** devuelve el contador a cero.

## 6. Ventajas y limitaciones frente a Tkinter

### Ventajas de Flet

- Permite desarrollar interfaces modernas.
- Utiliza Python para construir la interfaz.
- Facilita la creación de aplicaciones interactivas.
- Permite desarrollar aplicaciones para diferentes plataformas.

### Limitaciones de Flet

- Requiere instalar el framework y sus dependencias.
- Utiliza componentes propios que requieren aprendizaje.
- Su funcionamiento y despliegue pueden ser más complejos que los de aplicaciones sencillas con Tkinter.

### Comparación con Tkinter

| Característica | Flet | Tkinter |
|---|---|---|
| Lenguaje | Python | Python |
| Instalación | Requiere instalar Flet | Generalmente viene incluido con Python |
| Interfaz | Moderna y adaptable | Tradicional |
| Desarrollo web | Sí | No de forma nativa |
| Aplicaciones de escritorio | Sí | Sí |
| Curva de aprendizaje | Requiere conocer sus controles | Relativamente sencilla para comenzar |

## 7. Descripción técnica del proyecto

Mi_contador es una aplicación gráfica desarrollada en Python mediante Flet.

Su funcionamiento consiste en mostrar un contador que puede incrementarse o reiniciarse mediante dos botones.

La aplicación utiliza una clase principal para organizar los atributos, métodos y componentes visuales.

## 8. Arquitectura y programación orientada a objetos

El proyecto está organizado alrededor de la clase `ContadorApp`, que contiene los elementos necesarios para controlar la aplicación.

### Clase: ContadorApp

**Atributos:**

- `page`: referencia a la página principal.
- `contador`: almacena el valor actual del contador.
- `texto_contador`: componente visual que muestra el valor.

**Métodos:**

- `__init__(self, page)`: inicializa los atributos y componentes.
- `incrementar(self, e)`: aumenta el contador en una unidad.
- `reiniciar(self, e)`: restablece el contador a cero.
- `construir(self)`: configura la ventana y agrega los controles gráficos.

### Aplicación de POO

Se aplica el principio de encapsulación al agrupar los atributos y métodos relacionados dentro de la clase `ContadorApp`.

En la función `main()` se crea el objeto `aplicacion`, que es una instancia de dicha clase.

## 9. Funcionamiento de los eventos

La aplicación utiliza la propiedad `on_click` para detectar los clics realizados sobre los botones.

**Flujo de ejecución:**

1. El usuario presiona un botón.
2. Flet detecta el evento de clic.
3. Se ejecuta el método asociado.
4. Se modifica el valor del atributo `contador`.
5. Se actualiza la propiedad `value` del componente `texto_contador`.
6. La interfaz muestra el nuevo valor.

## 10. Funcionalidades

La aplicación dispone de dos operaciones principales:

- **Incrementar:** suma una unidad al contador.
- **Reiniciar:** establece el contador en cero.

El componente `ft.Text` permite visualizar los cambios realizados durante la interacción.

## 11. Ejecución del proyecto

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

Al iniciar, se abre una ventana con el título **Contador Interactivo**, donde se puede utilizar el botón Incrementar y el botón Reiniciar.

## 12. Estructura del proyecto

```text
Mi_contador/
├── main.py
├── README.md
├── requirements.txt
├── evidencia/
│   ├── captura1.png
│   └── captura2.png
└── .venv/ (entorno virtual local, no incluido en GitHub)
```

## 13. Evidencias de ejecución

El proyecto incluye capturas de pantalla que muestran la interfaz gráfica y el funcionamiento de los botones de incremento y reinicio.

## 14. Conclusiones

El desarrollo de este proyecto permitió explorar la biblioteca Flet y comprender cómo se construyen interfaces gráficas utilizando Python.

También se aplicaron conceptos de programación orientada a objetos, encapsulación, creación de instancias y programación basada en eventos.

Finalmente, se comprobó cómo las acciones del usuario pueden modificar los datos de una aplicación y actualizar sus componentes visuales.

## 15. Referencias

- [Documentación oficial de Flet](https://docs.flet.dev/)
- [Guía de inicio de Flet](https://flet.dev/docs/getting-started/)
- [Documentación oficial de Python](https://docs.python.org/3/)
- [Documentación de Tkinter](https://docs.python.org/3/library/tkinter.html)

---

**Proyecto académico:** Taller de investigación — Explorando bibliotecas para interfaces gráficas en Python.

**Asignatura:** Programación Orientada a Objetos.
