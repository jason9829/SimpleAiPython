globalUserName = "defaultName"  # Initilise global variable
# NOTE: # NO = The return value are just for unittest only
#             original code does not require the return to work


# Desc: Verify whether user input is greeting
# Param: Input from user in String
# Retval: True or False
def isUserInputGreeting(argument):
    switcher = {
        "hello": True,
        "hi": True,
        "how are you?": True,
        "morning": True,
        "afternoon": True,
        "evening": True,
        "noon": True,
    }
    return switcher.get(argument.lower(), False)


# Desc: Verify whether user input is farewell
# Param: Input from user in String
# Retval: True or False
def isUserInputFarewell(argument):
    switcher = {
        "bye": True,
        "see ya": True,
        "good bye?": True,
        "bye bye": True,
    }
    return switcher.get(argument.lower(), False)


# Desc: Get user name after greeting
# Param: None
# Retval: None since it's stored in Global variable
def getUserName():
    global globalUserName  # accessing the global viariable
    globalUserName = input()
    return globalUserName


# Desc: Response to user after asking for user name
# Param: Type of response
# Retval: None, result will be printed on console
def response(responseType):
    if responseType.lower() == "greeting":
        print("Hi, nice to meet you! What's your name?")
        return "Hi, nice to meet you! What's your name?"  # NO

    elif responseType.lower() == "replygreetingwithname":
        print("Hi " + globalUserName + ", how's your day?")
        return "Hi " + globalUserName + ", how's your day?"  # NO

    elif responseType.lower() == "farewell":
        print("Alright, see you soon.")
        return "Alright, see you soon."  # NO

    else:
        print("Invalid Response Type Detected!")
        return "Invalid Response Type Detected!"  # NO


# Desc: Main function to call relevant function to perform
#       chatting
# Param: Input from user in String
# Retval: None
def chatBot(inputFromUser):
    if isUserInputGreeting(inputFromUser) == True:
        response("greeting")
        getUserName()  # Store the user name @globalUserName
        retval = response("replyGreetingWithName")
        return retval  # NO

    elif isUserInputFarewell(inputFromUser) == True:
        retval = response("farewell")
        return retval  # NO
    else:
        print("I dont understand what you just said.")
        return "I dont understand what you just said."  # NO

        # Infinite Loop (remove because it cause unittest "hang, instantiating test")
        # while True:
        userInput = input()
        chatBot(userInput)
