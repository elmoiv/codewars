def data_reverse(data, help=[]):
    return data_reverse(data[:-8], help + data[-8:]) if data else help
