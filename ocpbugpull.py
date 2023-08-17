import pandas as pd
import re, argparse

def reg(m):
    return m.group(1)

def readcsv(csvfile):
    df = pd.read_csv(csvfile, sep=';', usecols=['Resource URL'], na_values=' NaN')
    result = df.mask(df.eq('None')).dropna()
    return result

def dataframetostring(data):
    #Convert Resource URL rows to strings
    record = data.to_string(header=False,index=False,index_names=False).split('\n')
    vals = [','.join(ele.split()) for ele in record]
    return vals

def getocpbugs(lst):
    buglist = []
    for row in lst:
        buglist.append(row.translate({ord(i): None for i in 'https://issues.redhat.com/browse/'}))
    #Convert list to string and do clean-up
    bugstring=' '
    for x in buglist:
        bugstring += '{}, '.format(x)
    bugstring = re.sub("(.*)(.{2}$)",reg,bugstring)
    #Add JQL to string
    result = "project = OCPBUGS AND issuekey in ({})".format(bugstring)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import csv from Salesforce to create JQL to find OCPBUGS')
    parser.add_argument('-f', help='path to csv')
    args = parser.parse_args()
    print(getocpbugs(dataframetostring(readcsv(csvfile=args.f))))