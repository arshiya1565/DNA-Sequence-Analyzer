dna = input("Enter a DNA sequence: ").upper()

print("Your DNA sequence is:", dna)

print("A =", dna.count("A"))
print("T =", dna.count("T"))
print("G =", dna.count("G"))
print("C =", dna.count("C"))

gc = dna.count("G") + dna.count("C")
gc_percent = (gc / len(dna)) * 100

print("GC Content =", round(gc_percent, 2), "%")
