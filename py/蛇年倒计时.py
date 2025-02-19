import tkinter as tk
import datetime

# 创建主窗口
root = tk.Tk()
root.title("蛇年倒计时")
root.geometry("400x200")  # 设置窗口大小

# 定义目标日期
target_date = datetime.datetime(2037, 1, 29)


# 更新倒计时的函数
def update_countdown():
    now = datetime.datetime.now()
    remaining_time = target_date - now

    if remaining_time.total_seconds() < 0:
        label.config(text="2037年蛇年已经到来！祝你蛇年大吉，万事如意！")
    else:
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        label.config(text=f"2025年蛇年已经到来！\n祝你蛇年大吉，越蛇越多！\n\n距离2037年蛇年还有：\n{days}天 {hours}小时 {minutes}分钟 {seconds}秒")

    # 每秒更新一次
    root.after(1000, update_countdown)


# 创建一个标签来显示倒计时
label = tk.Label(root, text="", font=("Arial", 16), fg="red")
label.pack(pady=10)  # 设置标签的位置和边距

# 启动倒计时更新
update_countdown()

# 启动主循环
root.mainloop()
