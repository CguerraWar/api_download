@echo off

::echo Preparando archivo de programacion...
::"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\python.exe"  "CompactProgrammer\CompactProgrammer\CompactProgrammer.py"
::timeout /t 2 /nobreak > nul

::echo Preparando archivo de programacion...
start "" "%~dp0execute"
timeout /t 2 /nobreak > nul

:: Agregar todos los archivos
echo Agregando archivos al area de preparacion...
git add terralert.json
timeout /t 2 /nobreak > nul

:: Realizar el commit
echo Realizando el commit...
git commit -m "Actualización automática"
timeout /t 5 /nobreak > nul

:: Subir los cambios
echo Subiendo cambios al repositorio remoto...
git push origin main
timeout /t 5 /nobreak > nul

echo Proceso completado.
pause