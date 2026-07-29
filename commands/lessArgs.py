def ZeroArgs(command):
    print(f"{command}: missing operand")
    print(f"Try '{command} --help' for more information.")

def LessArgs(command, arg1):
    print(f"command: missing operand after '{arg1}'")
    print(f"Try '{command} --help' for more information.")