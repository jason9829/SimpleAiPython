globalUserName = 0 # Initilise global variable 

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
        "noon": True,
        "evening": True,
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
  global globalUserName   # accessing the global viariable
  globalUserName = input()

# Desc: Response to user after asking for user name 
# Param: Type of response
# Retval: None, result will be printed on console
def response(responseType):
  if responseType.lower() == "greeting":
    print("Hi, nice to meet you! What's your name?")
  elif responseType.lower() == "replygreetingwithname":
    print("Hi " + globalUserName + ", how's your day?")
  elif responseType.lower() == "farewell":
    print("Alright, see you soon.")

# Desc: Main function to call relevant function to perform
#       chatting
# Param: Input from user in String
# Retval: None
def chatBot(inputFromUser):
  if isUserInputGreeting(inputFromUser) == True:
    response("greeting")
    getUserName() # Store the user name @globalUserName
    response("replyGreetingWithName")

  elif isUserInputFarewell(inputFromUser) == True:
    response("farewell")
  else:
    print("I dont understand what you just said.")  

# Infinite Loop 
while True:
  userInput = input()
  chatBot(userInput)

# Reference
# [1]. https://data-flair.training/blogs/python-switch-case/