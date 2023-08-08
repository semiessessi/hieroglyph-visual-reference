@echo off

echo Keeping PIP up-to-date...
python.exe -m pip install --upgrade pip
if errorlevel 1 goto fail

echo Making sure dependencies exist...
pip install pillow
if errorlevel 1 goto fail

if NOT [%1] == [images] goto skipimages

echo Building cached images...
python ./build/build_image_cache.py
if errorlevel 1 goto fail

del temp_image

:skipimages

echo Building website...
python ./build/build_website.py
if errorlevel 1 goto fail

echo Copying webpage to output location...
copy .\source\index.html .\index.html /y
if errorlevel 1 goto fail

echo [32mSUCCESS[0m
goto end

:fail
echo [31mERROR: Build failed!!![0m

:end
echo [36mCompleted.[0m
