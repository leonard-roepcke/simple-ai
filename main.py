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
    spread=0.8,
    defosion=0.97
    )

evo.run(rounds=10000, population=20)