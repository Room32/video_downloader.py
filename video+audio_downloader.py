import os
import tkinter as tk
import re

mp3 = ['-x', 'mp3']
video = '%(ext)s'


def push_btn_video():
    url = ent.get()
    match = re.search(r'https?://(?:[-\w]+\.)+[-\w]+(?:/[-\w./?%&=]*)?', url)

    if match:
        command = fr'yt-dlp "{url}" -o C:\Users\Admin\Desktop\video\#\"%(title)s.{video}"'
        os.system(f'powershell.exe -Command "{command}"')
        done_lbl = tk.Label(text='ГОТОВО!', font=('Calibri', 22, 'bold'), bg='#261d2c', fg='white')
        done_lbl.grid(row=3, column=0, columnspan=2)
    else:
        lbl['text'] = 'Invalid url. Try again:'

def push_btn_audio():
    url = ent.get()
    match = re.search(r'https?://(?:[-\w]+\.)+[-\w]+(?:/[-\w./?%&=]*)?', url)

    if match:
        command = fr'yt-dlp {mp3[0]} "{url}" -o C:\Users\Admin\Desktop\video\#\"%(title)s.{mp3[1]}"'
        os.system(f'powershell.exe -Command "{command}"')
        done_lbl = tk.Label(text='ГОТОВО!', font=('Calibri', 22, 'bold'), bg='#261d2c', fg='white')
        done_lbl.grid(row=3, column=0, columnspan=2)
    else:
        lbl['text'] = 'Invalid url. Try again:'

window = tk.Tk()
window.title('Video Downloader')
window.geometry('445x210+200+200')
window['bg'] = '#261d2c'
window.resizable(width=False, height=False)

ent = tk.Entry(font=('Calibri', 15), width=43)
btn_video = tk.Button(text='Скачать видео', font=('Calibri', 22, 'bold'), bg='#261d2c', fg='white', command=push_btn_video)
btn_audio = tk.Button(text='Скачать аудио', font=('Calibri', 22, 'bold'), bg='#261d2c', fg='white', command=push_btn_audio)

lbl = tk.Label(text='Вставьте ссылку сюда:', font=('Calibri', 22, 'bold'), bg='#261d2c', fg='white')


def show_menu(event):
    ent.focus()
    menu.tk_popup(event.x_root, event.y_root)


menu = tk.Menu(window, tearoff=0)
menu.add_command(label="Вставить", command=lambda: ent.event_generate("<Control-v>"))
ent.bind("<Button-3>", show_menu)

lbl.grid(row=0, column=0, columnspan=2, pady=5)
ent.grid(row=1, column=0, columnspan=2, pady=5, padx=5)
btn_video.grid(row=2, column=1, pady=5)
btn_audio.grid(row=2, column=0, pady=5)

window.mainloop()
