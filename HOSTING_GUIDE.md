# 🌐 Hướng Dẫn Deploy Dashboard Lên Hosting

Bạn có thể đưa file `colab_dashboard.html` lên mạng để truy cập từ bất kỳ đâu (điện thoại, máy tính khác) mà không cần file local.

## Cách 1: GitHub Pages (Nhanh nhất & Miễn phí) 🚀

Vì bạn đã có repo GitHub, đây là cách dễ nhất:

1. Vào repo: https://github.com/luffyorhuy02-blip/comfy-ui
2. Vào **Settings** > **Pages** (menu trái).
3. Tại mục **Build and deployment** > **Source**, chọn **Deploy from a branch**.
4. Tại mục **Branch**, chọn `main` và folder `/ (root)`.
5. Bấm **Save**.
6. Đợi 1-2 phút, reload trang. GitHub sẽ hiện link (vd: `https://luffyorhuy02-blip.github.io/comfy-ui/`).
7. Để vào dashboard, thêm `/colab_dashboard.html` vào cuối link.
   - Link sẽ là: `https://luffyorhuy02-blip.github.io/comfy-ui/colab_dashboard.html`

---

## Cách 2: Upload lên Hosting bất kỳ (Vercel / Netlify / Hosting riêng)

Chỉ cần upload đúng 1 file `colab_dashboard.html` (có thể đổi tên thành `index.html` để nso tự chạy trang chủ).

1. Đổi tên `colab_dashboard.html` -> `index.html` (nếu muốn làm trang chủ).
2. Upload lên thư mục `public_html` hoặc `www` của hosting.
3. Truy cập theo tên miền của bạn.

---

## 🔒 Lưu ý cho nhiều tài khoản

Khi bạn gửi link này cho người khác hoặc dùng tài khoản Google khác:
1. Mỗi người tự **Copy Token Cloudflare** của họ.
2. Dán vào ô **"Cloudflare Token Helper"** trên Dashboard.
3. Bấm **Mở trong Colab**.
4. Khi Colab chạy, paste token đó vào (nếu họ chưa setup Secret).

Code Colab đã được thiết kế để chạy độc lập với tài khoản người dùng!
