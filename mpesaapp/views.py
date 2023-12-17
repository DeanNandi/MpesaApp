from django.shortcuts import render
from .genrateAcesstoken import get_access_token
from .stkPush import initiate_stk_push
from .query import query_stk_status
from .callback import process_stk_callback
from .models import Transaction


def display_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'display_transactions.html', {'transactions': transactions})


