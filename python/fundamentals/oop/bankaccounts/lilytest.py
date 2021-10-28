import math
import os
import random
import re
import sys
from typing import Dict
from textwrap import wrap


start_codon: str = "AUG"
stop_codon: str = "STOP"
codon_to_amino_acid: Dict[str, str] = {
    "AUG": "Met",
    "CAA": "Gln",
    "CAG": "Gln",
    "GGU": "Gly",
    "GCG": "Ala",
    "UUU": "Phe",
    "UUC": "Phe",
    "UGG": "Trp",
    "UAA": stop_codon,
    "UAG": stop_codon,
    "UGA": stop_codon,
    "TAA": stop_codon,
}

def protein_synthesis_part_one(dna):
    is_open = False #establishes that the sequence starts off closed and uses this to remove anything before the start codon
    text = "" #starts the blank string for the answer
    for sequence in wrap(dna, 3): #beginning of our for loop telling it to go by steps in 3
        if sequence == "CAA": # the opening item to start the string that we want to use but is before the start codon
            is_open = True
        elif sequence == "TAA": #establishes the stop codon of the string
            is_open = False
        elif is_open:
            sequence = sequence.replace("CAA", "")
            sequence = sequence.replace("ATG", "AUG")
            text += codon_to_amino_acid[sequence] + " "

#once it's open lines 35-38 have it iterate through the loop, filtering out the non used parts
#and using the dictionary to conver the rna to the amino acids

    return text 
print(protein_synthesis_part_one("CAAATGCAGGCG"))