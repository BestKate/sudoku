def instructions():
    """
    shows instructions
    """
    read_text(file_name='instructions.txt')


def read_text(file_name) -> None:
    """
    read and shows file contents
    """
    with open(file_name, 'r') as file:
        readfile = file.read()
    print(readfile)
