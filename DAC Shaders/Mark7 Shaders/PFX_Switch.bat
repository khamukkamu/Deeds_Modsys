@echo off
SETLOCAL EnableDelayedExpansion

:start
REM Temporary file name to avoid conflicts
SET "TEMP_NAME=postFX_temp.fx"

REM Check if temporary file exists
IF EXIST "%TEMP_NAME%" (
    ECHO Temporary file "%TEMP_NAME%" already exists. Please remove it and try again.
    GOTO :start
)

REM Rename postFX to temporary file name
IF EXIST "postFX.fx" (
    REN "postFX.fx" "%TEMP_NAME%"
)

REM Rename mb2.fx to mb.fx
IF EXIST "postFX2.fx" (
    REN "postFX2.fx" "postFX.fx"
)

REM Rename temporary file to postFX2.fx
IF EXIST "%TEMP_NAME%" (
    REN "%TEMP_NAME%" "postFX2.fx"
)

ECHO Press any key to toggle PostFX the files again...
pause >nul
goto :start

:End
ENDLOCAL