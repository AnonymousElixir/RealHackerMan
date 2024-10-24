    code = """
    # Define a function
    FUNC: my_cool_function(param1, param2)

    # Use the function
    CALL: my_cool_function("Hello", "World")

    # Variable assignments
    secret_message = "Hacking is fun!"
    numbers = [1, 2, 3, 4, 5]
    data = {"key": "value", "another_key": [10, 20, 30]}

    # Print statements
    PRINT: secret_message
    PRINT: numbers
    PRINT: data

    # Conditional statements
    IF: secret_message == "Hacking is fun!"
    IF: secret_message == "Hacking is fun!" OR numbers[0] == 1
    IF: secret_message == "Not fun" AND numbers[1] == 2

    # Looping
    LOOP: 5 times

    # Shouting and silence
    SHOUT: HACKING IS AWESOME!
    SILENCE: This is a secret message.

    # Random hacker command
    RANDOM HACKER COMMAND

    # Sleep
    SLEEP: 3

    # Code Red
    CODE RED
    """

    interpreter = RealHackerManInterpreter()
    interpreter.execute(code)
