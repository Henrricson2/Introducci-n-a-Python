# Crear y Activar Entornos Virtuales en Python

## Windows (PowerShell o CMD)

### Crear entorno
python -m venv .venv

### Activar entorno
.\.venv\Scripts\Activate



### Desactivar entorno
deactivate

### Instalar librerías
python -m pip install nombre_libreria  
python -m pip install -r requirements.txt  

### Actualizar pip
python -m pip install --upgrade pip

### Comandos útiles
| Acción | Comando |
|--------|----------|
| Ver librerías instaladas | python -m pip list |
| Ver ubicación del entorno | where python |
| Exportar librerías | python -m pip freeze > requirements.txt |
| Instalar desde archivo | python -m pip install -r requirements.txt |

---

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
