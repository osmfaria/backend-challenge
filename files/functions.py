from datetime import datetime
from django.shortcuts import get_object_or_404
from transactions.models import Transaction, Transactions_type
from stores.models import Store


def handle_uploaded_file(file):  

    for line in file:
        decoded_line = line.decode()
        
        trasaction_code_data = decoded_line[0:1]
        date_data = handle_date(decoded_line[1:9])
        amount_data = int(decoded_line[9:19])/100
        cpf_data = handle_cpf(decoded_line[19:30])
        card_data = decoded_line[30:42]
        time_data = handle_time(decoded_line[42:48])
        owner_data = handle_names(decoded_line[48:62])
        store_data = handle_names(decoded_line[62:81])

        transaction_data = {
            "date": handle_datetime(time_data, date_data),
            "amount": amount_data,
            "cpf": cpf_data,
            "card": card_data
        }
        
        handle_create(owner_data, store_data, trasaction_code_data, transaction_data)


def handle_date(date_str):
    date_format = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}"
    return date_format


def handle_cpf(raw_cpf):
    return raw_cpf.lstrip('0')


def handle_time(time_str):
    time_format = f"{time_str[0:2]}:{time_str[2:4]}:{time_str[4:6]}"
    return time_format


def handle_datetime(time_str, date_str):
    datetime_str = f"{date_str} {time_str}"
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def handle_names(raw_name):
    return raw_name.strip()


def handle_create(store_owner, store_name, trasaction_code, transaction_data):
    type = get_object_or_404(Transactions_type, id=trasaction_code)
    store, _ = Store.objects.get_or_create(name=store_name, owner=store_owner)
    Transaction.objects.create(**transaction_data, store=store, type=type)
