@echo off
setlocal

cd /d "%~dp0"

echo ==============================
echo DataJam ETL Pipeline
echo ==============================

if not exist ".venv" (
    echo Creando entorno virtual...
    python -m venv .venv

    echo Instalando dependencias...
    call .venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    echo Activando entorno virtual...
    call .venv\Scripts\activate.bat
)

echo.
echo ==============================
echo Ejecutando pipeline...
echo ==============================

python scripts\0_normalizacion_limpieza.py

set EXIT_CODE=%ERRORLEVEL%

echo.
echo ==============================

if %EXIT_CODE% EQU 0 (
    echo Pipeline terminado correctamente.
) else (
    echo Pipeline terminado con errores.
)

echo ==============================


echo.
echo Eliminando entorno virtual...

call deactivate

cd /d "%~dp0"

rmdir /s /q ".venv"


echo.
echo ==============================
echo Proceso finalizado.
echo ==============================

pause