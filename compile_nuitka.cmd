del /f /s /q dist 1>nul
rmdir /s /q dist
mkdir dist

python -m nuitka --follow-imports pysel.py --standalone --show-progress -j 8 --recurse-all --standalone

robocopy pysel.dist dist/files /MOVE /E
robocopy files dist/files /E
robocopy lib dist/lib /E

pause
