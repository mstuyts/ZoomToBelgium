@echo off
rem set path=C:\OSGeo4W64\bin;%WINDIR%\system32;%WINDIR%;%WINDIR%\WBem
del /q resources3.py
del /q resources.pyc
pyrcc5 -o resources3.py resources.qrc