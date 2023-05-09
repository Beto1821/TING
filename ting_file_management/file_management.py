import os  # module to perform file operations
import sys  # module to write error messages to stderr(standard error stream)


def txt_importer(path_file):
    if not os.path.exists(path_file):
        # If the file doesn't exist,
        #  write an error message to stderr and return an empty list
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    if not path_file.endswith('.txt'):
        # If the file extension is not .txt,
        #  write an error message to stderr and return an empty list
        print("Formato inválido", file=sys.stderr)
        return []

    # Open the file in read mode and read the contents into a string
    with open(path_file, 'r') as file:
        News = file.read().split('\n')

    return News
