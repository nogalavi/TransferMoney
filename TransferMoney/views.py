from django.shortcuts import render
from django.http import HttpResponse
from TransferMoney.client import User


def index(request):
    return HttpResponse("Hello, world")


def get_offer(request):
    # TODO print to log

    user_id = request.GET["user_id"]
    amount = int(request.GET["amount"])
    destination_bank_name = request.GET["destination_bank_name"]
    destination_bank_number = request.GET["destination_bank_number"]

    response = HttpResponse("Done")
    response["is_offer_valid"] = False

    offer_id = 1  # TODO insert here a really good hash function
    user = User(user_id)  # This class will read from client info from DB

    try:
        user_has_amount = does_user_have_amount(user)

        if not user_has_amount:
            print("ERROR %s user doesn't have enough money to transfer" % user_id)
            return response

        print("DEBUG %s user has enough money to transfer" % user_id)

        bitcoins_amount = currency_to_bitcoin(amount)  # Shekels to Bitcoin
        offer = bitcoin_to_destination(bitcoins_amount, destination_bank_name,
                                       destination_bank_number)  # Bitcoin to Dollar, and move dollar to destination account

    except Exception:  # TODO seperate different kinds of errors and inform in log. Perhaps create custom Exceptions
        print("ERROR %s user couldn't connect to X service" %user_id)
        return response

    print("DEBUG %s user odder is %s" % (user_id, offer))

    response["is_offer_valid"] = True
    response["offer_id"] = offer_id
    response["offer"] = offer

    return response


def does_user_have_amount(user_id):
    return True


def currency_to_bitcoin(amount):
    rate = 2
    return rate * amount


def bitcoin_to_destination(bitcoins_amount, bank_name, bank_number):
    rate = 0.7
    return rate * bitcoins_amount
