def number(bus_stops):
    return (lambda x, y: x - y)(*map(sum, zip(*bus_stops)))
