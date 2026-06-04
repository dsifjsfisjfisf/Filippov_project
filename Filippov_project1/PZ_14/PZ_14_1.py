import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    message_text = text_message.get("1.0", tk.END).strip()
    subject = var_subject.get()
    
    if not name or not email or not message_text:
        messagebox.showwarning("Error", "Please fill all entries!")
        return
    
    result = f"Name: {name}\nEmail: {email}\nMessage: {message_text}\nSubject: {subject}"
    messagebox.showinfo("Submitted", result)

root = tk.Tk()
root.title("Contact Form")
root.geometry("500x550")
root.configure(bg="#d3d3d3")

main_frame = tk.Frame(root, bg="#d3d3d3")
main_frame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

title = tk.Label(main_frame, text="Contact Form", font=("Helvetica", 24, "bold"), bg="#d3d3d3", fg="#333333")
title.pack(anchor="w", pady=(0, 5))

subtitle = tk.Label(main_frame, text="Please fill all entries.", font=("Helvetica", 10), bg="#d3d3d3", fg="#666666")
subtitle.pack(anchor="w", pady=(0, 30))

frame_name = tk.Frame(main_frame, bg="#d3d3d3")
frame_name.pack(fill=tk.X, pady=(0, 15))
tk.Label(frame_name, text="Name:", font=("Helvetica", 11), bg="#d3d3d3", fg="#333333", width=10, anchor="w").pack(side=tk.LEFT)
entry_name = tk.Entry(frame_name, font=("Helvetica", 11), bg="white", fg="#333333", relief="solid", bd=1)
entry_name.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)

frame_email = tk.Frame(main_frame, bg="#d3d3d3")
frame_email.pack(fill=tk.X, pady=(0, 15))
tk.Label(frame_email, text="Email:", font=("Helvetica", 11), bg="#d3d3d3", fg="#333333", width=10, anchor="w").pack(side=tk.LEFT)
entry_email = tk.Entry(frame_email, font=("Helvetica", 11), bg="white", fg="#333333", relief="solid", bd=1)
entry_email.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)

frame_message = tk.Frame(main_frame, bg="#d3d3d3")
frame_message.pack(fill=tk.X, pady=(0, 15))
tk.Label(frame_message, text="Message:", font=("Helvetica", 11), bg="#d3d3d3", fg="#333333", width=10, anchor="nw").pack(side=tk.LEFT)
text_message = tk.Text(frame_message, font=("Helvetica", 11), bg="white", fg="#333333", relief="solid", bd=1, height=5)
text_message.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)

frame_subject = tk.Frame(main_frame, bg="#d3d3d3")
frame_subject.pack(fill=tk.X, pady=(0, 30))
tk.Label(frame_subject, text="Subject:", font=("Helvetica", 11), bg="#d3d3d3", fg="#333333", width=10, anchor="w").pack(side=tk.LEFT)
var_subject = tk.StringVar(value="Product Inquiry")
subject_options = ["Product Inquiry", "Support", "Feedback", "Other"]
subject_menu = tk.OptionMenu(frame_subject, var_subject, *subject_options)
subject_menu.config(font=("Helvetica", 11), bg="white", fg="#333333", relief="solid", bd=1, width=30)
subject_menu.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3)

btn_send = tk.Button(main_frame, text="Send", font=("Helvetica", 12, "bold"), bg="#a0a0a0", fg="white", relief="flat", cursor="hand2", command=submit_form)
btn_send.pack(anchor="w", pady=(10, 0), ipadx=30, ipady=8)

root.mainloop()
