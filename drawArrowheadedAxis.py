'''
Author: Wkgreat
Date: 17 Mar 2017
Draw the axis with arrowhead
'''

def drawArrowheadedAxis(ax,position):
    '''
    :param ax: which axes
    :param position: which axis should be drawn, four axises "top","bottom","left", "right"
    :return: the arrow object
    '''

    xmin,xmax = ax.get_xlim()
    ymin,ymax = ax.get_ylim()

    if position == "top":
        xy = (xmax,ymax)
        xytext = (xmin,ymax)
    elif position == "bottom":
        xy = (xmax,ymin)
        xytext = (xmin,ymin)
    elif position == "left":
        xy = (xmin,ymax)
        xytext = (xmin,ymin)
    elif position == "right":
        xy = (xmax,ymax)
        xytext = (xmax,ymin)
    else:
        print "the postion should be 'top','bottom','left' or 'right'."
        return

    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # set properties of arrow
    arrowprops = { "arrowstyle":'-|>', # style and direction of arrow
                   "facecolor":"k", # face color of arrow
                   "edgecolor":"k" } # edge color of arrow

    arrow = ax.annotate("", xy=xy, xytext=xytext, xycoords="data",arrowprops=arrowprops)
    return arrow

def test():
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure(0,facecolor="w")
    ax = fig.add_subplot(111)

    x = np.linspace(0,100,1000)
    y = np.sin(x)
    ax.plot(x,y)

    drawArrowheadedAxis(ax, "bottom") # add bottom x axis
    drawArrowheadedAxis(ax, "left") # add left y axis
    plt.show()

if __name__ == "__main__":
    test()
