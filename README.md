Twilio Integration:

Supported Python Versions:

This library supports the following Python implementations:

Python 3.6+

Installation
Install from PyPi using pip, a package manager for Python.

    pip install twilio

Uses:

Below code shows how to use the module by passing whole necessary paarameters for using it.

    >>> from twilio_integration import TwilioClient
    >>> class_object = TwilioClient( account_sid="AC3XXXXXXXXXXXXXXXXXXXXXXXXXXXXdef", auth_token="7b9XXXXXXXXXXXXXXXXXXXXXXXXXXXXaf2", from_number="+19XXXXXXX40")
    >>> class_object.send_sms(msg="hello! World",       to_number="+91XXXXXXX065")
    {'status': 200, 'details': 'message sent successfully'}

And this below code shows how to use module with defining TwilioClient paramenter in os.enviroment.

    >>> from twilio_integration import TwilioClient
    >>> class_object = TwilioClient()
    >>> class_object.send_sms(msg="hello! World", to_number="+91XXXXXXX065")
    {'status': 200, 'details': 'message sent successfully'}

Tests:

For running test case -

 Create .env by taking referance from example.env and add require environment values.

Run unit test cases by using command:

    python test.py

Note: Test methods are mixture of both uses type so if you want to run whole test successful mention values in the globel variable of twilio_integration.py.  
