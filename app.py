import csv, re, argparse

csvf = "csvtest1.csv"

def reg(m):
    return m.group(1)

def csvhandler(csvfile):
    with open(csvfile, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        linec = 0
        buglist = []
        for row in reader:
            if linec == 0:
                #print(f'Column names are {", ".join(row)}')
                linec += 1
            #print(f'OCPBUGS rows: {row["Resource URL"]}')
            while('' in row):
                row.remove('')
            buglist.append(row['Resource URL'].translate({ord(i): None for i in 'https://issues.redhat.com/browse/'}))
            linec += 1
    return buglist

def findbugs(data):
    #Remove empty results
    while('' in data):
        data.remove('')
    #Check for duplicates
    if len(data) == len(set(data)):
        #print("Found duplicates in list")
        return False
    else:
        #print("No duplicates found")
        True
    #Convert list to string and do clean-up
    bugstring=' '
    for x in data:
        bugstring += '{}, '.format(x)
    bugstring = re.sub("(.*)(.{2}$)",reg,bugstring)
    
    #Add JQL to string
    result = "project = OCPBUGS AND issuekey in ({})".format(bugstring)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import csv from Salesforce to create JQL to find OCPBUGS')
    parser.add_argument('-f', help='path to csv')
    args = parser.parse_args()
    print(findbugs(csvhandler(csvfile=args.f)))