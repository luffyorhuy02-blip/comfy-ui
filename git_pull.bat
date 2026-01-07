@echo off
chcp 65001 >nul
title Git Auto Pull

echo ========================================
echo        GIT AUTO PULL (CẬP NHẬT)
echo ========================================
echo.

echo ⏳ Đang kiểm tra và tải code mới từ GitHub...
echo.

git pull origin main

if errorlevel 1 (
    echo.
    echo ❌ Cập nhật thất bại! Có thể do xung đột file.
    echo Hãy dùng 'git_reset.bat' nếu muốn xóa thay đổi local.
) else (
    echo.
    echo ✅ Đã cập nhật thành công!
)

echo.
pause
