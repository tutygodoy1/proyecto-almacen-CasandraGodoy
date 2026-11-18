from fastapi import FastAPI
from pydantic import BaseModel
# from datos import datos_diccionario as datos
from datos import datos_postgres as datos
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoriaid: int

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return FileResponse("static/index.html")
    # return {"mensaje": "Sistema de gestión de stock"}

@app.get("/categorias")
def cargar_categorias():
    return datos.cargar_categorias()

@app.get("/productos")
def cargar_productos(categoriaid: int = None):
    return datos.cargar_productos(categoriaid)

@app.post("/productos")
def insertar_producto(producto: Producto):
    productoid = datos.insertar_producto(
        producto.nombre,
        producto.descripcion,
        producto.precio,
        producto.stock,
        producto.categoriaid
    )

    return {"productoid": productoid}

@app.put("/productos/{productoid}")
def modificar_producto(productoid: int, producto: Producto):
    modificado = datos.modificar_producto(
        productoid,
        producto.nombre,
        producto.descripcion,
        producto.precio,
        producto.stock,
        producto.categoriaid
    )

    return {"modificado": modificado}

@app.delete("/productos/{productoid}")
def borrar_producto(productoid: int):
    borrado = datos.borrar_producto(productoid)

    return {"borrado": borrado}

@app.get("/estadisticas")
def cargar_estadisticas():
    return datos.cargar_estadisticas()