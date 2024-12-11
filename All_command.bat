@echo off

echo Preparando archivo de programacion...
execute
timeout /t 2 /nobreak > nul

:: Agregar todos los archivos
echo Agregando archivos al área de preparación...
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