@echo off

echo Making sure dependencies exist...
pip install pillow
if errorlevel 1 goto fail

echo Attempting to launch build script...
python ./build/build.py
if errorlevel 1 goto fail

echo Copying webpage to output location...
copy .\source\index.html .\index.html /y
if errorlevel 1 goto fail

del temp_image

echo [32mSUCCESS[0m
goto end

:fail
echo [31mERROR: Build failed!!![0m

:end
echo [36mCompleted.[0m