# -*- coding: utf-8 -*-
"""
Utilidad compartida para gestionar docs/supuestos.md entre corridas del pipeline.
"""

def truncar_supuestos_para_nueva_corrida(ruta_archivo, marcador="# 5. ENMIENDAS AL PREREGISTRO"):
    """
    Trunca docs/supuestos.md hasta el marcador (inclusive). Las Secciones 1-4
    son fijas y nunca se tocan; la Sección 5 se reconstruye desde cero.
    Llamar UNA SOLA VEZ, al principio del primer notebook de la cadena
    (01_preparacion.ipynb) — nunca en 02/03/04/05.
    """
    with open(ruta_archivo, encoding="utf-8") as f:
        contenido = f.read()

    idx = contenido.find(marcador)
    if idx == -1:
        raise ValueError(f"No se encontró el marcador '{marcador}' en {ruta_archivo}.")

    fin_linea_marcador = contenido.find("\n", idx) + 1
    contenido_truncado = contenido[:fin_linea_marcador]

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(contenido_truncado)

    print(f"docs/supuestos.md truncado. Conservadas Secciones 1-4 "
          f"({fin_linea_marcador} caracteres).")