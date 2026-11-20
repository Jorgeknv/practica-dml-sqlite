-- Dar de alta a dos vendedores. El ID 5 se usa para verificar el borrado.
INSERT INTO vendedores (id, nombre, ventas_totales, zona, fecha_ingreso)
VALUES
    (4, 'Diego Paredes', 11200, 'Sur', '2025-04-07'),
    (5, 'Vendedor de prueba', 0, 'Centro', '2025-04-10');

-- Cargar otros tres vendedores con una sola sentencia (ejercicio opcional).
INSERT INTO vendedores (id, nombre, ventas_totales, zona, fecha_ingreso)
VALUES
    (6, 'Elena Ruiz', 4600, 'Centro', '2025-04-21'),
    (7, 'Felipe Soto', 6900, 'Norte', '2025-05-05'),
    (8, 'Gabriela Vega', 9100, 'Sur', '2025-05-12');

-- Ver el total del vendedor 2 antes de registrar la nueva venta.
SELECT id, nombre, ventas_totales
FROM vendedores
WHERE id = 2;

-- Sumar 500 al total actual del vendedor 2.
UPDATE vendedores
SET ventas_totales = ventas_totales + 500
WHERE id = 2;

-- Identificar a los vendedores que superan el umbral de 10 000.
SELECT id, nombre, ventas_totales
FROM vendedores
WHERE ventas_totales > 10000
ORDER BY id;

-- Pasar a Internacional a los vendedores que superan el umbral.
UPDATE vendedores
SET zona = 'Internacional'
WHERE ventas_totales > 10000;

-- Confirmar el ID y el nombre del registro de prueba antes de eliminarlo.
SELECT id, nombre
FROM vendedores
WHERE id = 5;

-- Eliminar el registro de prueba por su identificador.
DELETE FROM vendedores
WHERE id = 5;

-- Revisar los vendedores que quedaron y sus zonas finales.
SELECT id, nombre, ventas_totales, zona, fecha_ingreso
FROM vendedores
ORDER BY id;

-- Verificar que quedan cero registros con el ID de prueba.
SELECT COUNT(*) AS registros_de_prueba
FROM vendedores
WHERE id = 5;
