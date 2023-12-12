import sys
import os
import tkinter as tk
import webbrowser

def replace_spaces():
    input_text = input_entry.get("1.0", "end-1c")
    replaced_text = input_text.replace("\xa0", "\x20")
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", replaced_text)

def open_github():
    webbrowser.open("https://github.com/1492949083/EscapeCharReplacer")

# 创建主窗口
root = tk.Tk()
root.title("转义字符替换")

# 窗口大小
h = '800'
w = '600'
root.geometry(h + 'x' + w)
# 居中

root.update_idletasks()

# 创建导航栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="关于", menu=about_menu)
about_menu.add_command(label="GitHub", command=open_github)

# 创建输入框
input_label = tk.Label(root, text="输入文本:")
input_label.grid(row=0, column=0, sticky='w')
input_entry = tk.Text(root)
input_entry.grid(row=1, column=0, sticky='nsew')

# 创建替换按钮
replace_button = tk.Button(root, text="替换", command=replace_spaces)
replace_button.grid(row=2, column=0)

# 创建输出框
output_label = tk.Label(root, text="输出文本:")
output_label.grid(row=3, column=0, sticky='w')
output_entry = tk.Text(root)
output_entry.grid(row=4, column=0, sticky='nsew')

# 配置行和列的权重
root.grid_rowconfigure(1, weight=1)  # 输入框的行权重设置为1
root.grid_rowconfigure(4, weight=1)  # 输出框的行权重设置为1
root.grid_columnconfigure(0, weight=1)  # 列权重设置为1

# 运行主循环
root.mainloop()
