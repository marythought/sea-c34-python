# safe_input for task 10


def safe_input(function):
    try:
        function
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

safe_input(name=raw_input("what is your name?"))
