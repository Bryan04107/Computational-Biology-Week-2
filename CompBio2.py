def validate_dna(input, process_type):
    seqm = input.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("T") + seqm.count("G")

    codon_map = {
        'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 
        'CUA': 'Leucine', 'CUG': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine', 
        'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine', 'AUG': 'Methionine', 
        'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine', 

        'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 
        'CCA': 'Proline', 'CCG': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline', 
        'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine', 
        'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine', 

        'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UAA': 'Stop', 'UAG': 'Stop', 
        'CAA': 'Histidine', 'CAG': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 
        'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 
        'GAU': 'Asparatic Acid', 'GAC': 'Asparatic Acid', 'GAA': 'Glutamic Acid', 'GAG': 'Glutamic Acid', 

        'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'Stop', 'UGG': 'Tryptophan', 
        'CGA': 'Arginine', 'CGG': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 
        'AGU': 'Serine', 'AGC': 'Serine', 'AGA': 'Arginine', 'AGG': 'Arginine', 
        'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine', 
    }

    if valid == len(seqm):

        if process_type.lower() == "transcription":
            mrna_seq = ""
            for i in (seqm):
                if i == "A":
                    mrna_seq += "U"
                elif i == "T":
                    mrna_seq += "A"
                elif i == "C":
                    mrna_seq += "G"
                elif i == "G":
                    mrna_seq += "C"
            print("Original DNA Sequence   : ", seqm)
            print("mRNA Sequence           : ", mrna_seq)
            print("------------------------------------------------------------------")

        elif process_type.lower() == "translation":
            mrna_seq = ""
            for i in (seqm):
                if i == "A":
                    mrna_seq += "U"
                elif i == "T":
                    mrna_seq += "A"
                elif i == "C":
                    mrna_seq += "G"
                elif i == "G":
                    mrna_seq += "C"

            amino_acids = []
            for j in range(0, len(mrna_seq) - 2, 3):
                codon = mrna_seq[j:j + 3]
                if codon in codon_map:
                    if codon_map[codon] == 'Stop':
                        amino_acids.append(codon_map[codon])
                        break
                    amino_acids.append(codon_map[codon])
            
            print("Original DNA Sequence   : ", seqm)
            print("Transcribed RNA Sequence: ", mrna_seq)
            print("Translated Amino Acids  : ", " - ".join(amino_acids))
            print("------------------------------------------------------------------")

        else:
            print("Invalid process type. Choose 'transcription' or 'translation'.")
            print("------------------------------------------------------------------")

    else:
        print("Invalid DNA sequence")
        print("------------------------------------------------------------------")



validate_dna("ATTGCGT", "transcription")
validate_dna("ATGCGTATTTGA", "translation")
validate_dna("ATGCGTAACTGAA", "translation")
validate_dna("ATTGCGX", "translation")
validate_dna("ATTGCGT", "moop")