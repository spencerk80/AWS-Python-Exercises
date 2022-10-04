# Vars
inputFilename = "preproinsulin-seq.txt"
outputFilename = "formated-preproinsulin-seq.txt"

inputFile = open(inputFilename, "r")
contents = inputFile.readlines()

outputFile = open(outputFilename, "w")
output = ""

# Remove unwanted stuff
output = output.join([c for c in contents[1] if not c.isdigit() and c != ' '])
output += "".join([c for c in contents[2] if not c.isdigit() and c != ' '])
output = output.replace('\n', '')
output = output.replace('\r', '')

outputFile.write(output)

inputFile.close()
outputFile.close()

# Write all the files needed for lab
file = open("lsinsulin-seq-clean.txt", 'w')
file.write(output[0:24])
file.close()

file = open("binsulin-seq-clean.txt", 'w')
file.write(output[24:54])
file.close()

file = open("cinsulin-seq-clean.txt", 'w')
file.write(output[55:89])
file.close()

file = open("ainsulin-seq-clean.txt", 'w')
file.write(output[89:])
file.close()

# Store the numan preproinsulin sequence in a var called preproinsulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))