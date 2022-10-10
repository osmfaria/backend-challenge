from django.shortcuts import render
from stores.models import Store
from .functions import handle_total
from transactions.models import Transaction
from .serializer import TransactionSerializer


def retrieve_transactions(request, store_name):

    store = Store.objects.get(name=store_name)
    transactions_list = Transaction.objects.filter(store=store)
    serializer = TransactionSerializer(transactions_list, many=True)

    total = handle_total(serializer.data)

    return render(
        request,
        "transactions/transactions.html",
        {"transactions_list": serializer.data, "store": store, "total": total},
    )


def search_stores(request):

    if request.method == "POST":
        searched_business = request.POST['searched-business']
        stores = Store.objects.filter(name__icontains=searched_business)
        return render(request, "transactions/search_stores.html", {'stores': stores})
    
    return render(request, "transactions/search_stores.html", {})