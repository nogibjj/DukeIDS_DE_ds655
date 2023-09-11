#   Importing Packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd


def PandasPlot(df):
    groups = df.groupby('species')
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(group.sepal_length, group.sepal_width, marker='o', linestyle='', ms=12, label=name)
    ax.legend()
    plt.savefig('./Resources/plot image.png')
    plt.show()
    print(plt)
    image = mpimg.imread('./Resources/plot image.png')
    plt.imshow(image)
    plt.show()