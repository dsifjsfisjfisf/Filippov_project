import tkinter as tk
from tkinter import filedialog, messagebox

def create_label(parent, text, font, bg, fg, anchor, pady):
    label = tk.Label(parent, text=text, font=font, bg=bg, fg=fg)
    label.pack(anchor=anchor, pady=pady)
    return label

def create_entry(parent, label_text, is_multiline=False):
    frame = tk.Frame(parent, bg="#f0f0f0")
    frame.pack(fill=tk.X, pady=(0, 10))
    tk.Label(frame, text=label_text, font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
    if is_multiline:
        entry = tk.Text(frame, font=("Arial", 10), height=5, width=40)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    else:
        entry = tk.Entry(frame, font=("Arial", 10), width=40)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    return entry

def create_file_row(parent, row_num):
    frame = tk.Frame(parent, bg="#f0f0f0")
    frame.pack(fill=tk.X, pady=(0, 5))
    tk.Label(frame, text=f"Прикрепить файл:", font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
    file_path_var = tk.StringVar()
    file_path_var.set("Файл не выбран")
    path_label = tk.Label(frame, textvariable=file_path_var, font=("Arial", 9), bg="#f0f0f0", fg="gray", width=30, anchor="w")
    path_label.pack(side=tk.LEFT, padx=(0, 10))
    
    def browse_file():
        filename = filedialog.askopenfilename()
        if filename:
            file_path_var.set(filename)
    
    btn = tk.Button(frame, text="Обзор...", font=("Arial", 9), command=browse_file)
    btn.pack(side=tk.LEFT)
    return file_path_var

def create_button(parent, text, bg, command):
    btn = tk.Button(parent, text=text, font=("Arial", 10, "bold"), bg=bg, fg="white", padx=20, pady=5, command=command)
    btn.pack(side=tk.LEFT, padx=(0, 10))
    return btn

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    subject = entry_subject.get()
    message = text_message.get("1.0", tk.END).strip()
    
    if not name or not email or not subject or not message:
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
        return
    
    files = [v.get() for v in file_paths if v.get() != "Файл не выбран"]
    result = f"Имя: {name}\nEmail: {email}\nТема: {subject}\nСообщение: {message}\nФайлы: {', '.join(files) if files else 'Нет'}"
    messagebox.showinfo("Отправлено", result)

def cancel_form():
    name = entry_name.get()
    if name:
        messagebox.showinfo("Отчисление", f"Студент {name} успешно отчислен!")
    else:
        messagebox.showinfo("Отчисление", "Студент успешно отчислен!")
    
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    text_message.delete("1.0", tk.END)
    for v in file_paths:
        v.set("Файл не выбран")

root = tk.Tk()
root.title("Форма заявки")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

create_label(main_frame, "Форма заявки", ("Arial", 18, "bold"), "#f0f0f0", "#333333", "w", (0, 10))

info_text = """Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml
Макс. размер каждого файла: 1024kb. Макс. общий размер файла: 2048kb."""
create_label(main_frame, info_text, ("Arial", 9), "#f0f0f0", "#666666", "w", (0, 15))

entry_name = create_entry(main_frame, "Ваше имя:")
entry_email = create_entry(main_frame, "Ваш Email:")
entry_subject = create_entry(main_frame, "Тема письма:")

file_paths = []
for i in range(3):
    file_paths.append(create_file_row(main_frame, i+1))

create_label(main_frame, "Ваше сообщение:", ("Arial", 10, "bold"), "#f0f0f0", "#333333", "w", (10, 5))
text_message = create_entry(main_frame, "", is_multiline=True)

button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.pack(pady=(20, 0), anchor="w")

create_button(button_frame, "Отправить Email", "#4CAF50", submit_form)
create_button(button_frame, "Отчислить", "#f44336", cancel_form)

root.mainloop()
