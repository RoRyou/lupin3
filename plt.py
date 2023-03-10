import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def Stackedbar(titlename, xlabel, label, botV, cenV, topV):
    plt.title(titlename)
    N = len(xlabel)
    ind = np.arange(N)  # [ 0  1  2  3  4  5  6  7  8 ]
    plt.xticks(ind, xlabel)

    # plt.ylabel('Scores')
    Bottom, Center, Top = botV, cenV, topV

    d = []
    for i in range(0, len(Bottom)):
        sum = Bottom[i] + Center[i]
        d.append(sum)

    colors = list(mcolors.TABLEAU_COLORS.keys())

    p1 = plt.bar(ind, Bottom, color=colors[0])
    p2 = plt.bar(ind, Center, bottom=Bottom, color=colors[1])
    p3 = plt.bar(ind, Top, bottom=d, color=colors[2])

    plt.legend((p1[0], p2[0], p3[0]), label, loc=2)

    plt.show()


def multiplebar(n=2, total_width=0.5, size=5):
    print('待修改')
    x = np.arange(size)
    a = np.random.random(size)
    b = np.random.random(size)
    c = np.random.random(size)

    # total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, a, width=width, label='a')
    plt.bar(x + width, b, width=width, label='b')
    plt.bar(x + 2 * width, c, width=width, label='c')
    plt.legend()

    plt.plot(x, a)
    plt.plot(x + width, b)
    plt.plot(x + 2 * width, c)
    # plt.plot(x, y, "r", marker='*', ms=10, label="a")
    # plt.xticks(rotation=45)
    # plt.legend(loc="upper left")

    plt.show()


def pieplt(sizes, labels=0):
    explode = len(sizes) * [0]  # 突出显示，这里仅仅突出显示第二块（即'Hogs'）
    explode[sizes.index(max(sizes))] = 0.1

    if labels == 0:
        labels = range(len(sizes))

    plt.pie(sizes, explode=explode, labels=labels,  autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
    plt.show()



def plt3bar(l1,l2,l3,labels,xlabel = 'Scoresx',ylabel='Scores'):

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    r1 = np.arange(len(labels))
    r2 = [x + width for x in r1]
    r3 = [x + width for x in r2]


    fig, ax = plt.subplots()
    rects1 = ax.bar(r1, l1, width, label='Men')
    rects2 = ax.bar(r2, l2, width, label='Women')
    rects3 = ax.bar(r3, l3, width, label='Womens')


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_title(xlabel)


    ax.bar_label(rects1, padding=3)  # 更加简单好用的api
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)


    plt.xticks([r + width for r in range(len(l1))], labels)


    fig.tight_layout()

    plt.show()