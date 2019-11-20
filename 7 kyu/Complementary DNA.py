def DNA_strand(dna):
    return ''.join({'T':'A','A':'T','G':'C','C':'G'}[i] for i in dna)
