-- Crear la tabla con un identificador único por vendedor.
CREATE TABLE vendedores (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    ventas_totales INTEGER NOT NULL CHECK (ventas_totales >= 0),
    zona TEXT NOT NULL,
    fecha_ingreso TEXT NOT NULL
);

-- Cargar los tres vendedores ficticios de partida.
INSERT INTO vendedores (id, nombre, ventas_totales, zona, fecha_ingreso)
VALUES
    (1, 'Ana Torres', 8200, 'Norte', '2025-01-13'),
    (2, 'Bruno Rojas', 9750, 'Sur', '2025-02-03'),
    (3, 'Carla Medina', 10000, 'Norte', '2025-03-17');

-- Consultar el nombre y las ventas acumuladas de los vendedores del Norte.
SELECT nombre, ventas_totales
FROM vendedores
WHERE zona = 'Norte'
ORDER BY id;
