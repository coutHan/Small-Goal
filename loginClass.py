import os

import pyotp
import robin_stocks.robinhood as r
from dotenv import load_dotenv
import time


class Login:
    # This class is used to manage security and login
    # totp = None

    def __init__(self):
        print("Login init...")

    def login(self):
        load_dotenv()
        print("Current OTP:", type(os.environ['robin_mfa']))
        totp = pyotp.TOTP(os.environ['robin_mfa']).now()
        print("Current OTP:", totp)
        # Here I am setting store_session=False so no pickle file is used.
        login = r.login(os.environ['robin_username'],
                        os.environ['robin_password'], store_session=False, mfa_code=totp)
        # In the login dictionary, you will see that 'detail' is
        # 'logged in with brand new authentication code.' to show that I am not using a pickle file.
        print(login)
