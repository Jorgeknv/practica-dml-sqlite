from contextlib import closing
from pathlib import Path
import sqlite3


def ejecutar_sql(conexion, archivo):
    """Ejecuta las sentencias y muestra las consultas y las filas modificadas."""
    print(f"\n--- {archivo.name} ---")
    sentencia = ""
    for linea in archivo.read_text(encoding="utf-8").splitlines(keepends=True):
        if not sentencia.strip() and linea.lstrip().startswith("--"):
            continue
        sentencia += linea
        if not sqlite3.complete_statement(sentencia):
            continue

        print(f"\n{' '.join(sentencia.split())}")
        resultado = conexion.execute(sentencia)
        if resultado.description:
            print(" | ".join(columna[0] for columna in resultado.description))
            for fila in resultado:
                print(" | ".join(map(str, fila)))
        elif resultado.rowcount >= 0:
            print(f"Filas afectadas: {resultado.rowcount}")
        sentencia = ""

    if sentencia.strip():
        raise ValueError(f"Revisa el punto y coma final en {archivo.name}.")


def main():
    carpeta = Path(__file__).resolve().parent
    salida = carpeta / "salida"
    salida.mkdir(exist_ok=True)
    base = salida / "practica_dml.db"
    try:
        base.touch(exist_ok=False)
    except FileExistsError:
        raise SystemExit(
            "salida/practica_dml.db ya existe. Mueve o renombra ese archivo para repetir la práctica."
        ) from None

    with closing(sqlite3.connect(base)) as conexion, conexion:
        conexion.execute("BEGIN")
        ejecutar_sql(conexion, carpeta / "01_preparacion.sql")
        ejecutar_sql(conexion, carpeta / "02_operaciones_dml.sql")

    print(f"\nBase de datos guardada en {base.relative_to(carpeta).as_posix()}")


if __name__ == "__main__":
    main()
