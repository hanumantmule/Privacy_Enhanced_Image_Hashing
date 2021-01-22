import matplotlib.pyplot as plt


def plot_graph(x, y, x_label, y_label, title,image_name):
    file_path='../Result Data/'
    fig, ax = plt.subplots() # fig : figure object, ax : Axes object
    ax.plot(x, y,marker='o', color='b')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    # function to show the plot
    plt.savefig(file_path+image_name)

# plot_graph(x,y,'X','Y','Compression Graph')
