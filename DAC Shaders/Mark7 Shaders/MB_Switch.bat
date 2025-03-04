@echo off
SETLOCAL EnableDelayedExpansion

:start
REM Temporary file name to avoid conflicts
SET "TEMP_NAME=mb_temp.fx"

REM Check if temporary file exists
IF EXIST "%TEMP_NAME%" (
    ECHO Temporary file "%TEMP_NAME%" already exists. Please remove it and try again.
    GOTO :start
)

REM Rename mb.fx to temporary file name
IF EXIST "mb.fx" (
    REN "mb.fx" "%TEMP_NAME%"
)

REM Rename mb2.fx to mb.fx
IF EXIST "mb2.fx" (
    REN "mb2.fx" "mb.fx"
)

REM Rename temporary file to mb2.fx
IF EXIST "%TEMP_NAME%" (
    REN "%TEMP_NAME%" "mb2.fx"
)

ECHO Press any key to toggle MB.FX the files again...
pause >nul
goto :start

:End
ENDLOCAL
