# Práctica DML en SQLite

Esta práctica simula el mantenimiento de una tabla de vendedores. Usa datos ficticios para consultar las ventas del Norte, registrar vendedores, actualizar sus totales y eliminar un registro de prueba.

## Archivos

- `01_preparacion.sql` crea la tabla `vendedores`, carga tres registros iniciales y consulta los nombres y las ventas de la zona Norte.
- `02_operaciones_dml.sql` registra vendedores nuevos, actualiza sus ventas y zona según las condiciones de la práctica y elimina el registro de prueba. Ambos `UPDATE` y el `DELETE` usan `WHERE`.
- `ejecutar_practica.py` ejecuta los dos scripts en orden con SQLite y muestra el resultado de cada `SELECT`.
- `practica_dml.db` es la base SQLite incluida con el estado final de los datos.
- `evidencia_ejecucion.txt` contiene la salida de una ejecución desde cero.

## Cómo ejecutarlo en VS Code

1. Abre la carpeta del proyecto en VS Code y abre una terminal integrada con **Terminal > Nueva terminal**.
2. Ejecuta el siguiente comando desde esa carpeta. Solo necesitas Python 3, que incluye `sqlite3`.

   ```powershell
   python ejecutar_practica.py
   ```

3. Compara la salida con [evidencia_ejecucion.txt](evidencia_ejecucion.txt). El comando crea una base nueva en `salida/practica_dml.db`. Para repetirlo, mueve o renombra el archivo dentro de `salida/`.

## Resultados esperados

| Operación | Resultado |
| --- | --- |
| Consulta inicial del Norte | Ana Torres (8 200) y Carla Medina (10 000). |
| Dos altas y una inserción masiva de tres | Se agregan los IDs 4 y 5. La inserción opcional agrega los IDs 6, 7 y 8. |
| Suma de 500 al vendedor 2 | Pasa de 9 750 a 10 250. |
| Reasignación de zona | Los IDs 2 y 4 pasan a Internacional. Carla sigue en Norte con exactamente 10 000. |
| Borrado por ID | El ID 5 aparece antes del `DELETE`. El `SELECT` final devuelve `registros_de_prueba = 0` y quedan siete vendedores. |
