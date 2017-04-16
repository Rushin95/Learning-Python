import csv

writer = csv.writer(open('stock.csv', 'wb', buffering = 0))
writer.writerows([('GOOG', 'Google, Inc.', 505.34, 0.47, 0.6),
                   ('YHOO', 'Yahoo, Inc.', 50.34, 0.7, 0.6)])

stocks = csv.reader(open('stock.csv', 'rb'))

status_labels = {-1 : 'down',
                  0 : 'unchanged',
                  1 : 'up'
                 }


for ticker, name, price, change, pct in stocks:
    status = status_labels[cmp(float(change),0.0)]
    # %% is used to print the percentage sign
    print '%s is %s (%s%%)' % (name,status,pct)