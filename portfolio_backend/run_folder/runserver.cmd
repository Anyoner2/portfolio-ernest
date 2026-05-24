@echo off
REM Run the Django app from a single folder even if the project is nested.
pushd "%~dp0..\"
if exist "..\.venv\Scripts\python.exe" (
  "..\.venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
) else (
  python manage.py runserver 127.0.0.1:8000
)
popd
