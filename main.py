import numpy as np
import matplotlib.pyplot as plt

x = range(100)
y = range(100)

days = (
        "72225",
        "72325",
        "7`2625"
        )

Set_Counts = {
        "Set 1": np.array([6,7,8]),
        "Set 2": np.array([3,5,7]),
        "Set 3": np.array([0,3,5]),
        }

width = 0.5
fig, ax = plt.subplots()
bottom = np.zeros(3)

for set_name, weight_count in Set_Counts.items():
    p = ax.bar(days,Set_Counts,width,label=set_name, bottom=bottom)
    bottom += weight_count

ax.set_title("Progressive Overload for Upper Body")
ax.legend(loc="upper right")

plt.show()



