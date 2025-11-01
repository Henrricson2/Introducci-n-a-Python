# Crear y Activar Entornos Virtuales en Python

## Windows (PowerShell o CMD)

### Crear entorno
python -m venv .venv

### Activar entorno
.\.venv\Scripts\Activate



### Desactivar entorno
deactivate

### Instalar librerías
pip install nombre_libreria  
pip install -r requirements.txt  

### Actualizar pip
python.exe -m pip install --upgrade pip

### Comandos útiles
| Acción | Comando |
|--------|----------|
| Ver librerías instaladas | python -m pip list |
| Exportar librerías | python -m pip freeze > requirements.txt |
| Instalar desde archivo | python -m pip install -r requirements.txt |


# Configuracion Git

git config --global user.name "Tu Nombre"
git config --global user.email "tucorreo@ejemplo.com"
git config --list

---
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## macOS / Linux

### Crear entorno
python3 -m venv .venv

### Activar entorno
source .venv/bin/activate

### Desactivar entorno
deactivate

### Instalar librerías
pip3 install nombre_libreria  
pip3 install -r requirements.txt  

### Actualizar pip
python3 -m pip install --upgrade pip



### Comandos útiles
| Acción | Comando |
|--------|----------|
| Ver librerías instaladas | pip3 list |
| Ver ubicación del entorno | which python3 |
| Exportar librerías | pip3 freeze > requirements.txt |
| Instalar desde archivo | pip3 install -r requirements.txt |

---

## Recomendaciones
- Crea un entorno virtual por proyecto.  
- No uses permisos de administrador dentro del entorno.  
- Usa python o python3 según tu sistema.  
- En VS Code selecciona el entorno desde *Select Interpreter*.



