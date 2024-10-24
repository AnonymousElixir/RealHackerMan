from hackermaninterp import RealHackerManInterpreter

code = """
HACKER: hack the planet 🌍
secret_message = "Hacking is fun!"
PRINT: secret_message
IF: secret_message == "Hacking is fun!"
LOOP: 5 times
HACKER: uninstall gravity 🪂
RANDOM HACKER COMMAND
SLEEP: 3
CODE RED
"""

interpreter = RealHackerManInterpreter()
interpreter.execute(code)
