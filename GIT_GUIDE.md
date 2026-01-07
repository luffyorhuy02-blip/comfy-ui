# 📚 Hướng Dẫn Git CMD

## 🔧 Cài đặt ban đầu

```bash
# Cấu hình tên và email
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

---

## 🚀 Tạo mới và push lên GitHub

```bash
# 1. Di chuyển vào thư mục project
cd C:\path\to\your\project

# 2. Khởi tạo Git
git init

# 3. Thêm tất cả files
git add .

# 4. Commit lần đầu
git commit -m "Initial commit"

# 5. Kết nối với GitHub (tạo repo trên github.com/new trước)
git remote add origin https://github.com/USERNAME/REPO.git

# 6. Đổi tên branch thành main
git branch -M main

# 7. Push lên GitHub
git push -u origin main
```

---

## �️ Công Cụ Tự Động (Scripts)

Đã có sẵn các script để giúp bạn thao tác nhanh hơn:

| File | Chức năng | Cách dùng |
|------|-----------|-----------|
| **`git_push.bat`** | Update code lên GitHub | Chạy file, nhập message |
| **`git_pull.bat`** | Tải code mới về máy | Chạy file |
| **`git_release.bat`** | Tạo phiên bản mới | Chạy file, nhập version (vd v1.0) |
| **`git_reset.bat`** | ⚠️ Hủy thay đổi, quay về gốc | Chạy file (Cẩn thận!) |
| **`colab_dashboard.html`** | Bảng điều khiển Notebooks | Mở bằng trình duyệt để vào nhanh Colab |


---

## �📦 Cập nhật code (sau khi đã setup)

```bash
# 1. Xem files đã thay đổi
git status

# 2. Thêm files đã sửa
git add .

# 3. Commit với message
git commit -m "Mô tả thay đổi"

# 4. Push lên GitHub
git push
```

---

## 🏷️ Tạo Version Tags

```bash
# Tạo tag phiên bản
git tag v1.0.0

# Push tag lên GitHub
git push origin v1.0.0

# Xem tất cả tags
git tag -l
```

---

## 🔄 Các lệnh thường dùng

| Lệnh | Mô tả |
|------|-------|
| `git status` | Xem trạng thái files |
| `git add .` | Thêm tất cả files |
| `git add file.txt` | Thêm 1 file cụ thể |
| `git commit -m "msg"` | Commit với message |
| `git push` | Push lên remote |
| `git pull` | Kéo code mới từ remote |
| `git log` | Xem lịch sử commit |
| `git diff` | Xem thay đổi |

---

## ⚠️ Ghi đè code trên GitHub

```bash
# Force push (cẩn thận!)
git push --force
```

---

## 🔐 Nếu bị hỏi đăng nhập

1. Tạo Personal Access Token: https://github.com/settings/tokens
2. Chọn "Generate new token (classic)"
3. Check ✅ `repo`
4. Copy token, dùng thay password

---

## 📁 Tạo file .gitignore

```bash
# Tạo file .gitignore để bỏ qua files không cần
echo "*.log" > .gitignore
echo "node_modules/" >> .gitignore
echo "__pycache__/" >> .gitignore
```
