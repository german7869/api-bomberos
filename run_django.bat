@echo off
cd C:\backenddjango\bq
waitress-serve --port=7002 run_django.bat bq.wsgi:applicationcls

