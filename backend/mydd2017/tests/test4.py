from mannirpy import remita
import time



rem =  remita.Remita('demo')

#print(rem.status('260007628900'))

payment = {
    'payerName': 'Test User',
    'payerPhone': '08000000001',
    'payerEmail': 'test@example.com',
    'paymenttype': 'BANK_BRANCH',
    'orderId': '',
    'serviceTypeId': '4430731',
    'amount': 2000,
    'serviceCharge': 1000,
    'order_id': int(time.time()),
}

print(rem.split(payment))
