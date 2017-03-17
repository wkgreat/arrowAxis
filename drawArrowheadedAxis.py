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

    if position not in ["top","bottom","left","right"]:
        print "the postion should be 'top','bottom','left' or 'right'."
        return

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

    # set properties of arrow
    arrowprops = { "arrowstyle":'-|>', # style and direction of arrow
                   "facecolor":"k", # face color of arrow
                   "edgecolor":"k" } # edge color of arrow

    arrow = ax.annotate("", xy=xy, xytext=xytext, xycoords="data",arrowprops=arrowprops)
    return arrow

def test():
    '''an example for ploting'''
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure(0,facecolor="w")
    ax = fig.add_subplot(111)

    #draw a curve
    x = np.linspace(0,6*np.pi,1000)
    y = np.sin(x)
    ax.axis([0,6*np.pi,-1,1])
    ax.plot(x,y)

    ax.spines["top"].set_visible(False) #turn off top spine line
    ax.spines["right"].set_visible(False) #turn off right spine linw
    ax.tick_params(axis="both",top="off",right="off") # turn off top and right ticks

    drawArrowheadedAxis(ax, "bottom") # add bottom x axis with arrow
    drawArrowheadedAxis(ax, "left") # add left y axis with arrow
    plt.show()

if __name__ == "__main__":
    test()
