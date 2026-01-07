# ============================================
# 🔄 COLAB KEEP ALIVE - Chống tự động tắt
# ============================================
# Copy toàn bộ code này vào 1 cell riêng và chạy TRƯỚC khi train
# ============================================

import time
import threading
from IPython.display import display, Javascript, HTML

def setup_keep_alive():
    """
    Setup anti-idle để giữ Colab không tự tắt
    Cần chạy 1 lần trước khi bắt đầu train
    """
    
    # === Method 1: JavaScript Auto-Click ===
    js_code = Javascript('''
    // Anti-idle: Click connect button định kỳ
    function ClickConnect(){
        console.log("[Keep Alive] " + new Date().toLocaleTimeString());
        
        // Click connect button nếu có
        var connectBtn = document.querySelector("colab-connect-button");
        if(connectBtn) connectBtn.click();
        
        // Click vào output area để giả lập hoạt động
        var outputArea = document.querySelector("#output-area");
        if(outputArea) outputArea.click();
        
        // Scroll một chút
        window.scrollBy(0, 1);
        window.scrollBy(0, -1);
    }
    
    // Chạy mỗi 30 giây
    var keepAliveInterval = setInterval(ClickConnect, 30000);
    
    // Thêm indicator
    var indicator = document.createElement('div');
    indicator.id = 'keep-alive-indicator';
    indicator.innerHTML = '🔄 Keep Alive: ACTIVE';
    indicator.style.cssText = 'position:fixed;top:10px;right:10px;background:#4CAF50;color:white;padding:8px 16px;border-radius:20px;font-size:12px;z-index:9999;font-family:Arial;';
    document.body.appendChild(indicator);
    
    console.log("✅ Keep Alive activated - clicking every 30 seconds");
    ''')
    display(js_code)
    
    # === Method 2: Python Thread Keep Alive ===
    def python_keep_alive():
        """Background thread để giữ Python active"""
        while True:
            time.sleep(60)  # Mỗi 60 giây
            # Thao tác nhẹ để giữ kernel active
            _ = 1 + 1
    
    keep_alive_thread = threading.Thread(target=python_keep_alive, daemon=True)
    keep_alive_thread.start()
    
    # === Hiển thị thông tin ===
    display(HTML('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 15px 20px; border-radius: 10px; margin: 10px 0; color: white;">
        <h3 style="margin:0 0 10px 0;">🔄 Colab Keep Alive - ACTIVATED</h3>
        <p style="margin:5px 0;">✅ JavaScript auto-click: Every 30 seconds</p>
        <p style="margin:5px 0;">✅ Python background thread: Active</p>
        <p style="margin:5px 0;">⚠️ Lưu ý: Vẫn cần giữ tab browser mở (có thể minimize)</p>
    </div>
    '''))
    
    print("\n" + "="*50)
    print("🔄 KEEP ALIVE ACTIVATED!")
    print("="*50)
    print("• Auto-click mỗi 30 giây")
    print("• Background thread đang chạy")
    print("• Tab cần giữ mở (minimize OK)")
    print("="*50 + "\n")

# === CHẠY NGAY ===
setup_keep_alive()
