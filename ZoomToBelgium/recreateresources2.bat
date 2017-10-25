@echo off
set path=C:\OSGeo4W64\bin;%WINDIR%\system32;%WINDIR%;%WINDIR%\WBem
del /q resources.py
del /q resources.pyc
pyrcc4 -o resources.py resources.qrc