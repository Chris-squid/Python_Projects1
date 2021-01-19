class User:
    name = 'Chris Rob'
    email = ' '
    password = '12345678'
    account_number = 0

class Employee(User):
    base_pay =12.00
    department = 'Floor'

class Customer(User):
    mailing_address = ' '
    mailing_list = True
