answer = 0
while answer not in [1, 2, 3]:
    answer = int(input("""Choose an option:
    1. Words
    2. Numbers
    3. Conundrum\n\n"""))

if answer == 1:
    import wordgame
elif answer == 2:
    import numbersolver
else:
    import solver
