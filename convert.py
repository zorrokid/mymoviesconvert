import xml.etree.ElementTree as ET
from importlib import reload
import csv
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')

with open('Collection.xml', 'r') as xml_file:
    tree = ET.parse("Collection.xml")
    root = tree.getroot()

    print('Starting')

    with open('Collection.csv', 'w') as csv_file:

        csvwriter = csv.writer(csv_file, delimiter='\t')

        header = [
                'Checked',
                'Original title',
                'Local title',
                'Year',
                'Media type',
                'Type',
                'Edition',
                'Country',
                'Case',
                'Discs',
                'Sub-fi',
                'Sub-en',
                'Aspect ratio',
                'Running time',
                'Director',
                'Status',
                'Condition',
                'Notes',
                'Watched',
                'Rental',
                'Slip Cover',
                'Hologram',
                'Id',
                'Barcode',
                'IMDB',
                'Collection'
                ]

        csvwriter.writerow(header)

        disctitles = root.find('DiscTitles')
        for disctitle in disctitles.findall('DiscTitle'):
            personal_data = disctitle.find('PersonalData')

            categories = disctitle.find('Categories')
            #categories
            slipcover = 'no'
            snapcase = False
            steelbook = False
            vuokraleffa = 'no'
            uusittava = 'no'
            hologrammikansi = 'no'
            checked = 'no'
            nordic = False
            for category in categories.findall('Category'):
                category_val = category.text.strip()
                if (category_val == 'Vuokraleffa'):
                    vuokraleffa = 'yes'
                if (category_val == 'Slipcover'):
                    slipcover = 'yes'
                if (category_val == 'Nordic'):
                    nordic = True
                if (category_val == 'Snap Case'):
                    snapcase = True
                if (category_val == 'Steelbook'):
                    steelbook = True
                if (category_val == 'Hologrammikansi'):
                    hologrammikansi = 'yes'

            row = []
            row.append(checked)
            originaltitle = disctitle.find('OriginalTitle').text.strip()
            localtitle = disctitle.find('LocalTitle').text.strip()

            row.append(originaltitle)
            if (originaltitle == localtitle):
                localtitle = ''
            row.append(localtitle)
            row.append(disctitle.find('ProductionYear').text.strip())            
            row.append(disctitle.find('MediaType').text.strip())
            row.append(disctitle.find('Type').text.strip())
            row.append(disctitle.find('Edition').text.strip())
            country = disctitle.find('Country').text.strip()
            if (nordic == True):
                country = 'Nordic'
            row.append(country)
            case = ''
            if (snapcase == True):
                case = 'Snap'
            if (steelbook == True):
                case = 'Steelbook'
            row.append(case)
            row.append(len(disctitle.find('Discs').findall('Disc')))

            subtitles = disctitle.find('Subtitles').findall('Subtitle')
            sub_fi = 'no'
            sub_en = 'no'
            for subtitle in subtitles:
                if subtitle.attrib['Language'] == 'Finnish':
                    sub_fi = 'yes'
                if subtitle.attrib['Language'] == 'English':
                    sub_en = 'yes'
            row.append(sub_fi)
            row.append(sub_en)
            
            row.append(disctitle.find('AspectRatio').text.strip())
            row.append(disctitle.find('RunningTime').text.strip())
            directors = []
            for person in disctitle.find('Persons').findall('Person'):
                if (person.find('Type').text.strip() == 'Director'):
                    directors.append(person.find('Name').text.strip())
            row.append(", ".join(directors))
            row.append(personal_data.attrib['Group'])
            row.append(personal_data.attrib['Condition'])
            row.append(personal_data.attrib['Notes'])
            watched = 'no'
            if (personal_data.attrib['Watched'] == 'True'):
                watched = 'yes'
            row.append(watched)


            row.append(vuokraleffa)
            row.append(slipcover)
            row.append(hologrammikansi)

            row.append(personal_data.attrib['CollectionNumber'])
            row.append(disctitle.find('Barcode').text.strip())
            row.append(disctitle.find('IMDB').text.strip())
            csvwriter.writerow(row)

print('Done')
