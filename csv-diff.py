import csv
import sys

def get_csv_diff(file1, file2):
    # read the contents of the two files into two lists of rows
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        rows1 = [row for row in reader1]
        rows2 = [row for row in reader2]

    # compare the two lists of rows and store the differences in a list of rows
    diff_rows = []
    for i in range(min(len(rows1), len(rows2))):
        if rows1[i] != rows2[i]:
            diff_rows.append((','.join(rows1[i]), ','.join(rows2[i])))

    # output the differences as a CSV file
    with open('diff.csv', 'w', newline='') as diff_file:
        writer = csv.writer(diff_file)
        writer.writerow(['File 1', 'File 2'])
        writer.writerows(diff_rows)

    print('Differences written to diff.csv')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python csv_diff.py <file1> <file2>')
        sys.exit(1)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    get_csv_diff(file1, file2)
