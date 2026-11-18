import psycopg


# ============================================================
# CONEXIÓN A POSTGRESQL
# ============================================================

HOST = "localhost"
PORT = 5432
DBNAME = "proyecto_almacen"
USER = "postgres"
PASSWORD = "COMPLETAR"


def conectar():
    """
    Abre y devuelve una conexión a PostgreSQL.
    Completar los datos de conexión antes de ejecutar la aplicación.
    """

    return psycopg.connect(
        host=HOST,
        port=PORT,
        dbname=DBNAME,
        user=USER,
        password=PASSWORD
    )


# ============================================================
# CATEGORÍAS
# ============================================================

def cargar_categorias():
    """
    Devuelve una lista de categorías ordenadas alfabéticamente.

    Cada elemento debe tener este formato:
    {
        "categoriaid": ...,
        "nombre": ...
    }
    """

    conexion = conectar()
    cursor = conexion.cursor()

    # TODO:
    # Completar la consulta SQL.
    #
    # Debe:
    # - obtener categoriaid y nombre;
    # - consultar la tabla stock.categorias;
    # - ordenar alfabéticamente por nombre.

    sql = """
        SELECT categoriaid, nombre 
        FROM stock.categorias 
        ORDER BY nombre
    """

    cursor.execute(sql)

    filas = cursor.fetchall()

    lista = []

    for fila in filas:
        categoria = {
            "categoriaid": fila[0],
            "nombre": fila[1]
        }

        lista.append(categoria)

    cursor.close()
    conexion.close()

    return lista


# ============================================================
# PRODUCTOS
# ============================================================

def cargar_productos(categoriaid=None):
    """
    Devuelve una lista de productos.

    Si categoriaid es None, debe devolver todos los productos.
    Si categoriaid tiene un valor, debe devolver solamente
    los productos pertenecientes a esa categoría.

    Cada elemento debe tener este formato:
    {
        "productoid": ...,
        "nombre": ...,
        "descripcion": ...,
        "precio": ...,
        "stock": ...,
        "categoriaid": ...,
        "categoria": ...
    }
    """

    conexion = conectar()
    cursor = conexion.cursor()

    if categoriaid is None:

        # TODO:
        # Completar la consulta SQL para traer todos los productos.
        #
        # Debe:
        # - consultar stock.productos;
        # - unir con stock.categorias mediante INNER JOIN;
        # - obtener también el nombre de la categoría;
        # - ordenar alfabéticamente por nombre del producto.
        #
        # IMPORTANTE:
        # El orden de las columnas del SELECT debe coincidir con
        # las posiciones fila[0], fila[1], etc. usadas más abajo.

        sql = """
            SELECT p.productoid, p.nombre, p.descripcion, p.precio, p.stock, p.categoriaid, c.nombre AS categoria
            FROM stock.productos p
            INNER JOIN stock.categorias c ON p.categoriaid = c.categoriaid
            ORDER BY p.nombre
        """

        cursor.execute(sql)

    else:

        # TODO:
        # Completar la consulta SQL para traer solamente
        # los productos de la categoría recibida.
        #
        # Debe:
        # - consultar stock.productos;
        # - unir con stock.categorias mediante INNER JOIN;
        # - filtrar por categoriaid;
        # - ordenar alfabéticamente por nombre del producto.
        #
        # Utilizar %s para recibir el parámetro.

        sql = """
            SELECT p.productoid, p.nombre, p.descripcion, p.precio, p.stock, p.categoriaid, c.nombre AS categoria
            FROM stock.productos p
            INNER JOIN stock.categorias c ON p.categoriaid = c.categoriaid
            WHERE p.categoriaid = %s
            ORDER BY p.nombre
        """

        cursor.execute(sql, (categoriaid,))

    filas = cursor.fetchall()

    lista = []

    for fila in filas:
        producto = {
            "productoid": fila[0],
            "nombre": fila[1],
            "descripcion": fila[2],
            "precio": float(fila[3]),
            "stock": fila[4],
            "categoriaid": fila[5],
            "categoria": fila[6]
        }

        lista.append(producto)

    cursor.close()
    conexion.close()

    return lista


# ============================================================
# INSERTAR PRODUCTO
# ============================================================

def insertar_producto(nombre, descripcion, precio, stock, categoriaid):
    """
    Inserta un nuevo producto y devuelve el productoid generado.
    """

    conexion = conectar()
    cursor = conexion.cursor()

    # TODO:
    # Completar la sentencia INSERT.
    #
    # Debe:
    # - insertar nombre, descripcion, precio, stock y categoriaid;
    # - utilizar parámetros %s;
    # - devolver el productoid generado mediante RETURNING.

    sql = """
        INSERT INTO stock.productos (nombre, descripcion, precio, stock, categoriaid) 
        VALUES (%s, %s, %s, %s, %s) 
        RETURNING productoid
    """

    cursor.execute(
        sql,
        (nombre, descripcion, precio, stock, categoriaid)
    )

    productoid = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return productoid


# ============================================================
# MODIFICAR PRODUCTO
# ============================================================

def modificar_producto(
    productoid,
    nombre,
    descripcion,
    precio,
    stock,
    categoriaid
):
    """
    Modifica un producto existente.

    Devuelve True si se modificó alguna fila.
    Devuelve False si no se encontró el productoid.
    """

    conexion = conectar()
    cursor = conexion.cursor()

    # TODO:
    # Completar la sentencia UPDATE.
    #
    # Debe:
    # - modificar nombre, descripcion, precio, stock y categoriaid;
    # - identificar el producto mediante productoid;
    # - utilizar parámetros %s.

    sql = """
        UPDATE stock.productos 
        SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoriaid = %s 
        WHERE productoid = %s
    """

    cursor.execute(
        sql,
        (
            nombre,
            descripcion,
            precio,
            stock,
            categoriaid,
            productoid
        )
    )

    modificado = cursor.rowcount > 0

    conexion.commit()

    cursor.close()
    conexion.close()

    return modificado


# ============================================================
# BORRAR PRODUCTO
# ============================================================

def borrar_producto(productoid):
    """
    Elimina un producto.

    Devuelve True si se eliminó alguna fila.
    Devuelve False si no se encontró el productoid.
    """

    conexion = conectar()
    cursor = conexion.cursor()

    # TODO:
    # Completar la sentencia DELETE.
    #
    # Debe:
    # - eliminar un producto de stock.productos;
    # - identificarlo mediante productoid;
    # - utilizar un parámetro %s.

    sql = "DELETE FROM stock.productos WHERE productoid = %s"

    cursor.execute(sql, (productoid,))

    borrado = cursor.rowcount > 0

    conexion.commit()

    cursor.close()
    conexion.close()

    return borrado
def cargar_estadisticas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM stock.productos")
    total_productos = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(precio) FROM stock.productos")
    precio_promedio = cursor.fetchone()[0]
    precio_promedio = float(precio_promedio) if precio_promedio is not None else None

    cursor.execute("SELECT nombre FROM stock.productos ORDER BY precio DESC LIMIT 1")
    fila = cursor.fetchone()
    producto_mas_caro = fila[0] if fila else None

    cursor.execute("SELECT nombre FROM stock.productos ORDER BY precio ASC LIMIT 1")
    fila = cursor.fetchone()
    producto_mas_barato = fila[0] if fila else None

    cursor.execute("SELECT nombre FROM stock.productos ORDER BY stock DESC LIMIT 1")
    fila = cursor.fetchone()
    producto_mayor_stock = fila[0] if fila else None

    cursor.execute("SELECT SUM(stock) FROM stock.productos")
    unidades_stock = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(precio * stock) FROM stock.productos")
    valor_inventario = cursor.fetchone()[0]
    valor_inventario = float(valor_inventario) if valor_inventario is not None else 0.0

    cursor.execute("""
        SELECT c.nombre, COUNT(p.productoid)
        FROM stock.categorias c
        LEFT JOIN stock.productos p ON c.categoriaid = p.categoriaid
        GROUP BY c.categoriaid, c.nombre
        ORDER BY c.nombre
    """)
    productos_por_categoria = [
        {"categoria": fila[0], "cantidad": fila[1]} for fila in cursor.fetchall()
    ]

    cursor.execute("""
        SELECT c.nombre
        FROM stock.categorias c
        LEFT JOIN stock.productos p ON c.categoriaid = p.categoriaid
        WHERE p.productoid IS NULL
    """)
    categorias_sin_productos = [fila[0] for fila in cursor.fetchall()]

    cursor.close()
    conexion.close()

    return {
        "total_productos": total_productos,
        "precio_promedio": precio_promedio,
        "producto_mas_caro": producto_mas_caro,
        "producto_mas_barato": producto_mas_barato,
        "producto_mayor_stock": producto_mayor_stock,
        "unidades_stock": unidades_stock,
        "valor_inventario": valor_inventario,
        "productos_por_categoria": productos_por_categoria,
        "categorias_sin_productos": categorias_sin_productos
    }