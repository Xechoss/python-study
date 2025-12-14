import tkinter as tk
import random
import time
import threading

# 背景颜色列表
BG_COLORS = [
    '#1abc9c', '#f1c40f', '#3498db', '#e74c3c', '#9b59b6', '#f39c12', '#16a085', '#8e44ad', '#f7dc6f', '#2ecc71',
    '#e67e22', '#34495e', '#ecf0f1', '#95a5a6', '#d35400'
]

# 弹窗内容
POPUP_MESSAGES = [
    "💧多喝水哦～", "😊保持微笑呀！", "✨每天都要元气满满", "🍚记得按时吃饭", "🌙早点休息哦～", "❤️保持好心情", "💌我想你了～",
    "🥰今天开心嘛～", "🌈愿所有烦恼都消失～", "🎉开心最重要啦！", "🌟梦想成真～", "⏳慢慢来别急呀～", "🧥天冷了，记得加衣服",
    "🤗期待下次见面！", "😌累了就歇会呀～"
]

# 弹窗弹出间隔时间（秒）
POPUP_INTERVAL = 0.2

# 弹窗大小
POPUP_WIDTH = 250
POPUP_HEIGHT = 60


def create_popup(message, bg_color):
    # 创建顶层窗口作为弹窗
    popup = tk.Toplevel()

    popup.title("温馨提示")

    # 设置弹窗大小和随机位置
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = random.randrange(0, screen_width - POPUP_WIDTH)
    y = random.randrange(0, screen_height - POPUP_HEIGHT)
    popup.geometry(f"{POPUP_WIDTH}x{POPUP_HEIGHT}+{x}+{y}")

    # 设置弹窗总在最前
    popup.attributes("-topmost", True)

    # 设置弹窗本身的背景色
    popup.configure(bg=bg_color)

    # 创建标签并完全填充弹窗
    label = tk.Label(
        popup,
        text=message,
        font=("微软雅黑", 16),
        bg=bg_color
    )

    # 让标签填充整个弹窗空间
    label.pack(expand=True, fill="both", padx=0, pady=0)


def popup_generator():
    while True:
        # 选择弹窗颜色
        bg_color = random.choice(BG_COLORS)
        popup_message = random.choice(POPUP_MESSAGES)

        # 创建弹窗
        # create_popup(popup_message, bg_color)
        root.after(0, create_popup, popup_message, bg_color)

        # 间隔时间
        time.sleep(POPUP_INTERVAL)


if __name__ == "__main__":
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()

    # 启动弹窗线程
    popup_thread = threading.Thread(target=popup_generator, daemon=True)
    popup_thread.start()

    root.mainloop()
