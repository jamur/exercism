def to_rna(dna_strand):
    return dna_strand.translate(str.maketrans("GCTA","CGAU"))

LOOK_UP = {"G": "C", "C": "G", "T": "A", "A": "U"}
def to_rna_dict(dna_strand):
    return "".join([LOOK_UP[char] for char in dna_strand])
