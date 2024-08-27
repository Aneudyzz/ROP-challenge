'''
excercise ring of power
Summary of the exercise: What will happen if you had to give the rings of power amongst the races of middle earth

Requirements:
1. The Elfs must receive un-even number.
2. The Dwarfs Must receive a Prime number.
3. The Man will receive an even number.
4. Sauron always gets one.

Actions:
1. Create a program that receives the total number of rings of Power and searches through for a possible combination to deliver them.
2. Show the Final result of the rings that were given or the error by doing so.
'''

#ROP =  Ring of Power






def distribute_rop(total_rop):
    if total_rop < 4:
        raise ValueError("Total ROP must be at least 4")

    Sauron = 1
    remaining = total_rop - Sauron

    # Elves get an odd number
    Elves = 1
    while Elves < remaining and (remaining - Elves) < 3:
        Elves += 2
        remaining -= Elves

    # Dwarves get a prime number
    Dwarf = 2
    while Dwarf < remaining - 2:
        if is_prime(Dwarf) and is_prime(remaining - Dwarf):
            break
        Dwarf += 1
    remaining -= Dwarf

    # Man gets the remaining even number
    Man = remaining
    while Man % 2 != 0:
        # Adjust Elves and Dwarves if possible
        if Elves > 2:
            Elves -= 2
            Man += 2
        elif Dwarf > 2:
            # Find the next prime number less than Dwarf
            next_prime = Dwarf - 1
            while not is_prime(next_prime):
                next_prime -= 1
            Dwarf = next_prime
            Man += 2
        else:
            # If no adjustments are possible, adjust Sauron
            Sauron += 1
            Man -= 1

    return Sauron, Elves, Dwarf, Man

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get user input
print("The Division of the Rings of Power in Middle Earth Begins!")
while True:
    try:
        total_rop = int(input("How many rings of power do we have available? "))
        sauron, elves, dwarves, man = distribute_rop(total_rop)
        break
    except ValueError:
        print("Please enter a number greater than or equal to 4.")

# Distribution
Sauron, Elves, Dwarf, Man = distribute_rop(total_rop)

# Printing results
print(f"Sauron gets {Sauron} ring.")
print(f"Elves get {Elves} rings.")
print(f"Dwarves get {Dwarf} rings.")
print(f"Men get {Man} rings.")