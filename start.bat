@echo off
title Dota 2 Auto Accept - Startup
chcp 65001 > nul

cd /d "%~dp0"

echo ============================================
echo   Checking and installing libraries...
echo ============================================

:: Checking and installing the necessary modules
py -m pip install --quiet pyautogui pillow keyboard pygetwindow opencv-python

echo.
echo ============================================
echo   All libraries are ready! Program launch....
echo ============================================
echo.

:: We are launching main.py
py main.py

echo.
echo The program has been completed.
pause