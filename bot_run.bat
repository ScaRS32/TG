@echo off

call %~dp0bot_run\venv\Scripts\activate

cd %~dp0bot_run

set TOKEN=5462228890:AAE5KcULenChjcvsgazjzJQKtTmdM9QgspM

py bot_telegram.py
pause


