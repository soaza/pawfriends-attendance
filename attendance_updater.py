import csv

def main():
   with open('BFF tracking sheet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')

if __name__ == "__main__":
    main()