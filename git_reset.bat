@echo off
chcp 65001 >nul
title Git Hard Reset

echo ========================================
echo        GIT HARD RESET (KHÔI PHỤC)
echo ========================================
echo.
echo ⚠️  CẢNH BÁO NGUY HIỂM!
echo.
echo Lệnh này sẽ:
echo 1. XÓA SẠCH mọi thay đổi bạn chưa push
echo 2. Quay về trạng thái giống y hệt trên GitHub
echo.
echo Dùng khi: Code bị lỗi nặng, muốn tải lại từ đầu.
echo.

set /p CONFIRM="🔴 Bạn có chắc chắn muốn RESET không? (Y/N): "
if /i "%CONFIRM%"=="Y" (
    echo.
    echo ⏳ Đang reset...
    git fetch origin
    git reset --hard origin/main
    echo.
    echo ✅ Đã khôi phục về trạng thái sạch!
) else (
    echo.
    echo ❌ Đã hủy thao tác.
)

echo.
pause
