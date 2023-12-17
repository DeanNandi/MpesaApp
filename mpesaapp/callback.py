import json
from django.http import JsonResponse
from .models import Transaction  # The Transaction model


def process_stk_callback(request):
    stk_callback_response = json.loads(request.body)
    log_file = "Mpesastkresponse.json"
    with open(log_file, "a") as log:
        json.dump(stk_callback_response, log)

    merchant_request_id = stk_callback_response['Body']['stkCallback']['MerchantRequestID']
    checkout_request_id = stk_callback_response['Body']['stkCallback']['CheckoutRequestID']
    result_code = stk_callback_response['Body']['stkCallback']['ResultCode']
    result_desc = stk_callback_response['Body']['stkCallback']['ResultDesc']
    amount = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
    transaction_id = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
    user_phone_number = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

    if result_code == 0:
        # Store the transactions in the database
        transaction = Transaction.objects.create(
            merchant_request_id=merchant_request_id,
            checkout_request_id=checkout_request_id,
            result_code=result_code,
            result_desc=result_desc,
            amount=amount,
            transaction_id=transaction_id,
            user_phone_number=user_phone_number
        )
        transaction.save()

        # Optionally, you can return a JsonResponse to acknowledge the successful processing of the callback
        return JsonResponse({'status': 'success'})
    else:
        # Handle other result codes if needed
        return JsonResponse({'status': 'failure', 'message': 'Transaction failed'})

# Note: Make sure to replace '.models' with the actual location of your models module
