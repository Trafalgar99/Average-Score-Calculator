import tkinter as tk
from tkinter import messagebox
rw = tk.Tk()

# 标题
rw.title("new window")
# 尺寸
rw.geometry("450x600")
rw["background"] = "#66ccff"
rw.attributes("-alpha", 0.5)

text = tk.Label(rw,
                text="这是一个新的窗口",
                bg="yellow",
                fg="red",
                font=('Times', 20, 'bold italic'))

text.pack()

func_res = []


def func():
    msg = tk.Message(rw,
                     text="摩洛哥炒饼",
                     width=60,
                     font=('微软雅黑', 10, 'bold'))
    global func_res
    msg.pack(side="left")
    func_res.append(msg)


def clear(msg):
    msg[-1].pack_forget()
    msg.pop()


button1 = tk.Button(rw, text="关闭", command=func)
button1.pack(side="bottom")
button2 = tk.Button(rw, text="清空", command=lambda: clear(func_res))
k = button2.pack(side="bottom")


callback_res = ""


def callback():
    if messagebox.showwarning("asd", "asddd"):
        rw.destroy()


def check():

    if (e1.get() == "123"):
        messagebox.showinfo("ok")
        return True
    else:
        messagebox.showinfo("no")
        e1.delete(0, tk.END)
        return False


dstr = tk.StringVar()
e1 = tk.Entry(rw, textvariable=dstr,
              validate="focusout", validatecommand=check)
e2 = tk.Entry(rw)
e2.pack(padx=20, pady=20)
e1.pack(padx=20, pady=20)
# e1.insert(0, "password")
# print(e1.get())

rw.protocol("WM_DELETE_WINDOW", callback)
rw.mainloop()
