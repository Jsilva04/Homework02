import unittest
from fasta_to_nexus import fasta_parser, nexus_header, nexus_matrix

class TestFastaToNexus(unittest.TestCase):

    def test_fasta_parser(self):
        expected = {
            'AB193435.1 Paguma larvata APOB gene for apolipoprotein B, partial cds, isolate: HS1198': 'accatcaaaatttctctgctggaaacaatgagaacaccatcgaggcccatgtaggaataaatggagaagccaatctggatttcctgaacattcctttaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaacaacacgcttgaaggagttcttgaagacaacaaagcaatcatttgatttaagtgtaaaggctcagtataagaaaaacaaagacaagcattccatcccaattcctttttatgtgaaagatttacaggcatcgagtaccccaaacagtattttaattccagccatgggcaatattacctatgatttttcctttaagtcaagtgtcatcacattgaataccaatgctggactttataaccagtcagatattgttgctcatttccttacttcctcttcttctgtcactgatgcactgcagtataaattagagggtacctcaagtttgacaaggaaaagaggcttgaagctagccacagctttgtctctgagtaataaatttgtagaaggcaatcatgacagtactattagtttgaccaagaaaaacatggaagcatcggtgacaacatctgcaaaagtccagattcccattttgagaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactgtctcttcatccattgaattaacatatgatttcaaatacccccatctgtacactactgccacaggggcagttgaccacaagctcatcttagaaagccttacctcttacttttccattgagtcatctaccaaaggagatatcaaggttttagtcctttcaaaggaatattcaggaactatttccagtgaggccagcacttatttgaattccaagagtactcgatcttcagtgaagttgcaaggggcttccaaagccgatggtatctggaacc',
            'AB193434.1 Panthera tigris APOB gene for apolipoprotein B, partial cds, isolate: HS1201': 'accatcaaaacttctctgctggaaacaatgagaacagcattgaggcccacgtaggaataaatggagaagccaatctggattttctgaacattcctctaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaaaaacaggcttgaaggaattcttgaagacaacaaagcaatcgtttgatttaagtgtaaatgctcagtataagaaaaacaaagacaagcattccatcccaatccctttttatgtaaaaggtttcgaggcagtgagtaccccaaacaatattttaattccagccatgggcaatattacctatgacttttcctttaagtcaagtgtcatcacactgaatgccaatgctggactttataaccagtcagatattgttgctcattttgttacttcctcttcttccgtcactgacacactggagtacaaattagagggcacctcaagtttgacaaggaaaagaggcttaaagctagccacagctttgtctctgagtaataaattcatggaaggcaatcatgacagtactattagtctgaccaagaaaagcatggaagcatcagtgacaacatctgcaaaagtccaaattcccattttgaaaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactatctcttcatccattgggttaacatatgatttcaattctcccaaactttactctactgctactggggcagttgaccacaagctcattttagaaagccttacctcttacttttctgttgagtcatctaccaaaggagatatcaagggttcagtcctttcacgggaatattcaggaactattgccagtgaggccagcacttatttgaattccaagagtactaggtctttagtgaagctgcaaggggcttccaaagtcgatggtatctggaacc', 
            'AB193433.1 Panthera pardus APOB gene for apolipoprotein B, partial cds, isolate: HS1203': 'accatcaaaacttctctgctggaaacaatgagaacagcattgaggcccacgtaggaataaatggagaagccaatctggattttctgaacattcctctaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaaaaacaggcttgaaggaattcttgaagacaacaaagcaatcgtttgatttaagtgtaaatgctcagtataagaaaaacaaagacaagcattccatcccaatccctttttatgtaaaaggtttccaggcagtgagtaccccaaacaatattttaattccagccatgggcaatattacctatgacttttcctttaagtcaagtgtcatcacactgaatgccaatgctggactttataaccagtcagatattgttgctcattttgttacttcctcttcttccgtcactgacacactggagtacaaattagagggcacctcaagtttgacaaggaaaagaggcttaaagctagccacagctttgtctctgagtaataaattcatggaaggcaatcatgacagtactattagtctgaccaagaaaagcatggaagcatcagtgacaacatctgcaaaagtccaaattcccattttgaaaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactatytcttcatccattgggttaacatatgatttcaattctcccaaactttactctactgctactggggcagttgaccacaagctcattttagaaagccttacctcttacttttctgttgagtcatctaccaaaggagatatcaagggttcagtcctttcacgggaatattcaggaactattgccagtgaggccagcacttatttgaattccaagagtactaggtctttagtgaagctgcaaggggcttccaaagtcgatggtatctggaacc', 
            'AB193432.1 Panthera leo APOB gene for apolipoprotein B, partial cds, isolate: HS1205': 'accatcaaaacttctctgctggaaacaatgagaacagcattgaggcccacgtaggaataaatggagaagccaatctggattttctgaacattcctctaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaaaaacaggcttgaaggaattcttgaagacaacaaagcaatcgtttgatttaagtgtaaatgctcagtataagaaaaacaaagacaagcattccatcccaatccctttttatgtaaaagatttccaggcagtgagtaccccaaacaatattttaattccagccatgggcaatattacctatgacttttcctttaagtcaagtgtcatcacactgaatgccaatgctggactttataaccagtcagatattgttgctcattttgttacttcctcttcttccatcactgacacactggagtacaaattagagggcacctcaagtttgacaaggaaaagaggcttaaagctagccacagctttgtctctgagtaataaattcatggaaggcaatcatgacagtactattagtctgaccaagaaaagcatggaagcatcagtgacaacatctgcaaaagtccaaattcccattttgaaaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactatttcttcatccattgggttaacatatgatttcaattctcccaaactttactctactgctactggggcagttgaccacaagctcattttagaaagccttacctcttacttttctgttgagtcatctaccaaaggagatatcaagggttcagtcctttcacgggaatattcaggaactattgccagtgaggccagcacttatttgaattccaagagtactaggtctttagtgaagctgcaaggggcttccaaagtcgatggtatctggaacc'
        }

        result = fasta_parser("data/teste.fasta")
        self.assertEqual(result, expected)

    def test_nexus_header(self):
        sequences = fasta_parser("data/teste.fasta")
        expected = (
            "#NEXUS\n\n"
            "BEGIN DATA;\n"
            "    DIMENSIONS NTAX=4 NCHAR=963;\n"
            "    FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"
            "    MATRIX\n"
        )
        result = nexus_header(sequences)
        self.assertEqual(result, expected)

    def test_nexus_matrix(self):
        sequences = fasta_parser("data/teste.fasta")
        expected = (
            "AB193435.1 Paguma larvata APOB gene for apolipoprotein B, partial cds, isolate: HS1198     accatcaaaatttctctgctggaaacaatgagaacaccatcgaggcccatgtaggaataaatggagaagccaatctggatttcctgaacattcctttaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaacaacacgcttgaaggagttcttgaagacaacaaagcaatcatttgatttaagtgtaaaggctcagtataagaaaaacaaagacaagcattccatcccaattcctttttatgtgaaagatttacaggcatcgagtaccccaaacagtattttaattccagccatgggcaatattacctatgatttttcctttaagtcaagtgtcatcacattgaataccaatgctggactttataaccagtcagatattgttgctcatttccttacttcctcttcttctgtcactgatgcactgcagtataaattagagggtacctcaagtttgacaaggaaaagaggcttgaagctagccacagctttgtctctgagtaataaatttgtagaaggcaatcatgacagtactattagtttgaccaagaaaaacatggaagcatcggtgacaacatctgcaaaagtccagattcccattttgagaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactgtctcttcatccattgaattaacatatgatttcaaatacccccatctgtacactactgccacaggggcagttgaccacaagctcatcttagaaagccttacctcttacttttccattgagtcatctaccaaaggagatatcaaggttttagtcctttcaaaggaatattcaggaactatttccagtgaggccagcacttatttgaattccaagagtactcgatcttcagtgaagttgcaaggggcttccaaagccgatggtatctggaacc\n" +
            "AB193434.1 Panthera tigris APOB gene for apolipoprotein B, partial cds, isolate: HS1201     accatcaaaacttctctgctggaaacaatgagaacagcattgaggcccacgtaggaataaatggagaagccaatctggattttctgaacattcctctaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaaaaacaggcttgaaggaattcttgaagacaacaaagcaatcgtttgatttaagtgtaaatgctcagtataagaaaaacaaagacaagcattccatcccaatccctttttatgtaaaaggtttcgaggcagtgagtaccccaaacaatattttaattccagccatgggcaatattacctatgacttttcctttaagtcaagtgtcatcacactgaatgccaatgctggactttataaccagtcagatattgttgctcattttgttacttcctcttcttccgtcactgacacactggagtacaaattagagggcacctcaagtttgacaaggaaaagaggcttaaagctagccacagctttgtctctgagtaataaattcatggaaggcaatcatgacagtactattagtctgaccaagaaaagcatggaagcatcagtgacaacatctgcaaaagtccaaattcccattttgaaaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactatctcttcatccattgggttaacatatgatttcaattctcccaaactttactctactgctactggggcagttgaccacaagctcattttagaaagccttacctcttacttttctgttgagtcatctaccaaaggagatatcaagggttcagtcctttcacgggaatattcaggaactattgccagtgaggccagcacttatttgaattccaagagtactaggtctttagtgaagctgcaaggggcttccaaagtcgatggtatctggaacc\n" +
            "AB193433.1 Panthera pardus APOB gene for apolipoprotein B, partial cds, isolate: HS1203     accatcaaaacttctctgctggaaacaatgagaacagcattgaggcccacgtaggaataaatggagaagccaatctggattttctgaacattcctctaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaaaaacaggcttgaaggaattcttgaagacaacaaagcaatcgtttgatttaagtgtaaatgctcagtataagaaaaacaaagacaagcattccatcccaatccctttttatgtaaaaggtttccaggcagtgagtaccccaaacaatattttaattccagccatgggcaatattacctatgacttttcctttaagtcaagtgtcatcacactgaatgccaatgctggactttataaccagtcagatattgttgctcattttgttacttcctcttcttccgtcactgacacactggagtacaaattagagggcacctcaagtttgacaaggaaaagaggcttaaagctagccacagctttgtctctgagtaataaattcatggaaggcaatcatgacagtactattagtctgaccaagaaaagcatggaagcatcagtgacaacatctgcaaaagtccaaattcccattttgaaaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactatytcttcatccattgggttaacatatgatttcaattctcccaaactttactctactgctactggggcagttgaccacaagctcattttagaaagccttacctcttacttttctgttgagtcatctaccaaaggagatatcaagggttcagtcctttcacgggaatattcaggaactattgccagtgaggccagcacttatttgaattccaagagtactaggtctttagtgaagctgcaaggggcttccaaagtcgatggtatctggaacc\n" +
            "AB193432.1 Panthera leo APOB gene for apolipoprotein B, partial cds, isolate: HS1205     accatcaaaacttctctgctggaaacaatgagaacagcattgaggcccacgtaggaataaatggagaagccaatctggattttctgaacattcctctaacaattcctgaaatgactctaccttacacagtgctcacaactcctcaggtgaaagatttctccttatgggaaaaaacaggcttgaaggaattcttgaagacaacaaagcaatcgtttgatttaagtgtaaatgctcagtataagaaaaacaaagacaagcattccatcccaatccctttttatgtaaaagatttccaggcagtgagtaccccaaacaatattttaattccagccatgggcaatattacctatgacttttcctttaagtcaagtgtcatcacactgaatgccaatgctggactttataaccagtcagatattgttgctcattttgttacttcctcttcttccatcactgacacactggagtacaaattagagggcacctcaagtttgacaaggaaaagaggcttaaagctagccacagctttgtctctgagtaataaattcatggaaggcaatcatgacagtactattagtctgaccaagaaaagcatggaagcatcagtgacaacatctgcaaaagtccaaattcccattttgaaaatgaatttcaaacaagaacttaatggaaataccaagtcaaagcctactatttcttcatccattgggttaacatatgatttcaattctcccaaactttactctactgctactggggcagttgaccacaagctcattttagaaagccttacctcttacttttctgttgagtcatctaccaaaggagatatcaagggttcagtcctttcacgggaatattcaggaactattgccagtgaggccagcacttatttgaattccaagagtactaggtctttagtgaagctgcaaggggcttccaaagtcgatggtatctggaacc\n" +
            "     ;\nEND;\n"
        )
        result = nexus_matrix(sequences)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
