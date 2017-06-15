import StringIO
import csv

csvVar = 'billingRate,clientName,clientLocation,anotherOne'

def template(inVar):
    oneVar = inVar

    #this takes the first character of the variable and converts it to uppercase
    oneVarStart = oneVar[0].upper() + oneVar[1:]

    template = "public String get" + oneVarStart + "(String " + oneVar + "){\n\t" + "return " + oneVar + ";\n}"

    return template


f = StringIO.StringIO(csvVar)
reader = csv.reader(f, delimiter=',')

for row in reader:
    for thing in row:
            print template(thing) + "\n"

#TODO - make the variable types into variables
