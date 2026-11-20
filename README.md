# Práctica DML en SQLite

Esta práctica simula el mantenimiento de una tabla de vendedores. Usa datos ficticios para consultar las ventas del Norte, registrar vendedores, actualizar sus totales y eliminar un registro de prueba.

## Archivos

- `01_preparacion.sql` crea la tabla `vendedores`, carga tres registros iniciales y consulta los nombres y las ventas de la zona Norte.
- `02_operaciones_dml.sql` registra dos vendedores y añade tres más en una inserción masiva. Actualiza las ventas del vendedor 2, reasigna la zona de quienes superan las 10 000 unidades y verifica el borrado del vendedor de prueba.
- `ejecutar_practica.py` crea `practica_dml.db`, ejecuta los dos archivos SQL en orden y muestra cada `SELECT` en la terminal.

## Cómo ejecutarlo en VS Code

1. Abre la carpeta del proyecto en VS Code y abre una terminal integrada con **Terminal > Nueva terminal**.
2. Ejecuta el siguiente comando desde esa carpeta. Solo necesitas Python 3, que incluye `sqlite3`.

   ```powershell
   python ejecutar_practica.py
   ```

3. Revisa los resultados en la terminal. `practica_dml.db` se guarda junto a los scripts. Si quieres repetir la práctica desde cero, mueve o renombra ese archivo antes de ejecutar el comando otra vez.

## Resultados esperados

- La consulta inicial del Norte devuelve a Ana Torres (8 200) y Carla Medina (10 000).
- Las ventas del vendedor 2 pasan de 9 750 a 10 250.
- Los vendedores 2 y 4 quedan en la zona Internacional. Carla se queda en el Norte con exactamente 10 000.
- El resultado final contiene siete vendedores y `registros_de_prueba` devuelve `0`.
