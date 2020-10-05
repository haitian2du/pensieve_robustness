import matplotlib
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
import numpy as np

plt.rcParams.update({'font.size': 15})
labels = ['LTE(41)', '3G(269)']


# set width of bar
bars1 = [115, -71]
bars2 = [117, -90]
bars3 = [121, -46]

bars1_err = [20.257, 16.207]
bars2_err = [14.872, 13.588]
bars3_err = [14.134, 8.821]

width = 25  # the width of the bars

x1 = [41, 269]
x2 = [p - width for p in x1]
x3 = [p + width for p in x1]


fig, ax = plt.subplots()
rects1 = ax.bar(x1, bars1, width, yerr=bars1_err, label='Pensieve')
rects2 = ax.bar(x2, bars2, width, yerr=bars2_err, label='BBA')
rects3 = ax.bar(x3, bars3, width, yerr=bars3_err, label='MPC')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Mean Reward')
ax.set_xticks(x1)
ax.set_xlabel('Divergence with Pensieve training traces')
ax.set_xticklabels(labels, fontweight='bold')
ax.legend(loc=9)



def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 15),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='right', va='top')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


fig.tight_layout()

plt.show()


# labels = ['fixed(34)', 'high(38971)', 'low(618582)', 'middle(1879068)']
#
# bars1 = [58, 73, 41, 56]
# bars2 = [48, 58, 36, 47]
# bars3 = [59, 72, 45, 58]
#
# bars1_err = [20.4, 4.1, 1.1, 3.1]
# bars2_err = [11.3, 3.1, 1.0, 2.0]
# bars3_err = [16.9, 5.7, 2.3, 2.9]
#
# width = 3500  # the width of the bars
#
# x1 = [34, 18971, 51858.2, 87906.8]
# x2 = [p - width for p in x1]
# x3 = [p + width for p in x1]
#
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(x1, bars1, width, yerr=bars1_err, label='Pensieve')
# rects2 = ax.bar(x2, bars2, width, yerr=bars2_err, label='BBA')
# rects3 = ax.bar(x3, bars3, width, yerr=bars3_err, label='MPC')
#
# #bax = brokenaxes(xlims=((0, 40000), (600000, 1900000)), hspace=5)
#
# ax.set_ylabel('Mean Reward')
# ax.set_xticks(x1)
# ax.set_xlabel('Divergence with Pensieve training traces')
# ax.set_xticklabels(labels, fontweight='bold')
# ax.legend(loc=9)
#
#
# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 30),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='right', va='top')
#
#
# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
#
# fig.tight_layout()
# plt.show()