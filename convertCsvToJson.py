import csv
import json

with open("collection.tsv", encoding='utf8') as csv_file:
    #csv_reader = csv.reader(csv_file, dialect="excel-tab")
    # Checked	Original title	Local title	Year	Media type	Type	Edition	Country	Case	Discs	Sub-fi	Sub-en	Aspect ratio	Running time	Director	Status	Condition	Notes	Watched	Rental	Slip Cover	Hologram	Id	Barcode	IMDB	Collection	Part of Collection	Collection Id	Series

    #index_OriginalName = 1
    #for row in csv_reader:
    #    print(row)
    #    movie = {'originalName': row[1]}
    #    print(json.dumps(movie))
    csv_reader = csv.DictReader(csv_file)
    data = [r for r in csv_reader]
    print(data[0]["Original title"])
