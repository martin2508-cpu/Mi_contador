# Mi_contador | Aplicación gráfica con Python y Flet

## 1. Información general

**Nombre del proyecto:** Mi_contador  
**Lenguaje de programación:** Python  
**Framework:** Flet 1.1.0  
**Paradigma:** Programación orientada a objetos (POO)  
**Tipo de aplicación:** Interfaz gráfica interactiva  
**Archivo principal:** `main.py`

## 2. Descripción técnica

Mi_contador es una aplicación gráfica desarrollada en Python mediante el framework Flet. Implementa una interfaz de usuario que permite gestionar un valor numérico a través de eventos asociados a controles interactivos.

La aplicación utiliza una arquitectura basada en una clase principal encargada de encapsular el estado del contador, gestionar sus operaciones y construir los componentes visuales de la interfaz.

## 3. Objetivos

- Explorar el desarrollo de interfaces gráficas mediante Flet.
- Implementar el paradigma de programación orientada a objetos.
- Gestionar eventos de interacción del usuario.
- Manipular dinámicamente las propiedades de los componentes gráficos.
- Separar la lógica de funcionamiento de la construcción de la interfaz.

## 4. Tecnologías y componentes

| Tecnología o componente | Función |
|---|---|
| Python | Lenguaje de programación |
| Flet | Framework de interfaz gráfica |
| `ft.Page` | Representa la página principal |
| `ft.Text` | Muestra información textual |
| `ft.Button` | Permite la interacción del usuario |
| `on_click` | Vincula eventos a métodos |
| `ft.run()` | Inicia la aplicación |

## 5. Arquitectura y programación orientada a objetos

El proyecto está estructurado alrededor de la clase `ContadorApp`, que encapsula los atributos y métodos necesarios para el funcionamiento de la aplicación.

### Clase: ContadorApp

**Atributos:**

- `page`: referencia al objeto de la página principal.
- `contador`: variable que almacena el estado numérico.
- `texto_contador`: componente visual encargado de representar el valor actual.

**Métodos:**

- `__init__(self, page)`: constructor que inicializa el estado y los componentes.
- `incrementar(self, e)`: modifica el contador aumentando su valor en una unidad.
- `reiniciar(self, e)`: restablece el estado numérico a cero.
- `construir(self)`: configura la ventana y agrega los controles gráficos.

### Aplicación de POO

Se implementa la encapsulación al agrupar los datos y comportamientos relacionados dentro de una misma clase. El objeto `aplicacion` es una instancia de `ContadorApp`, responsable de controlar el funcionamiento de la interfaz.

## 6. Programación orientada a eventos

La aplicación utiliza un modelo de interacción basado en eventos.

Los botones registran funciones de retorno (*callbacks*) mediante la propiedad `on_click`.

**Flujo de ejecución:**

1. El usuario interactúa con un botón.
2. Flet detecta el evento de clic.
3. Se ejecuta el método asociado.
4. Se modifica el atributo `contador`.
5. Se actualiza la propiedad `value` del componente `texto_contador`.
6. La interfaz refleja el nuevo estado.

## 7. Funcionamiento de la aplicación

La interfaz dispone de dos operaciones principales:

- **Incrementar:** ejecuta `incrementar()` y suma una unidad al valor almacenado.
- **Reiniciar:** ejecuta `reiniciar()` y asigna cero al contador.

El componente `ft.Text` representa visualmente el estado actual de la aplicación.

## 8. Instalación y configuración

Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto.

Crear entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 9. Ejecución

Desde el directorio raíz del proyecto, ejecutar:

```bash
python main.py
```

## 10. Estructura del proyecto

```text
Mi_contador/
├── main.py
├── README.md
├── requirements.txt
├── evidencia/
│   ├── captura1.png
│   └── captura2.png
└── .venv/ (entorno local, no incluido en GitHub)

```
## 11. Evidencias de ejecución

El repositorio incluye capturas de pantalla que documentan la interfaz gráfica y el funcionamiento de los eventos de incremento y reinicio.

## 12. Conclusiones

El desarrollo permitió implementar una interfaz gráfica funcional utilizando Flet y Python. Se aplicaron conceptos de encapsulación, instanciación de objetos y programación orientada a eventos.

Además, se comprobó cómo los eventos de interacción permiten modificar el estado de una aplicación y reflejar dichos cambios en sus componentes visuales.

## 13. Referencias técnicas

- Documentación oficial de Flet: https://docs.flet.dev/
- Documentación de Python: https://docs.python.org/3/
- Repositorio del proyecto: https://github.com/martin2508-cpu/Mi_contador
