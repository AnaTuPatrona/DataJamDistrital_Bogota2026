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

cd scripts
python 0_normalizacion_limpieza.py

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
echo. Ejecucion finalizada. Puede borrar el directorio ".venv" si desea eliminar el entorno virtual para liberar espacio en disco una vez haya terminado de usar el programa.
@REM echo Eliminando entorno virtual...

@REM call deactivate

@REM cd /d "%~dp0"

@REM rmdir /s /q ".venv"


echo.
echo ==============================
echo Proceso finalizado.
echo ==============================

pause