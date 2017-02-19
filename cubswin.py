inning = 0

indiansruns = [0, 0, 1, 0, 2, 0, 0, 3, 0, 1]
cubsruns = [1, 0, 0, 2, 2, 1, 0, 0, 0, 2]

indiansscore = 0
cubsscore = 0

for i in range(0, 10):
        indiansscore = indiansscore + indiansruns[i]
        cubsscore = cubsscore + cubsruns[i]
        inning += 1
        print("After " + str(inning) + "innings, the score is Indians: " + str(indiansscore) + " Cubs: " + str(cubsscore) + ".")

        if inning == 10 and cubsscore > indiansscore:
            print("CUBS WIN!")
            print("Chicago Cubs: 2016 World Series Champions!")
