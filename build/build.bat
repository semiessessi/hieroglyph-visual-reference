@echo off

echo Making sure dependencies exist...
pip install pillow
if errorlevel 1 goto fail

echo Attempting to launch build script...
python ./build/build.py
if errorlevel 1 goto fail

del temp_image

echo Success
goto end

:fail
echo Failed!

:end
echo Completed.