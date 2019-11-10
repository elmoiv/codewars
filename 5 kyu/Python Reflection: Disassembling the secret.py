import dis

def find_the_secret(f):
    return dis.Bytecode(f).dis()[92:124]
