#ESTE SCRIPT ES EL ÚNICO QUE SE EJECUTA, YA QUE LLAMA AL RESTO DE SCRIPTS DE LA CARPETA.

#Ejecuta secuencialmente todos los archivos .py y .ipynb de una carpeta,
#excluyendo el script actual.
# Args:
    # directorio: Ruta de la carpeta. Si es None, usa el directorio donde se encuentra este script.
    # detener_en_error: Si True, se detiene al primer fallo. Si False, continúa con los demás.

#si algo no funciona, ejecutar este en consola una vez instalado los requerimientos: python -m ipykernel install --user --name python3

import subprocess
import sys
from pathlib import Path
import importlib.util

def check_ipykernel():
    """Verifica si ipykernel está instalado."""
    return importlib.util.find_spec("ipykernel") is not None

def ejecutar_scripts_de_carpeta(directorio=None, detener_en_error=False, incluir_notebooks=True):
    if directorio is None:
        directorio = Path(__file__).parent
    else:
        directorio = Path(directorio)

    # --- Scripts Python ---
    scripts = sorted(directorio.glob("*.py"))
    script_actual = Path(__file__).resolve()
    scripts = [s for s in scripts if s.resolve() != script_actual]

    # --- Notebooks ---
    notebooks = []
    if incluir_notebooks:
        notebooks = sorted(directorio.glob("*.ipynb"))

    total = len(scripts) + len(notebooks)
    if total == 0:
        print("No se encontraron archivos .py ni .ipynb para ejecutar.")
        return

    print(f"Se ejecutarán {len(scripts)} scripts .py y {len(notebooks)} notebooks .ipynb.")
    if scripts:
        print("Scripts .py:")
        for s in scripts:
            print(f"  - {s.name}")
    if notebooks:
        print("Notebooks .ipynb:")
        for nb in notebooks:
            print(f"  - {nb.name}")
    print("\n" + "="*50 + "\n")

    # 1) Ejecutar scripts Python
    for script in scripts:
        print(f"--- Ejecutando script: {script.name} ---")
        try:
            resultado = subprocess.run(
                [sys.executable, str(script)],
                capture_output=True,
                text=True,
                check=False
            )
            if resultado.stdout:
                print(resultado.stdout, end="")
            if resultado.stderr:
                print("Errores:", resultado.stderr, end="")
            if resultado.returncode != 0:
                print(f"{script.name} terminó con código de error {resultado.returncode}")
                if detener_en_error:
                    print("Deteniendo ejecución por error.")
                    return
            else:
                print(f"{script.name} ejecutado correctamente.")
        except Exception as e:
            print(f"Error al intentar ejecutar {script.name}: {e}")
            if detener_en_error:
                return
        print("\n" + "-"*50 + "\n")

    # 2) Ejecutar notebooks
    if notebooks:
        # Verificar si ipykernel está instalado
        if not check_ipykernel():
            print("No se encontró 'ipykernel'. Para ejecutar notebooks necesitas instalarlo:")
            print("   pip install ipykernel")
            print("   python -m ipykernel install --user --name python3")
            if detener_en_error:
                print("Deteniendo ejecución por error.")
                return
            else:
                print("Omitiendo ejecución de notebooks.\n")
                return

        for notebook in notebooks:
            print(f"--- Ejecutando notebook: {notebook.name} ---")
            try:
                comando = [
                    sys.executable, "-m", "jupyter", "nbconvert",
                    "--to", "notebook",
                    "--execute",
                    "--inplace",
                    "--ExecutePreprocessor.kernel_name=python3",  # Aseguramos kernel python3
                    str(notebook)
                ]
                resultado = subprocess.run(
                    comando,
                    capture_output=True,
                    text=True,
                    check=False
                )

                if resultado.stdout:
                    print(resultado.stdout, end="")
                if resultado.stderr:
                    print("Errores:", resultado.stderr, end="")

                if resultado.returncode != 0:
                    print(f"{notebook.name} terminó con error (código {resultado.returncode})")
                    # Si el error es por kernel no encontrado, mostrar ayuda
                    if "No such kernel" in (resultado.stderr or ""):
                        print("   Posible causa: kernel 'python3' no registrado.")
                        print("   Solución: instala ipykernel y registra el kernel:")
                        print("   pip install ipykernel")
                        print("   python -m ipykernel install --user --name python3")
                    if detener_en_error:
                        print("Deteniendo ejecución por error.")
                        return
                else:
                    print(f"{notebook.name} ejecutado correctamente. Revisa el archivo para ver los resultados.")
            except Exception as e:
                print(f"Error al intentar ejecutar {notebook.name}: {e}")
                if detener_en_error:
                    return
            print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    ejecutar_scripts_de_carpeta(detener_en_error=False)