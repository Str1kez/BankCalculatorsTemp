from decimal import Decimal
from tkinter.ttk import Treeview


def decimal_format(n: Decimal) -> Decimal:
    return n.quantize(Decimal("0.01"))


def __calculate_deposit(rate: Decimal, duration: int, credit: Decimal) -> list[tuple[int, Decimal, Decimal]]:
    percent = rate / 12 / 100
    result_values = []
    for month in range(1, duration + 1):
        income = credit * percent
        credit += income
        result_values.append((month, decimal_format(income), decimal_format(credit)))
    return result_values


def deposit_calc(table: Treeview, rate: Decimal, duration: int, credit: Decimal):
    values = __calculate_deposit(rate, duration, credit)
    for row in values:
        table.insert("", "end", text="", values=row)

    table.insert("", "end", text="", values=("", "", ""))
    summary_values = "", f"Сумма начислений: {decimal_format(values[-1][-1] - credit)}", ""
    table.insert("", "end", text="", values=summary_values)
