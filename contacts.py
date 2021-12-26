import csv
# function that reads the csv file and generates a dict of contacts
def read_file():
    file_name = "fam.csv"
    try:
        fp = open(file_name,'r')
    except FileNotFoundError:
        print("Could not find contacts file!")
    else:
        return fp

def gen_dict():
    contact_data = dict()
    contact_wb = csv.reader(read_file())
    #skip the header
    header = next(contact_wb,None)
    for row in contact_wb:
        contact_data[str(row[0])] = row[1]
    return(contact_data)
