# El código siguiente, que crea un dataframe y quita las filas duplicadas, siempre se ejecuta y actúa como un preámbulo del script: 
# dataset = pandas.DataFrame(Capacitive, Inductive, reactive_type_second_line, activa, reactiva2, Rated power)
# dataset = dataset.drop_duplicates()
# Pegue o escriba aquí el código de script:

import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import math

plt.rcParams.update({'font.size': 30})
from matplotlib.pyplot import figure
figure(figsize=(25, 10), dpi=70)

max_rated_power = max(dataset['Rated power'])

phi1 = math.acos(dataset.Inductive[0])
sin1 = math.sin(phi1)
max_reactive_1 = max_rated_power * sin1

phi2 = math.acos(dataset.Capacitive[0])
sin2 = math.sin(phi2)
max_reactive_2 = max_rated_power * sin2 * dataset.reactive_type_second_line[0]

color1 = 'limegreen' # 'gray' # 'limegreen'# 'black'
color2_init = 'green' # 'black' # 'green'# 'grey'
r1 = 'i'
if dataset.reactive_type_second_line[0] > 0:
    color2 = color2_init
    r2 = 'i'  # type of reactive E --> inductive or capacitive
else:
    color2 = 'orange'
    r2 = 'c'

plt.scatter(dataset.activa, dataset.reactiva2, s=30)
plt.plot([0,max_rated_power], [0,max_reactive_1], c=color1, lw=2)
plt.plot([0,max_rated_power], [0,max_reactive_2], c=color2, lw=2)
# plt.plot(dataset.activa, dataset['reactiva 0.98'], c='orange')
# plt.plot(dataset.activa, dataset['reactiva 0.95'], c='orange')

# plt.title('Characteristic Curve Real power Vs Reactive Power', fontdict={'fontsize':30}, c="b")
plt.title(f"Real power Vs Reactive Power  -  RP: {max(dataset['Rated power'])}  -  {dataset.Inductive[0]} {r1}  -  {dataset.Capacitive[0]} {r2}", fontdict={'fontsize':30}, c="b")
plt.xlabel('Real Power', fontsize=25, c="r")
plt.ylabel('Reactive Power', fontsize=25, c="r")
plt.xlim([0, max_rated_power])
plt.tight_layout()

green_patch = mpatches.Patch(color=color1, label=f"Inductive 1 = {dataset.Inductive[0]}")
orange_patch = mpatches.Patch(color=color2, label=f"Inductive 2 = {dataset.Capacitive[0]}")
plt.legend(handles=[green_patch, orange_patch])

plt.show()
