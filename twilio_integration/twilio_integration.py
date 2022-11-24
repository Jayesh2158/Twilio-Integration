import os

from twilio.base.exceptions import TwilioException, TwilioRestException
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "")
FROM_NUMBER = os.environ.get("TWILIO_SENDER_NUM", "") 


class TwilioClient:
    def __init__(self, account_sid=None, auth_token=None, from_number=None):

        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number

        if account_sid is None or account_sid == "":
            self.account_sid = ACCOUNT_SID
        if auth_token is None or auth_token == "":
            self.auth_token = AUTH_TOKEN
        if from_number is None or from_number == "":
            self.from_number = FROM_NUMBER

    def send_sms(self, msg: str, to_number: str):

        try:
            client = Client(self.account_sid, self.auth_token)
        except TwilioException as err:
            return {"details": err, "status": 400}

        try:
            message = client.messages.create(
                from_=self.from_number, body=msg, to=to_number
            )
        except TwilioRestException as err:
            return {"status": err.status, "details": err.msg}

        if message.error_code or message.error_message:
            return {"status": message.error_code, "details": message.error_message}

        return {"status": 200, "details": "message sent successfully"}
