# ============================================================
# DATOS EN MEMORIA - DICCIONARIOS
# ============================================================

categorias = {
    1: "Almacén - DIC",
    2: "Bebidas - DIC",
    3: "Lácteos - DIC",
    4: "Limpieza - DIC"
}

productos = {
    1: {
        "nombre": "Arroz Integral 1kg - DIC",
        "descripcion": "Arroz integral paquete de 1 kg",
        "precio": 1400.00,
        "stock": 45,
        "categoriaid": 1
    },
    2: {
        "nombre": "Fideos Tallarín 500g - DIC",
        "descripcion": "Fideos secos paquete de 500 g",
        "precio": 980.00,
        "stock": 60,
        "categoriaid": 1
    },
    3: {
        "nombre": "Harina 000 1kg - DIC",
        "descripcion": "Harina de trigo tipo 000",
        "precio": 850.00,
        "stock": 35,
        "categoriaid": 1
    },
    4: {
        "nombre": "Aceite de Girasol 1.5L - DIC",
        "descripcion": "Aceite de girasol botella de 1,5 litros",
        "precio": 3200.00,
        "stock": 25,
        "categoriaid": 1
    },
    5: {
        "nombre": "Azúcar 1kg - DIC",
        "descripcion": "Azúcar común paquete de 1 kg",
        "precio": 1200.00,
        "stock": 50,
        "categoriaid": 1
    },
    6: {
        "nombre": "Agua Mineral 2L - DIC",
        "descripcion": "Agua mineral sin gas",
        "precio": 900.00,
        "stock": 55,
        "categoriaid": 2
    },
    7: {
        "nombre": "Gaseosa Cola 2.25L - DIC",
        "descripcion": "Gaseosa sabor cola",
        "precio": 2800.00,
        "stock": 40,
        "categoriaid": 2
    },
    8: {
        "nombre": "Jugo de Naranja 1L - DIC",
        "descripcion": "Jugo de naranja en envase tetra",
        "precio": 1900.00,
        "stock": 28,
        "categoriaid": 2
    },
    9: {
        "nombre": "Agua Saborizada 1.5L - DIC",
        "descripcion": "Agua saborizada de pomelo",
        "precio": 1600.00,
        "stock": 32,
        "categoriaid": 2
    },
    10: {
        "nombre": "Leche Entera 1L - DIC",
        "descripcion": "Leche entera larga vida",
        "precio": 1300.00,
        "stock": 80,
        "categoriaid": 3
    },
    11: {
        "nombre": "Yogur Natural 190g - DIC",
        "descripcion": "Yogur natural entero",
        "precio": 850.00,
        "stock": 42,
        "categoriaid": 3
    },
    12: {
        "nombre": "Queso Cremoso 500g - DIC",
        "descripcion": "Queso cremoso en trozo",
        "precio": 4500.00,
        "stock": 18,
        "categoriaid": 3
    }
}

def cargar_categorias():
    lista = []

    for categoriaid in categorias:
        categoria = {
            "categoriaid": categoriaid,
            "nombre": categorias[categoriaid]
        }
        lista.append(categoria)

    return lista

def cargar_productos(categoriaid=None):
    lista = []

    for productoid in productos:
        producto = productos[productoid]

        if categoriaid is None or producto["categoriaid"] == categoriaid:
            item = {
                "productoid": productoid,
                "nombre": producto["nombre"],
                "descripcion": producto["descripcion"],
                "precio": producto["precio"],
                "stock": producto["stock"],
                "categoriaid": producto["categoriaid"],
                "categoria": categorias[producto["categoriaid"]]
            }

            lista.append(item)

    return lista

def insertar_producto(nombre, descripcion, precio, stock, categoriaid):
    productoid = max(productos) + 1

    productos[productoid] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock,
        "categoriaid": categoriaid
    }

    return productoid

def modificar_producto(productoid, nombre, descripcion, precio, stock, categoriaid):
    if productoid in productos:
        productos[productoid] = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "categoriaid": categoriaid
        }

        return True

    return False

def borrar_producto(productoid):
    if productoid in productos:
        del productos[productoid]
        return True

    return False