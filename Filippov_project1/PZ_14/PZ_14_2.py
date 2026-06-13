import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    if not name or not email or not age:
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните обязательные поля (Имя, Email, Возраст)")
        return
    
    gender = var_gender.get()
    qualities = text_qualities.get("1.0", tk.END).strip()
    
    selected_animals = []
    for animal, var in animals_vars.items():
        if var.get():
            selected_animals.append(animal)
    
    result = f"Имя: {name}\nEmail: {email}\nВозраст: {age}\nПол: {gender}\nКачества: {qualities}\nЖивотные: {', '.join(selected_animals) if selected_animals else 'Нет'}"
    messagebox.showinfo("Заявка отправлена", result)

root = tk.Tk()
root.title("Форма заявки в зоопарк")
root.geometry("500x650")
root.configure(bg="#f0f0f0")

main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

title = tk.Label(main_frame, text="Форма заявки на работу в зоопарке", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
title.pack(pady=(0, 5))

subtitle = tk.Label(main_frame, text="Пожалуйста, заполните форму. Обязательные поля помечены *", font=("Arial", 9), bg="#f0f0f0", fg="#666666")
subtitle.pack(pady=(0, 20))

section1 = tk.Label(main_frame, text="Контактная информация", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333", anchor="w")
section1.pack(fill=tk.X, pady=(0, 10))

frame_name = tk.Frame(main_frame, bg="#f0f0f0")
frame_name.pack(fill=tk.X, pady=(0, 5))
tk.Label(frame_name, text="Имя *", font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
entry_name = tk.Entry(frame_name, font=("Arial", 10), width=30)
entry_name.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_phone = tk.Frame(main_frame, bg="#f0f0f0")
frame_phone.pack(fill=tk.X, pady=(0, 5))
tk.Label(frame_phone, text="Телефон", font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
entry_phone = tk.Entry(frame_phone, font=("Arial", 10), width=30)
entry_phone.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_email = tk.Frame(main_frame, bg="#f0f0f0")
frame_email.pack(fill=tk.X, pady=(0, 15))
tk.Label(frame_email, text="Email *", font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
entry_email = tk.Entry(frame_email, font=("Arial", 10), width=30)
entry_email.pack(side=tk.LEFT, fill=tk.X, expand=True)

section2 = tk.Label(main_frame, text="Персональная информация", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333", anchor="w")
section2.pack(fill=tk.X, pady=(0, 10))

frame_age = tk.Frame(main_frame, bg="#f0f0f0")
frame_age.pack(fill=tk.X, pady=(0, 5))
tk.Label(frame_age, text="Возраст *", font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
entry_age = tk.Entry(frame_age, font=("Arial", 10), width=30)
entry_age.pack(side=tk.LEFT, fill=tk.X, expand=True)

frame_gender = tk.Frame(main_frame, bg="#f0f0f0")
frame_gender.pack(fill=tk.X, pady=(0, 5))
tk.Label(frame_gender, text="Пол", font=("Arial", 10), bg="#f0f0f0", width=15, anchor="w").pack(side=tk.LEFT)
var_gender = tk.StringVar(value="Женщина")
gender_frame = tk.Frame(frame_gender, bg="#f0f0f0")
gender_frame.pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Мужчина", variable=var_gender, value="Мужчина", bg="#f0f0f0").pack(side=tk.LEFT, padx=(0, 10))
tk.Radiobutton(gender_frame, text="Женщина", variable=var_gender, value="Женщина", bg="#f0f0f0").pack(side=tk.LEFT)

frame_qualities = tk.Frame(main_frame, bg="#f0f0f0")
frame_qualities.pack(fill=tk.X, pady=(10, 5))
tk.Label(frame_qualities, text="Перечислите личные качества", font=("Arial", 10), bg="#f0f0f0", width=20, anchor="w").pack(anchor="w")
text_qualities = tk.Text(frame_qualities, font=("Arial", 10), height=4, width=40)
text_qualities.pack(fill=tk.X, pady=(5, 0))

section3 = tk.Label(main_frame, text="Выберите ваших любимых животных", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333", anchor="w")
section3.pack(fill=tk.X, pady=(15, 10))

animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
animals_vars = {}
animals_frame = tk.Frame(main_frame, bg="#f0f0f0")
animals_frame.pack(fill=tk.X, pady=(0, 15))

left_frame = tk.Frame(animals_frame, bg="#f0f0f0")
left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
right_frame = tk.Frame(animals_frame, bg="#f0f0f0")
right_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True)

for i, animal in enumerate(animals):
    var = tk.BooleanVar()
    animals_vars[animal] = var
    if i < 4:
        tk.Checkbutton(left_frame, text=animal, variable=var, bg="#f0f0f0", anchor="w").pack(fill=tk.X)
    else:
        tk.Checkbutton(right_frame, text=animal, variable=var, bg="#f0f0f0", anchor="w").pack(fill=tk.X)

btn_submit = tk.Button(main_frame, text="Отправить информацию", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", padx=20, pady=8, command=submit_form)
btn_submit.pack(pady=(10, 0))

root.mainloop()
