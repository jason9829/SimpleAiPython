import unittest
from unittest.mock import patch
from simpleai import response
from simpleai import getUserName
from simpleai import chatBot


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


# Ref: https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input (@Martjin Pieters)
class TestMockInputGetUserName(unittest.TestCase):
    @patch('simpleai.input', create=True)
    def test_e_mock_defaultName_expect_defaultName(self, mocked_input):
        # Mocked the input() function to return "defaultName"
        # Then, getUserName() will return the mocked_input
        mocked_input.side_effect = ["defaultName"]  # Without '[]', it will only mocked first character
        self.assertEqual("defaultName", getUserName())


class TestChatBot(unittest.TestCase):
    @patch('simpleai.getUserName', create=True)
    def test_f_mock_usernam_as_defaultName_expect_greeting_message_with_defaultName(self, mocked_getUserName):
        # Mocked the getUserName() function to return "defaultName"
        # as the user keyin name
        mocked_getUserName.side_effect = ["defaultName"]  # Without '[]', it will only mocked first character
        self.assertEqual("Hi defaultName, how's your day?", chatBot("hi"))

    def test_g_chatBot_given_bye_expect_farewell_message_from_bot(self):
        # Expected farewell message: "Alright, see you soon."
        self.assertEqual("Alright, see you soon.", chatBot("bye"))

    def test_h_chatBot_given_HI12399_expect_error_message_from_bot(self):
        # Expected error message: "I dont understand what you just said."
        self.assertEqual("I dont understand what you just said.", chatBot("HI12399"))


if __name__ == '__main__':
    unittest.main()
