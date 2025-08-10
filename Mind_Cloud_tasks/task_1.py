"""
I will create a variable to store the name a list for arithmetic operations
and a dictionary for the questions.
I will put two example questions in the dictionary for clarification.
"""
questions = {
    "how are you": "i'm fine! how do you want me to help you today",
    "what's your name? ": "i'm a chat bot"
}

name = input("Hello there!\nPlease enter your name: ")
print(f"Hello {name}!")

while 1:
    result = 0
    ask = input("What do you want me to do?")

    if "+" in ask:
        ask = ask.split("+")
        for i in ask:
            result += int(i.strip()) #to remove any spaces before turn it to int
        print(f"The result will be {result}")

    elif "-" in ask:
        ask = ask.split("-")
        result = int(ask[0].strip())
        for i in ask[1:]:
            result -= int(i.strip())
        print(f"The result will be {result}")

    elif "*" in ask:
        ask = ask.split("*")
        result = 1
        for i in ask:
            result *= int(i.strip())
        print(f"The result will be {result}")

    elif "/" in ask:
        ask = ask.split("/")
        result = int(ask[0].strip())
        for i in ask[1:]:
            result /= int(i.strip())
        print(f"The result will be {result}")

    elif "add" in ask:
        ask = ask.split("add")
        for i in ask:
            result += int(i.strip())
        print(f"The result will be {result}")

    elif "subtract" in ask:
        ask = ask.split("subtract")
        result = int(ask[0].strip())
        for i in ask[1:]:
            result -= int(i.strip())
        print(f"The result will be {result}")

    elif ask in questions:
        print(questions[ask])

    else:
        print(f"sorry {name} i can't answer this question")

