@echo off
chcp 65001 >nul
title Git Version Release

echo ========================================
echo       GIT VERSION RELEASE
echo ========================================
echo.

:: Hiển thị tags hiện có
echo 🏷️ Các phiên bản hiện tại:
git tag -l
echo.

:: Hỏi version mới
set /p VERSION="📦 Nhập phiên bản mới (vd: v1.0.0): "
if "%VERSION%"=="" (
    echo ❌ Chưa nhập phiên bản!
    pause
    exit
)

:: Hỏi mô tả
set /p DESC="📝 Mô tả phiên bản: "
if "%DESC%"=="" set DESC=Release %VERSION%

:: Commit changes
echo.
echo ⏳ Đang commit...
git add .
git commit -m "%DESC%"

:: Tạo tag
echo.
echo ⏳ Tạo tag %VERSION%...
git tag -a %VERSION% -m "%DESC%"

:: Push
echo.
echo ⏳ Đang push...
git push origin main
git push origin %VERSION%

echo.
echo ========================================
echo ✅ ĐÃ TẠO PHIÊN BẢN: %VERSION%
echo ========================================
echo.
echo 🔗 Vào GitHub > Releases để tạo release note
pause
