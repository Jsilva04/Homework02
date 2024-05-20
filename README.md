# FASTA to NEXUS Converter

This repository contains a Python script for converting FASTA files to NEXUS format and a set of unit tests to verify the functionality of the conversion script.

## Motivation

The purpose of this repository is to provide a simple tool for converting genetic sequence data from the widely used FASTA format to the NEXUS format, which is commonly used in phylogenetic analysis software. The provided scripts are useful for researchers and bioinformaticians who need to prepare their data for analysis in NEXUS-compatible tools.

## Scripts

### `fasta_to_nexus.py`

This script reads a FASTA file and outputs the corresponding NEXUS file content to the standard output.

#### Functions

- `parse_fasta(file_path)`: Reads a FASTA file and returns a dictionary with sequence names as keys and sequences as values.
- `generate_nexus_header(sequences)`: Generates the header section of the NEXUS file based on the number of sequences and their length.
- `generate_nexus_matrix(sequences)`: Creates the MATRIX block of the NEXUS file using the sequences.

#### Usage

To run the script, use the following command:

```bash
python fasta_to_nexus.py <input.fasta>
```

### `test_fasta_to_nexus.py´

This script contains unit tests for the `fasta_to_nexus.py´ script to ensure that each function works as expected.

#### Functions

- `test_fasta_parser(self)`: Compares the expected output with the output given by the fasta parser function.
- `test_nexus_header(self)`: Compares the expected output with the output given by the nexus header function.
- `test_nexus_matrix(self)`: Compares the expected output with the output given by the nexus matrix function.

#### Usage
```bash
python -m unittest test_fasta_to_nexus.py
```

## License
MIT License
