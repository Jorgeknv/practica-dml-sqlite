from contextlib import closing
from pathlib import Path
import sqlite3


def ejecutar_sql(conexion, archivo):
    """Ejecuta las sentencias del archivo y muestra el resultado de cada consulta."""
    print(f"\n--- {archivo.name} ---")
    sentencia = ""
    for linea in archivo.read_text(encoding="utf-8").splitlines(keepends=True):
        if not sentencia.strip() and linea.lstrip().startswith("--"):
            continue
        sentencia += linea
        if not sqlite3.complete_statement(sentencia):
            continue

        resultado = conexion.execute(sentencia)
        if resultado.description:
            print(f"\n{' '.join(sentencia.split())}")
            print(" | ".join(columna[0] for columna in resultado.description))
            for fila in resultado:
                print(" | ".join(map(str, fila)))
        sentencia = ""

    if sentencia.strip():
        raise ValueError(f"Revisa el punto y coma final en {archivo.name}.")


def main():
    carpeta = Path(__file__).resolve().parent
    base = carpeta / "practica_dml.db"
    try:
        base.touch(exist_ok=False)
    except FileExistsError:
        raise SystemExit(
            "practica_dml.db ya existe. Muévelo o cámbiale el nombre para iniciar otra práctica."
        ) from None

    with closing(sqlite3.connect(base)) as conexion, conexion:
        conexion.execute("BEGIN")
        ejecutar_sql(conexion, carpeta / "01_preparacion.sql")
        ejecutar_sql(conexion, carpeta / "02_operaciones_dml.sql")

    print(f"\nBase de datos guardada en {base}")


if __name__ == "__main__":
    main()
