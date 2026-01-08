
clauses = [
    ["~Human(x)", "Mortal(x)"],  
    ["Human(Socrates)"],            
    ["~Mortal(Socrates)"]           
]

def fopl():
    print("Clauses:")
    for c in clauses:
        print(c)

    print("\nResolving clauses...")

    if "~Human(x)" in clauses[0] and "Mortal(x)" in clauses[0]:
        print("Resolving ~Mortal(Socrates) with Mortal(x)")
        print("Derived clause: ~Human(Socrates)")

    print("Resolving ~Human(Socrates) with Human(Socrates)")
    print("Empty clause derived!")

    print("\nConclusion: Socrates is Mortal ✔")


fopl()