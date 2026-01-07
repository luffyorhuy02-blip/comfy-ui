# =====================================================
# 🔄 ADVANCED KEEP ALIVE - Giả lập hoạt động nâng cao
# =====================================================
# Chống Colab tự ngắt bằng nhiều phương pháp kết hợp
# Copy vào cell đầu tiên và chạy trước khi train
# =====================================================

import time
import random
import threading
import subprocess
from IPython.display import display, Javascript, HTML
from google.colab import output

class AdvancedKeepAlive:
    def __init__(self):
        self.running = True
        self.activity_count = 0
        
    def start(self):
        """Khởi động tất cả các phương pháp giữ hoạt động"""
        
        # === 1. JavaScript Activities ===
        self._setup_javascript_activities()
        
        # === 2. Python Background Activities ===
        self._start_python_activities()
        
        # === 3. Shell Activities ===
        self._start_shell_activities()
        
        self._show_status()
        
    def _setup_javascript_activities(self):
        """Giả lập hoạt động người dùng qua JavaScript"""
        display(Javascript('''
        (function() {
            let activityCount = 0;
            
            // Mảng các hoạt động ngẫu nhiên
            const activities = [
                // Click các element khác nhau
                () => document.querySelector("colab-connect-button")?.click(),
                () => document.querySelector("#output-area")?.click(),
                () => document.querySelector(".inputarea")?.click(),
                
                // Scroll ngẫu nhiên
                () => { 
                    const scrollAmount = Math.floor(Math.random() * 50) - 25;
                    window.scrollBy(0, scrollAmount); 
                },
                
                // Di chuyển chuột giả lập
                () => {
                    const event = new MouseEvent('mousemove', {
                        clientX: Math.random() * window.innerWidth,
                        clientY: Math.random() * window.innerHeight
                    });
                    document.dispatchEvent(event);
                },
                
                // Focus/blur
                () => {
                    const cells = document.querySelectorAll('.cell');
                    if(cells.length > 0) {
                        const randomCell = cells[Math.floor(Math.random() * cells.length)];
                        randomCell.focus();
                    }
                },
                
                // Giả lập keyboard activity
                () => {
                    document.dispatchEvent(new KeyboardEvent('keydown', {key: 'Shift'}));
                    document.dispatchEvent(new KeyboardEvent('keyup', {key: 'Shift'}));
                }
            ];
            
            function simulateActivity() {
                activityCount++;
                
                // Chọn 2-3 hoạt động ngẫu nhiên
                const numActivities = 2 + Math.floor(Math.random() * 2);
                for(let i = 0; i < numActivities; i++) {
                    const randomActivity = activities[Math.floor(Math.random() * activities.length)];
                    try { randomActivity(); } catch(e) {}
                }
                
                // Update indicator
                const indicator = document.getElementById('keep-alive-indicator');
                if(indicator) {
                    indicator.innerHTML = '🔄 Keep Alive: ' + activityCount + ' activities';
                }
                
                console.log('[Keep Alive #' + activityCount + '] ' + new Date().toLocaleTimeString());
            }
            
            // Chạy với interval ngẫu nhiên (20-40 giây)
            function scheduleNext() {
                const interval = 20000 + Math.floor(Math.random() * 20000);
                setTimeout(() => {
                    simulateActivity();
                    scheduleNext();
                }, interval);
            }
            
            // Khởi động
            simulateActivity();
            scheduleNext();
            
            // Tạo indicator
            const indicator = document.createElement('div');
            indicator.id = 'keep-alive-indicator';
            indicator.innerHTML = '🔄 Keep Alive: ACTIVE';
            indicator.style.cssText = `
                position: fixed;
                top: 10px;
                right: 10px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                font-size: 13px;
                font-weight: bold;
                z-index: 9999;
                font-family: Arial, sans-serif;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                animation: pulse 2s infinite;
            `;
            document.body.appendChild(indicator);
            
            // Animation
            const style = document.createElement('style');
            style.textContent = `
                @keyframes pulse {
                    0%, 100% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                }
            `;
            document.head.appendChild(style);
            
            console.log("✅ JavaScript Keep Alive ACTIVATED");
        })();
        '''))
    
    def _start_python_activities(self):
        """Các hoạt động Python nền"""
        
        def background_activities():
            """Thread chạy các hoạt động giả lập"""
            import gc
            import sys
            
            while self.running:
                try:
                    # Random delay (30-90 giây)
                    delay = random.randint(30, 90)
                    time.sleep(delay)
                    
                    self.activity_count += 1
                    
                    # Các hoạt động giả lập
                    activities = [
                        lambda: gc.collect(),  # Thu gom rác
                        lambda: len(dir()),    # List attributes
                        lambda: sys.getsizeof([]),  # Kiểm tra memory
                        lambda: time.time(),   # Lấy thời gian
                        lambda: random.random(),  # Tạo số ngẫu nhiên
                        lambda: list(range(100)),  # Tạo list nhỏ
                        lambda: {i: i**2 for i in range(10)},  # Dict comprehension
                    ]
                    
                    # Thực hiện 2-3 hoạt động
                    for _ in range(random.randint(2, 3)):
                        random.choice(activities)()
                    
                except Exception:
                    pass
        
        # Start thread
        thread = threading.Thread(target=background_activities, daemon=True)
        thread.start()
    
    def _start_shell_activities(self):
        """Các lệnh shell định kỳ"""
        
        def shell_activities():
            """Thread chạy lệnh shell nhẹ"""
            commands = [
                'echo "keep alive"',
                'date',
                'pwd',
                'ls > /dev/null',
                'df -h > /dev/null',
                'free -h > /dev/null',
            ]
            
            while self.running:
                try:
                    delay = random.randint(45, 120)
                    time.sleep(delay)
                    
                    # Chạy lệnh ngẫu nhiên (silent)
                    cmd = random.choice(commands)
                    subprocess.run(cmd, shell=True, capture_output=True)
                    
                except Exception:
                    pass
        
        thread = threading.Thread(target=shell_activities, daemon=True)
        thread.start()
    
    def _show_status(self):
        """Hiển thị trạng thái"""
        display(HTML('''
        <div style="
            background: linear-gradient(135deg, #11998e, #38ef7d);
            padding: 20px;
            border-radius: 15px;
            margin: 15px 0;
            color: white;
            font-family: Arial, sans-serif;
        ">
            <h2 style="margin: 0 0 15px 0; font-size: 20px;">
                🔄 Advanced Keep Alive - ACTIVATED
            </h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                    <strong>✅ JavaScript</strong><br>
                    • Click simulation<br>
                    • Mouse movement<br>
                    • Scroll simulation<br>
                    • Keyboard events
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                    <strong>✅ Python</strong><br>
                    • Memory operations<br>
                    • Random computations<br>
                    • Garbage collection
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                    <strong>✅ Shell</strong><br>
                    • System commands<br>
                    • File operations<br>
                    • Resource checks
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                    <strong>⚙️ Settings</strong><br>
                    • Random intervals<br>
                    • Multi-threaded<br>
                    • Auto-recovery
                </div>
            </div>
            <p style="margin: 15px 0 0 0; opacity: 0.9;">
                ⚠️ Vẫn cần giữ tab browser mở (minimize OK)
            </p>
        </div>
        '''))
        
        print("\n" + "="*60)
        print("🔄 ADVANCED KEEP ALIVE - ALL SYSTEMS ACTIVE")
        print("="*60)
        print("✅ JavaScript activities: Random 20-40s intervals")
        print("✅ Python activities: Random 30-90s intervals")
        print("✅ Shell activities: Random 45-120s intervals")
        print("="*60)
        print("💡 Indicator hiển thị góc phải màn hình")
        print("="*60 + "\n")

# === CHẠY NGAY ===
keeper = AdvancedKeepAlive()
keeper.start()
