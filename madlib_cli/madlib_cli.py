def read_template(pathOfFile):
    try :
        with open(pathOfFile)as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("file not found")