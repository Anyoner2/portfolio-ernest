@echo off
REM Run the backend from the correct project root even if you're in the inner folder.
pushd "%~dp0..\..\"
if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
) else (
  python manage.py runserver 127.0.0.1:8000
)
popd
