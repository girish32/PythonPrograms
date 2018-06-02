from pprint import pprint


def parse_table(filehandle):
    '''grab the next table out of filehandle'''
    # clear first newline
    next(filehandle)
    headers = next(filehandle).split()
    # clear out +---... line
    next(filehandle)

    data = []
    for line in filehandle:
        cols = line.split()
        if not cols:
            # blank line indicates end of a table
            break

        # grab the data and time
        if cols[0] == 'pm':
            # pm does not have a date, so grab the last one
            date = data[-1][0]
            time = cols[0]
            cols = cols[1:]
        else:
            date = cols[0]
            time = cols[1]
            cols = cols[2:]

        row = [date, time] + cols
        data.append(row)

    return data


def parse(filename='projload.txt'):
    filehandle = open(filename)

    result = {}
    while True:
        line = next(filehandle, None)
        if line is None:
            break
        if line.isupper():
            region = line.strip()
            result[region] = parse_table(filehandle)

    return result


r = parse()
pprint(r)