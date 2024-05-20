import sys

def fasta_parser(file):
    species = {}
    with open(file, 'r') as file:
        dna_found = False
        species_name = ""
        dna_sequence = ""
        sequence_length = None
        for line in file.readlines():
            line = line.replace("\n", "").replace("\r", "")
            if line.startswith(">"):
                if dna_found: 
                    if sequence_length is None:
                        sequence_length = len(dna_sequence)
                    else:
                        if (sequence_length != len(dna_sequence)):
                            sys.exit("Error: All DNA sequences must be the same length!")
                    species.update({species_name: dna_sequence})
                    species_name = line[1:]
                    dna_sequence = ""
                else:
                    species_name = line[1:]
                    dna_found = True
            elif line == "":
                if sequence_length is None:
                    sequence_length = len(dna_sequence)
                else:
                    if (sequence_length != len(dna_sequence)):
                        sys.exit("Error: All DNA sequences must be the same length!")
                species.update({species_name: dna_sequence})
                dna_found = False
                species_name = ""
                dna_sequence = ""
            elif dna_found:
                dna_sequence += line
        if dna_found:
            species.update({species_name: dna_sequence})
    return species

def nexus_header(species):
    taxa = len(species)
    chars = len((next(iter(species.values()))))
    header = (
       "#NEXUS\n\n"
        "BEGIN DATA;\n"
        f"    DIMENSIONS NTAX={taxa} NCHAR={chars};\n"
        "    FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"
        "    MATRIX\n"  
    )
    return header

def nexus_matrix(species):
    matrix = ""
    for species_name, dna_sequence in species.items():
        matrix += species_name + "     " + dna_sequence + "\n"
    matrix += "     ;\nEND;\n"
    return matrix

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fasta_to_nexus.py <input.fasta>")

    
    file = sys.argv[1]
    species = fasta_parser(file)
    header = nexus_header(species)
    matrix = nexus_matrix(species)

    output_nexus = header + matrix
    print(output_nexus)
    
