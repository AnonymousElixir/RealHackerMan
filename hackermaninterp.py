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

        # Ignore comments
        if line.startswith("#"):
            return

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
        elif line.startswith("FUNC:"):
            self.define_function(line[5:])
        elif line.startswith("CALL:"):
            self.call_function(line[5:])
        elif line.startswith("SHOUT:"):
            self.shout(line[6:])
        elif line.startswith("SILENCE:"):
            self.silence(line[8:])
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

        # Check for list or dictionary assignments
        if value.startswith("[") and value.endswith("]"):
            value = eval(value)  # Evaluate the list
        elif value.startswith("{") and value.endswith("}"):
            value = eval(value)  # Evaluate the dictionary

        self.variables[var_name] = value
        print(f"🎉 Yay! Variable '{var_name}' now holds the magic value '{value}'! 🪄")

    def print_variable(self, var_name):
        var_name = var_name.strip()
        if var_name in self.variables:
            print(f"📜 {var_name}: {self.variables[var_name]} ✨")
        else:
            print(f"😱 Error: Variable '{var_name}' not found. It might be lost in space! 🚀")

    def conditional_statement(self, condition):
        condition = condition.strip()
        if "AND" in condition:
            conditions = condition.split("AND")
            if all(self.check_condition(cond.strip()) for cond in conditions):
                print(f"🎊 All conditions met! Let's party! 🎉")
            else:
                print("💔 Not all conditions were met. Back to the drawing board! 🎨")
        elif "OR" in condition:
            conditions = condition.split("OR")
            if any(self.check_condition(cond.strip()) for cond in conditions):
                print(f"🎊 At least one condition is met! Let's celebrate! 🎉")
            else:
                print("💔 No conditions were met. Time to rethink! 🤔")
        else:
            if self.check_condition(condition):
                print(f"🎊 Condition met: {condition} is true! 🎉")
            else:
                print(f"💔 Condition failed: {condition} is false. Better luck next time! 🍀")

    def check_condition(self, condition):
        parts = condition.split("==")
        if len(parts) == 2:
            var_name = parts[0].strip()
            expected_value = parts[1].strip().strip('"')
            actual_value = self.variables.get(var_name, None)
            return actual_value == expected_value
        return False

    def loop_statement(self, loop):
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

    def define_function(self, func_definition):
        func_name, params = func_definition.split("(")
        params = params.rstrip(")").strip().split(",") if ")" in params else []
        self.variables[func_name.strip()] = (params, [])
        print(f"✨ Function '{func_name.strip()}' defined with parameters: {params}.")

    def call_function(self, func_call):
        func_name, args = func_call.split("(")
        args = args.rstrip(")").strip().split(",") if ")" in args else []
        func_name = func_name.strip()

        if func_name in self.variables:
            params, body = self.variables[func_name]
            if len(params) == len(args):
                for param, arg in zip(params, args):
                    self.variables[param.strip()] = arg.strip()
                print(f"🎉 Calling function '{func_name}' with arguments: {args}!")
                # Here you could add more functionality to execute the body of the function.
            else:
                print(f"🚨 Error: Function '{func_name}' expects {len(params)} arguments but got {len(args)}.")
        else:
            print(f"🚨 Error: Function '{func_name}' is not defined. Did you forget to define it? 🤷")

    def shout(self, message):
        print(f"📣 SHOUTING: {message.upper()}!!! 🔊")

    def silence(self, message):
        print(f"🤫 Silencing: '{message}'. Shhh... 🤭")

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
