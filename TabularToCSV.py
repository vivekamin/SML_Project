#Get acm_data.txt as input and you will be able to generate it's csv version.

import csv
from itertools import groupby



def load_dblp_arnet(infname, outfname):
    with open(infname, 'rb') as f, open(outfname, 'wb') as csvfile:
        csv_writer = csv.writer(
            csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        count = 0
        S = ['title', 'authors', 'year','venue','citation', 'refs', 'abstract']
        csv_writer.writerow(S)
        for key, group in groupby(f, key=lambda l: l.strip(' \n\r') == ''):
            if not key:
                refs = []
                authors = []
                title, venue, year, citation, abstract = [''] * 5
                for item in group:
                    item = item.strip(' \r\n')
                    if item.startswith('#*'):
                        title = item[2:]
                    elif item.startswith('#@'):
                        authors = item[2:].split(',')
                    elif item.startswith('#year'):
                        year = item[5   :]
                    elif item.startswith('#conf'):
                        venue = item[5:]
                    elif item.startswith('#citation'):
                        citation = item[9:]
                    elif item.startswith('#!'):
                        abstract = item[2:]
                    elif item.startswith('#%'):
                        refs.append(item[2:])
                csv_writer.writerow(
                    [title, authors, year,venue,citation, refs, abstract])
                count += 1
                print '\r%d\tlines' % (count,),


load_dblp_arnet('acm_data.txt', 'sample.csv')