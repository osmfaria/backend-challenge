def handle_total(transactions):

    total = sum([float(transaction['amount']) if transaction['type']['type'] == 'Entrada' else -float(transaction['amount']) for transaction in transactions])   
    return currency_formater(total)


def currency_formater(amount):
    currency = "R${:,.2f}".format(abs(amount)).replace(",", "X").replace(".", ",").replace("X", ".")
    if(amount < 0):
        return f"-{currency}"
    return currency