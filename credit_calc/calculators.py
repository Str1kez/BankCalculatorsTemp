from decimal import Decimal
from tkinter.ttk import Treeview


def decimal_format(n: Decimal) -> Decimal:
    return n.quantize(Decimal("0.01"))


def __calculate_annuity_loan(rate: Decimal, duration: int, credit: Decimal) -> tuple[Decimal, Decimal]:
    percent = rate / 12 / 100
    k = percent * (1 + percent) ** duration / ((1 + percent) ** duration - 1)
    return credit * k, credit * duration * k


def __calculate_diff_loan(
    rate: Decimal, duration: int, credit: Decimal
) -> tuple[list[tuple[int, Decimal, Decimal]], Decimal]:
    percent = rate / 12 / 100
    month_credit_payment = credit / duration
    summary_payments = Decimal(0)
    result_values = []

    for month in range(1, duration + 1):
        if credit > month_credit_payment:
            payment = month_credit_payment + credit * percent
            credit -= month_credit_payment
        else:
            payment = credit + credit * percent
            credit = Decimal(0)
        summary_payments += payment
        result_values.append((month, decimal_format(payment), decimal_format(credit)))

    return result_values, summary_payments


def diff_calc(table: Treeview, rate: Decimal, duration: int, credit: Decimal):
    values, summary_payment = __calculate_diff_loan(rate, duration, credit)
    for row in values:
        table.insert("", "end", text="", values=row)

    summary_values = (
        f"Общая сумма платежа: {decimal_format(summary_payment)}",
        f"Сумма переплаты: {decimal_format(summary_payment - credit)}",
    )
    table.insert("", "end", text="", values=summary_values)


def annuity_calc(table: Treeview, rate: Decimal, duration: int, credit: Decimal):
    month_payment, summary_payment = __calculate_annuity_loan(rate, duration, credit)
    values = (
        f"Ежемесячный платеж: {decimal_format(month_payment)}",
        f"Общая сумма платежа: {decimal_format(summary_payment)}",
        f"Сумма переплаты: {decimal_format(summary_payment - credit)}",
    )
    table.insert("", "end", text="", values=values)
