@echo off
setlocal

REM 先修改好文件和 .gitignore，然后再执行这个脚本进行推送

REM COMMIT_MESSAGE可以自行修改

echo current path: %~dp0
echo 1. Move to working directory
echo=
D:
cd D:\mybook_ubuk

echo 2. Start submitting code to the local repository
echo=
git add .

echo 3. Commit the changes to the local repository
set now=%date% %time%
set COMMIT_MESSAGE=update some files
echo Time: %now%
git commit -m "%COMMIT_MESSAGE%"
@REM git commit -am "$(date "+%Y-%m-%d %H:%M:%S")"

echo=
echo 4. Push the changes to the remote git server
git push -u origin main --force

endlocal

echo "Batch execution complete!"
pause