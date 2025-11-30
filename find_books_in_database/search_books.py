import csv
import sys
import os

def search_books(filename, query):
    matches = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if query.lower() in row[0].lower():
                    matches.append(row[0])
    else:
        print(f"File not found: {filename}", file=sys.stderr)
    return matches

if __name__ == "__main__":
    filename = sys.argv[1]
    query = sys.argv[2]
    
    results = search_books(filename, query)
    for result in results:
        print(result)
