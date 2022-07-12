with open('data1.csv', 'r') as csv1, open('data2.csv', 'r') as csv2: # Import CSV files
    import1 = csv1.readlines()
    import2 = csv2.readlines()

with open('data_diff.csv', 'w') as outFile: # Create CSV file with differences
    for row in import2:
        if row not in import1:
            outFile.write(row)