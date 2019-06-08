import tkinter as tk
from tkinter import messagebox as msg  # TODO 需单独引入，具体原因待查证
import pickle as pk

# 创建窗口
window = tk.Tk()
window.title('Welcome to ly Python')

# 获取显示屏宽高(分辨率)，设置窗口宽高，保证窗口居中
ws_width, ws_height = window.winfo_screenwidth(), window.winfo_screenheight()
wc_width, wc_height = 450, 300
window.geometry('%dx%d+%d+%d' % (wc_width, wc_height, (ws_width-wc_width)/2, (ws_height-wc_height)/2))

# 创建画布，存放图片
canvas = tk.Canvas(window, height=200, width=450)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 输入框及标题
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
tk.Label(window, text='Account: ').place(x=50, y=150)
tk.Entry(window, textvariable=var_usr_name, width=30).place(x=150, y=150)

var_usr_pwd = tk.StringVar()
tk.Label(window, text='Password: ').place(x=50, y=190)
tk.Entry(window, textvariable=var_usr_pwd, width=30, show='*').place(x=150, y=190)


# 登录事件
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usr_info = pk.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usr_info = {'admin': 'admin'}
            pk.dump(usr_info, usr_file)

    if usr_name in usr_info:
        if usr_pwd == usr_info[usr_name]:
            msg.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            msg.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = msg.askyesno('Welcome', 'You have not sign up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()


# 注册事件
def usr_sign_up():
    def sign_to_ly_python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usr_info.pickle', 'rb') as usr_file:
            exist_usr_info = pk.load(usr_file)
        if np != npf:
            msg.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            msg.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pk.dump(exist_usr_info, usr_file)
            msg.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    # 在window窗口上层再创建一个注册窗口
    window_sign_up = tk.Toplevel(window)
    nwc_width, nwc_height = 450, 300
    window_sign_up.title('Sign up window')
    window_sign_up.geometry('%dx%d+%d+%d' % (nwc_width, nwc_height, (ws_width-nwc_width)/2, (ws_height-nwc_height)/2))

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='Account: ').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)

    tk.Button(window_sign_up, text='Sign up', command=sign_to_ly_python).place(x=150, y=130)


# 登录、注册按钮
tk.Button(window, text='Login', command=usr_login).place(x=170, y=230)
tk.Button(window, text='Sign up', command=usr_sign_up).place(x=270, y=230)

window.mainloop()
