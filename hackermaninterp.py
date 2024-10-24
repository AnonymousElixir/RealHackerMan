import random

class RealHackerManInterpreter:
    def __init__(self):
        self.variables = {}
        self.hacker_commands = [
            "hack the planet 🌍",
            "uninstall gravity 🪂",
            "launch potato rocket 🥔🚀",
            "become a cat 😺",
            "make coffee ☕"
        ]

    def execute(self, code):
        lines = code.strip().splitlines()
        for line in lines:
            self.process_line(line)

    def process_line(self, line):
        line = line.strip()
        if line.startswith("HACKER:"):
            self.hacker_command(line[7:])
        elif "=" in line:
            self.assign_variable(line)
        elif line.startswith("PRINT:"):
            self.print_variable(line[6:])
        elif line.startswith("IF:"):
            self.conditional_statement(line[3:])
        elif line.startswith("LOOP:"):
            self.loop_statement(line[5:])
        elif line == "CODE RED":
            self.code_red()
        elif line == "RANDOM HACKER COMMAND":
            self.random_hacker_command()
        elif line.startswith("SLEEP:"):
            self.sleep_command(line[6:])
        else:
            print(f"Whoa there! Syntax Error: {line} 🚫")

    def hacker_command(self, command):
        if command in self.hacker_commands:
            print(f"🔥 Boom! Executing: {command}! 🚀")
        else:
            print(f"Uh-oh! Unknown hacker command: {command}. Maybe try 'hack the planet'? 🤔")

    def assign_variable(self, line):
        var_name, value = line.split("=")
        var_name = var_name.strip()
        value = value.strip()
        self.variables[var_name] = value
        print(f"🎉 Yay! Variable '{var_name}' now holds the magic value '{value}'! 🪄")

    def print_variable(self, var_name):
        var_name = var_name.strip()
        if var_name in self.variables:
            print(f"📜 {var_name}: {self.variables[var_name]} ✨")
        else:
            print(f"😱 Error: Variable '{var_name}' not found. It might be lost in space! 🚀")

    def conditional_statement(self, condition):
        # Example: IF: secret_message == "Hacking is fun!"
        condition = condition.strip().split("==")
        if len(condition) == 2:
            var_name = condition[0].strip()
            expected_value = condition[1].strip().strip('"')
            actual_value = self.variables.get(var_name, None)
            if actual_value == expected_value:
                print(f"🎊 Condition met: '{var_name}' is as fabulous as '{expected_value}'! 🎉")
            else:
                print(f"💔 Condition failed: '{var_name}' is not equal to '{expected_value}'. Better luck next time! 🍀")
        else:
            print("🚨 Error: Invalid conditional format. Use 'IF: var_name == value'.")

    def loop_statement(self, loop):
        # Example: LOOP: 3 times
        parts = loop.strip().split(" ")
        if len(parts) == 3 and parts[1].lower() == "times":
            try:
                count = int(parts[0])
                for i in range(count):
                    print(f"🔄 Loop iteration {i + 1}! Round and round we go! 🎡")
            except ValueError:
                print("🚨 Error: Loop count must be a number. No magic here!")
        else:
            print("🚨 Error: Invalid loop format. Use 'LOOP: count times'.")

    def code_red(self):
        print("🚨 CODE RED! Activating self-destruct sequence... Just kidding! Chill out! 😜")

    def random_hacker_command(self):
        command = random.choice(self.hacker_commands)
        print(f"🎲 Random Hacker Command: {command}! Let's get wild! 🤪")

    def sleep_command(self, seconds):
        try:
            seconds = int(seconds)
            if seconds < 0:
                print("🚫 Error: Cannot sleep for a negative time! That’s just silly! ⏳")
            else:
                print(f"😴 Zzz... Sleeping for {seconds} seconds... Sweet dreams! 🌙")
        except ValueError:
            print("🚨 Error: SLEEP command requires a number. Count sheep instead!")
