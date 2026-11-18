-- ============================================================
-- PROYECTO ALMACÉN
-- Creación y carga inicial de la base de datos
-- ============================================================


-- Crear esquema
CREATE SCHEMA IF NOT EXISTS stock;


-- ============================================================
-- TABLA CATEGORIAS
-- ============================================================

CREATE TABLE IF NOT EXISTS stock.categorias (
    categoriaid INTEGER GENERATED ALWAYS AS IDENTITY,
    nombre VARCHAR(50) NOT NULL,

    CONSTRAINT pk_categorias
        PRIMARY KEY (categoriaid),

    CONSTRAINT uq_categorias_nombre
        UNIQUE (nombre)
);


-- ============================================================
-- TABLA PRODUCTOS
-- ============================================================

CREATE TABLE IF NOT EXISTS stock.productos (
    productoid INTEGER GENERATED ALWAYS AS IDENTITY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200),
    precio NUMERIC(10,2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    categoriaid INTEGER NOT NULL,

    CONSTRAINT pk_productos
        PRIMARY KEY (productoid),

    CONSTRAINT fk_productos_categorias
        FOREIGN KEY (categoriaid)
        REFERENCES stock.categorias(categoriaid)
);


-- ============================================================
-- LIMPIAR DATOS
-- RESTART IDENTITY reinicia los IDENTITY desde 1
-- ============================================================

TRUNCATE TABLE stock.productos, stock.categorias
RESTART IDENTITY;


-- ============================================================
-- CARGA DE CATEGORIAS
-- ============================================================

INSERT INTO stock.categorias (nombre)
VALUES
    ('Almacén'),
    ('Bebidas'),
    ('Lácteos'),
    ('Limpieza');


-- ============================================================
-- CARGA DE PRODUCTOS
-- ============================================================

INSERT INTO stock.productos
    (nombre, descripcion, precio, stock, categoriaid)
VALUES
    ('Arroz Integral 1kg', 'Arroz integral paquete de 1 kg', 1400.00, 45, 1),
    ('Fideos Tallarín 500g', 'Fideos secos paquete de 500 g', 980.00, 60, 1),
    ('Harina 000 1kg', 'Harina de trigo tipo 000', 850.00, 35, 1),
    ('Aceite de Girasol 1.5L', 'Aceite de girasol botella de 1,5 litros', 3200.00, 25, 1),
    ('Azúcar 1kg', 'Azúcar común paquete de 1 kg', 1200.00, 50, 1),

    ('Agua Mineral 2L', 'Agua mineral sin gas', 900.00, 55, 2),
    ('Gaseosa Cola 2.25L', 'Gaseosa sabor cola', 2800.00, 40, 2),
    ('Jugo de Naranja 1L', 'Jugo de naranja en envase tetra', 1900.00, 28, 2),
    ('Agua Saborizada 1.5L', 'Agua saborizada de pomelo', 1600.00, 32, 2),

    ('Leche Entera 1L', 'Leche entera larga vida', 1300.00, 80, 3),
    ('Yogur Natural 190g', 'Yogur natural entero', 850.00, 42, 3),
    ('Queso Cremoso 500g', 'Queso cremoso en trozo', 4500.00, 18, 3);


-- ============================================================
-- VERIFICACIÓN
-- ============================================================

SELECT *
FROM stock.categorias
ORDER BY nombre;

SELECT *
FROM stock.productos
ORDER BY nombre;