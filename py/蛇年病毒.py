# 非原创！代码来自@巴布

import tkinter as tk
import random
import time


def create_custom_popup():
	popup = tk.Toplevel(root)
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = random.randint(0, screen_width - 500)
	y = random.randint(0, screen_height - 200)
	# 设置弹窗大小为 500x200
	popup.geometry(f'500x200+{x}+{y}')
	popup.title("新年快乐")
	popup.configure(bg='red')
	label = tk.Label(popup, text="新年快乐", fg='yellow', bg='red', font=('Arial', 20))
	label.pack(pady=20)


def pop_up():
	while True:
		create_custom_popup()
		root.update_idletasks()
		root.update()
		time.sleep(1)


root = tk.Tk()
root.title("弹出窗口演示")
root.withdraw()
pop_up()
root.mainloop()