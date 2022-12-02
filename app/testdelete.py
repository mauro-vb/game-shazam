from collections import Counter
import pandas as pd
import numpy as np


def show_results():

    probabilities= {
    "Among Us": 8.469408442797477e-13,
    "Apex Legends": 0.00782189890742302,
    "Fortnite": 3.1329201988228306e-7,
    "Forza Horizon": 3.666928023449145e-7,
    "Free Fire": 3.332720410753609e-8,
    "Genshin Impact": 1.2496562362684926e-7,
    "God of War": 0.9921765923500061,
    "Minecraft": 5.073176878589436e-10,
    "Roblox": 7.419536700581375e-7,
    "Terraria": 6.649480879111769e-12}

    count = Counter(probabilities)
    three_highest = count.most_common(4)

    pd.options.display.float_format = '{:.2f}'.format

    prob_table = pd.DataFrame(
    three_highest,
    columns= ["Game", "Certainty"]
   )

    prob_table["Certainty"] = prob_table["Certainty"].apply(
        lambda x: str(f"{round(x*100, 2)} %"))

    return prob_table



# set_index(keys="Game")


# print(first_choice)
