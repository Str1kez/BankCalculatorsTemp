from decimal import Decimal, InvalidOperation

from utils.exception import IncorrectInput


def validate_input(rate: str, duration: str, credit: str) -> tuple[Decimal, int, Decimal]:
    try:
        parsed_rate = Decimal(rate)
    except InvalidOperation:
        raise IncorrectInput("Неверный тип данных для ставки")
    try:
        parsed_duration = int(duration)
    except ValueError:
        raise IncorrectInput("Неверный тип данных для количества месяцев")
    try:
        parsed_credit = Decimal(credit)
    except InvalidOperation:
        raise IncorrectInput("Неверный тип данных для суммы кредита")

    if parsed_rate <= 0 or parsed_duration <= 0 or parsed_credit <= 0:
        raise IncorrectInput("Ставка, срок, сумма кредита должны быть больше 0")

    if "." in rate:
        _, mod = rate.split(".")
        if len(mod) > 2:
            raise IncorrectInput("Процентная ставка должна быть вида: Y.XX")

    return parsed_rate, parsed_duration, parsed_credit
