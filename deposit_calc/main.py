import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox as mb

from deposit_calc.calculators import deposit_calc
from utils import IncorrectInput, validate_input


def calculate():
    try:
        rate, duration, credit = validate_input(rate_entry.get(), duration_entry.get(), credit_entry.get())
    except IncorrectInput as e:
        mb.showerror(title="Ошибка ввода", message=str(e))
        return
    for row in table.get_children():
        table.delete(row)
    deposit_calc(table, rate, duration, credit)


win = Tk()

win["bg"] = "#fafafa"
win.title("Депозитный калькулятор")
win.geometry("1920x1080")
win.resizable(False, False)


input_frame = Frame(win, bg=win["bg"])
input_frame.place(relx=0.3, rely=0.02, relwidth=0.4, relheight=0.2)

table_frame = Frame(win, bg="green")
table_frame.place(relx=0.2, rely=0.22, relwidth=0.6, relheight=0.7)

# type_var = IntVar()
# annuity_button = Radiobutton(
#     input_frame,
#     text="Аннуитетный",
#     variable=type_var,
#     value=0,
#     background=win["bg"],
#     relief=GROOVE,
# )
#
# diff_button = Radiobutton(
#     input_frame,
#     text="Дифференцированный",
#     variable=type_var,
#     value=1,
#     background=win["bg"],
#     relief=GROOVE,
# )
# annuity_button.place(relx=0.2, rely=0.1, relwidth=0.3)
# diff_button.place(relx=0.5, rely=0.1, relwidth=0.3)

rate_label = Label(input_frame, text="Процентная ставка", bg=win["bg"])
rate_label.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)

rate_entry = Entry(input_frame, bg=win["bg"])
rate_entry.place(relx=0.35, rely=0.3, relwidth=0.55, relheight=0.1)

duration_label = Label(input_frame, text="Количество месяцев", bg=win["bg"])
duration_label.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.1)

duration_entry = Entry(input_frame, bg=win["bg"])
duration_entry.place(relx=0.35, rely=0.45, relwidth=0.55, relheight=0.1)

credit_label = Label(input_frame, text="Сумма вклада", bg=win["bg"])
credit_label.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.1)

credit_entry = Entry(input_frame, bg=win["bg"])
credit_entry.place(relx=0.35, rely=0.6, relwidth=0.55, relheight=0.1)

calculate_button = Button(input_frame, bg=win["bg"], text="Рассчитать", command=calculate)
calculate_button.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.15)

table = ttk.Treeview(table_frame, show="headings", columns=("month", "payment", "mod"))
table.heading("month", text="Месяц", anchor=CENTER)
table.heading("payment", text="Начисление", anchor=CENTER)
table.heading("mod", text="Баланс", anchor=CENTER)
scrollbar = Scrollbar(table_frame, orient=VERTICAL, command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

table.place(relx=0, rely=0, relwidth=0.985, relheight=1)
scrollbar.place(relx=0.985, rely=0, relwidth=0.015, relheight=1)

table.column("month", anchor=E, width=300)
table.column("payment", anchor=E, width=300)
table.column("mod", anchor=E, width=300)


if __name__ == "__main__":
    win.mainloop()
