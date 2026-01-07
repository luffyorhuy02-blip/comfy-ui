@echo off
chcp 65001 >nul
title Git Auto Push

echo ========================================
echo        GIT AUTO PUSH SCRIPT
echo ========================================
echo.

:: Lấy thư mục hiện tại
set "PROJECT_DIR=%cd%"
echo 📁 Project: %PROJECT_DIR%
echo.

:: Kiểm tra Git
git status >nul 2>&1
if errorlevel 1 (
    echo ❌ Thư mục này chưa có Git!
    echo 🔧 Khởi tạo Git...
    git init
)

:: Hiển thị thay đổi
echo 📋 Files đã thay đổi:
echo ----------------------------------------
git status -s
echo ----------------------------------------
echo.

:: Hỏi commit message
set /p COMMIT_MSG="📝 Nhập commit message (Enter = 'Auto update'): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Auto update %date% %time:~0,5%

:: Add và commit
echo.
echo ⏳ Đang commit...
git add .
git commit -m "%COMMIT_MSG%"

:: Push
echo.
echo ⏳ Đang push lên GitHub...
git push

if errorlevel 1 (
    echo.
    echo ⚠️ Push thất bại! Thử force push? (Y/N)
    set /p FORCE="Chọn: "
    if /i "%FORCE%"=="Y" (
        git push --force
    )
)

echo.
echo ========================================
echo ✅ HOÀN THÀNH!
echo ========================================
pause
