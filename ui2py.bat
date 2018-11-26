@echo off
for /r ./ %%a in (*.ui) do pyuic %%a -o %%a.py
pause