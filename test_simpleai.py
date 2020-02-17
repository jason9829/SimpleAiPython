import unittest
from simpleai import response


# Added alphabet because the test run in alphabetical order (a-first to z-last)
class TestResponse(unittest.TestCase):
    def test_a_response_given_greeting_expect_greeting_from_function(self):
        # expected greeting message from function: Hi, nice to meet you! What's your name?
        #               (EXPECTED, ACTUAL)
        self.assertEqual("Hi, nice to meet you! What's your name?", response("greeting"))

    def test_b_response_given_replygreetingwithname_symbols_greetingwithusername(self):
        # default global user name: "defaultName"
        # expected greeting message from function: "Hi " + globalUserName + ", how's your day?"
        self.assertEqual("Hi " + "defaultName" + ", how's your day?", response("replygreetingwithname"))

    def test_c_response_given_farewell_expect_farewell_message(self):
        # expected farewell message from function: "Alright, see you soon."
        self.assertEqual("Alright, see you soon.", response("farewell"))

    def test_d_response_given_random_symbols_expect_error_message(self):
        # error message from function: Invalid Response Type Detected!
        self.assertEqual("Invalid Response Type Detected!", response("#$%^&*((!@!^&*()"))


if __name__ == '__main__':
    unittest.main()
