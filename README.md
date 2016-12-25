This is a Django API Server.

- To install required dependencies, run:
    pip install -r requirements.txt


- To run server, run:
    python manage.py runserver

 This runs the server at http://127.0,0.1:8000
 To change ip and port, read more at: https://docs.djangoproject.com/en/1.10/intro/tutorial01/


- As for now, only "get_offer" get request works. Usage example:
    127.0.0.1:8000/TransferMoney/getoffer?user_id=513&amount=100&destination_bank_name=poalim&destination_bank_number=5101



