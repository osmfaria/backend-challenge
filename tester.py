import ipdb
from django.db import migrations

TRANSACTIONS_DATA = [
    {"description": "Débito", "type": "Entrada"},
    {"description": "Boleto", "type": "Saída"},
    {"description": "Finaciamento", "type": "Saída"},
    {"description": "Crédito", "type": "Entrada"},
    {"description": "Recebimento Empréstimo", "type": "Entrada"},
    {"description": "Vendas", "type": "Entrada"},
    {"description": "Recebimento TED", "type": "Entrada"},
    {"description": "Recebimento DOC", "type": "Entrada"},
    {"description": "Aluguel", "type": "Saída"},
]


def load_transactions_types(apps, schema_editor):

    Transactions_type = apps.get_model('transactions', 'Transactions_type')

    for data in TRANSACTIONS_DATA:
        ipdb.set_trace()
        Transactions_type.objects.create(**data)



class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [migrations.RunPython(load_transactions_types)]
