import time
import evolotion
print("init ai at: " + str(time.time()))

evo = evolotion.Evolution(
    values= [
        [[0, 0],[0, 1]],
        [[0, 1],[1, 0]],
        [[1, 0],[1, 0]],
        [[1, 1],[0, 1]],
    ],
    spread=0.4,
    defosion=0.94,
    hidenlayer=4,
    hidenSize=3
    )

evo.run(rounds=1000, population=20)