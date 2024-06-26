dna_to_rna_bases = {"G" : "C", "C" : "G", "A" : "U", "T" : "A"}
amino_acids = {"UUU" : "Phe", "UUC" : "Phe", "UUA" : "Leu", "UUG" : "Leu",
            "CUU" : "Leu", "CUC" : "Leu", "CUA" : "Leu", "CUG" : "Leu",
            "AUU" : "Ile", "AUC" : "Ile", "AUA" : "Ile", "AUG" : "Met",
            "GUU" : "Val", "GUC" : "Val", "GUA" : "Val", "GUG" : "Val",
            "UCU" : "Ser", "UCC" : "Ser", "UCA" : "Ser", "UCG" : "Ser",
            "CCU" : "Pro", "CCC" : "Pro", "CCA" : "Pro", "CCG" : "Pro",
            "ACU" : "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG" : "Thr",
            "GCU" : "Ala", "GCC" : "Ala", "GCA" : "Ala", "GCG" : "Ala",
            "UAU" : "Tyr", "UAC" : "Tyr", "UAA" : "STOP", "UAG" : "STOP",
            "CAU" : "His", "CAC" : "His", "CAA" : "Gln", "CAG" : "Gln",
            "AAU" : "Asn", "AAC" : "Asn", "AAA" : "Lys", "AAG" : "Lys",
            "GAU" : "Asp", "GAC" : "Asp", "GAA" : "Glu", "GAG" : "Glu",
            "UGU" : "Cys", "UGC" : "Cys", "UGA" : "STOP", "UGG" : "Trp",
            "CGU" : "Arg", "CGC" : "Arg", "CGA" : "Arg", "CGG" : "Arg",
            "AGU" : "Ser", "AGC" : "Ser", "AGA" : "Arg", "AGG" : "Arg",
            "GGU" : "Gly", "GGC" : "Gly", "GGA" : "Gly", "GGG" : "Gly"
              }

def check_dna(dna):
    if len(dna)%3!=0:
        return False
    else:
        for i in dna:
            if i not in "ATGC":
                return False
    return True

def dna_to_rna(dna):
    vaihda_emas=""
    for i in dna:
        if i =="A":
            vaihda_emas+="U"
        elif i =="C":
            vaihda_emas+="G"
        elif i=="T":
            vaihda_emas+="A"
        else:
            vaihda_emas+="C"
    return vaihda_emas

def rna_to_protein(rna):
   proteiini=""
   if len(rna)%3==0:
       for i in range(0, len(rna), 3):
           kodoni = rna[i:i+3]
           if amino_acids[kodoni]=="STOP":
               proteiini = proteiini + "*-"
           else:
               proteiini = proteiini + amino_acids[kodoni]+"-"
   proteiini=proteiini[:-1]
   return proteiini

def main():
    dna_jarjestys = input("Enter the DNA sequence:\n")
    dna_jarjestys_isoin_kirjaimin = dna_jarjestys.upper()
    dna_ketju = check_dna(dna_jarjestys_isoin_kirjaimin)
    if dna_ketju == False:
        print("Sorry,",dna_jarjestys_isoin_kirjaimin,"is not a valid DNA sequence for protein synthesis.")
    else:
        print("DNA:",dna_jarjestys_isoin_kirjaimin,"")
        rna_ketju = dna_to_rna(dna_jarjestys_isoin_kirjaimin)
        print("RNA:",rna_ketju,"")
        rna_proteiiniksi = rna_to_protein(rna_ketju)
        print("Protein:",rna_proteiiniksi,"")
        rna_lista = rna_proteiiniksi.split("-")
        print("The protein has {:d} amino acids in total.".format(len(rna_lista)))








main()