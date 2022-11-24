import os
import unittest
import uuid

from dotenv import load_dotenv

from twilio_integration import TwilioClient

load_dotenv()

FAKE_ACCOUNT_SID = str(uuid.uuid4())
FAKE_AUTH_TOKEN = str(uuid.uuid4())

MESSAGE = str(uuid.uuid4())

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")


class TestSendSms(unittest.TestCase):
    """the arguments which is not pass by end user for class instance those are taken by the environment"""

    def test_send_sms_successfully(self):
        twilio_client = TwilioClient()
        result = twilio_client.send_sms(msg=MESSAGE, to_number=TO_NUMBER)
        self.assertEqual(
            result, {"status": 200, "details": "message sent successfully"}
        )

    def test_send_sms_without_from_number(self):
        twilio_client = TwilioClient(
            account_sid=ACCOUNT_SID,
            auth_token=AUTH_TOKEN,
        )
        result = twilio_client.send_sms(msg=MESSAGE, to_number=TO_NUMBER)
        self.assertEqual(
            result, {"status": 200, "details": "message sent successfully"}
        )

    def test_send_sms_without_auth_token_and_account_sid(self):
        twilio_client = TwilioClient(
            account_sid="", auth_token="", from_number=FROM_NUMBER
        )
        result = twilio_client.send_sms(msg=MESSAGE, to_number=TO_NUMBER)
        self.assertEqual(
            result, {"status": 200, "details": "message sent successfully"}
        )

    def test_send_sms_with_missing_to_number(self):
        twilio_client = TwilioClient(
            account_sid=ACCOUNT_SID,
            auth_token=AUTH_TOKEN,
            from_number=FROM_NUMBER,
        )
        result = twilio_client.send_sms(msg=MESSAGE, to_number="")
        self.assertEqual(
            result,
            {
                "status": 400,
                "details": "Unable to create record: A 'To' phone number is required.",
            },
        )

    def test_send_sms_without_to_number(self):
        twilio_client = TwilioClient(
            account_sid=ACCOUNT_SID,
            auth_token=AUTH_TOKEN,
            from_number=FROM_NUMBER,
        )
        try:
            result = twilio_client.send_sms(msg=MESSAGE)
        except TypeError as err:
            result = str(err)
        self.assertEqual(
            result, "send_sms() missing 1 required positional argument: 'to_number'"
        )

    def test_send_sms_with_missing_msg(self):
        twilio_client = TwilioClient(
            account_sid=ACCOUNT_SID,
            auth_token=AUTH_TOKEN,
            from_number=FROM_NUMBER,
        )
        result = twilio_client.send_sms(msg="", to_number=TO_NUMBER)
        self.assertEqual(
            result,
            {
                "status": 400,
                "details": "Unable to create record: Message body is required.",
            },
        )

    def test_send_sms_without_msg(self):
        twilio_client = TwilioClient(
            account_sid=ACCOUNT_SID,
            auth_token=AUTH_TOKEN,
            from_number=FROM_NUMBER,
        )
        try:
            result = twilio_client.send_sms(to_number=TO_NUMBER)
        except TypeError as err:
            result = str(err)
        self.assertEqual(
            result, "send_sms() missing 1 required positional argument: 'msg'"
        )

    def test_send_sms_with_wrong_auth_token_and_account_sid(self):

        twilio_client = TwilioClient(
            account_sid=FAKE_ACCOUNT_SID,
            auth_token=FAKE_AUTH_TOKEN,
            from_number=FROM_NUMBER,
        )
        result = twilio_client.send_sms(msg=MESSAGE, to_number=TO_NUMBER)
        self.assertEqual(result["status"], 404)


if __name__ == "__main__":
    unittest.main()
