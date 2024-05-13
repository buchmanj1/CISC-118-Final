def blast_off(x):
    print(x)
    if x > 1:
        blast_off(x - 1)
    else:
        print("Blastoff!")


blast_off(10)
