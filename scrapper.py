import datefinder

with open('ynet.txt', 'r') as f:
    read_data = f.read()
    date = datefinder.find_dates(read_data, source=True)
for match in date:
    print match