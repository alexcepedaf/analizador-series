# Analizador de Series Numéricas

Aplicación web full-stack para administrar y analizar conjuntos de números enteros

## Stack tecnológico:
- **Backend**: Flask (Python)
- **Frontend**: React con v0.dev
- **Base de datos**: MongoDB
- **Orquestación**: Docker Compose

## Funcionalidad General
- Guardar series de números enteros en la base de datos
- Listar todas las series guardadas
- Calcular MCD de todos los números, media aritmética y desviación estándar de la serie
- Identificar cuáles de los números son primos

## Estructura del Proyecto

```
analizador-series/
├── backend/
│ ├── app/
│ │ ├── main.py # Aplicación Flask y endpoints
│ │ ├── utils.py # Utilidades matemáticas
│ │ ├── models.py # Modelos de datos
│ │ └── database.py # Conexión MongoDB
│ ├── requirements.txt # Dependencias Python
│ └── Dockerfile # Contenedor backend
├── frontend/
│ ├── index.html # Aplicación React completa
│ ├── nginx.conf # Configuración Nginx
│ └── Dockerfile # Contenedor frontend
├── docker-compose.yml # Orquestación de servicios
└── README.md
```

# Instalación y Ejecución

### Prerrequisitos
- Docker
- Docker Compose

### Ejecutar la aplicación
### Clonar el repositorio y ejecutar el docker-compose
```
git clone https://github.com/alexcepedaf/analizador-series-git
cd analizador-series
docker compose up --build
```

### La aplicación estará disponible en:
#### Frontend: http://localhost:3000
#### Backend API: http://localhost:8000
#### MongoDB: localhost:27017

#Uso de la Aplicación

## Interfaz Web
- Abrir http://localhost:3000
- Formulario superior: Ingresar números separados por comas (ej: "12, 15, 21, 30")
- Click "Guardar Serie"
- En el listado: Ver la serie guardada como "Serie 1: [12, 15, 21, 30]"
- Click "Analizar" para ver resultados matemáticos

## API Endpoints
- POST /series
    - Crear una nueva serie de números.
    - Ejemplo:
```
curl -X POST http://localhost:8000/series \
  -H "Content-Type: application/json" \
  -d '{"numbers": [12, 15, 21, 30]}'
```
Respuesta:
```json
{
  "id": "68e44a3341e72564bc3b16b9",
  "numbers": [12, 15, 21, 30],
  "message": "Serie creada exitosamente"
}
```
- GET /series
  - Obtener todas las series guardadas.
  - Ejemplo:
```
curl http://localhost:8000/series
```
Respuesta:
```json
[
  {
    "id": "68e44a3341e72564bc3b16b9",
    "numbers": [12, 15, 21, 30],
    "count": 4,
    "created_at": "2024-10-05T20:15:30.123456"
  }
]
```
- GET /series/{id}/analyze
   - Analizar una serie específica.
   - Ejemplo:
```
curl http://localhost:8000/series/68e44a3341e72564bc3b16b9/analyze
```
Respuesta:
```json
{
  "series_id": "68e44a3341e72564bc3b16b9",
  "gcd": 3,
  "mean": 19.5,
  "std_dev": 6.87,
  "primes": []
}
```
