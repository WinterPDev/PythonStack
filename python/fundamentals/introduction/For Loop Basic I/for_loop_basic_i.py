# -- Print all integers from 0 to 150.
for x in range(0,150):
    print(x)
# --Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1000,5):
    print(x)
# --Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,100):
    if x % 10 == 0: 
        print("Coding Dojo") 
    elif x % 5 == 0: 
        print("Coding") 
    else: 
        print(x)
# --Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
oddsum = 0
for x in range(0,500000):
    if x % 2 != 0:
        oddsum += x
print(oddsum)
# -Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    if x % 2 == 0:
        print(x)
# --Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
#   For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 10
mult = 3

for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)



print(proteinSynthesis("CAAATGCAGGCGTAA"))

def synth(rna, exclude1, exclude2):
    for i in range(0,len(rna),3):
        codon = rna[i:i+3]
        if codon == exclude1 or exclude2:
            rna = rna.replace(exclude1,"").replace(exclude2,"")
    return rna

print(synth("CAAATGCAGGCGTAA", "CAA", "TAA"))

x = [1,2]

x.append(7)
print(x)