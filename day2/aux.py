import numpy as np
import visdom
import torch
import torchvision
import matplotlib.pyplot as plt
from torch.autograd import Variable


# ===== Visualization Helpers =====
def create_plot_window(vis, xlabel, ylabel, title):
    return vis.line(
        X=np.array([1]),
        Y=np.array([np.nan]),
        opts=dict(xlabel=xlabel, ylabel=ylabel, title=title),
    )


def imshow(img):
    npimg = img.cpu().numpy()
    plt.axis("off")
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


def plot_re(groups, threshold_fixed):
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(
            group.index,
            group.re,
            marker="o",
            ms=3.5,
            linestyle="",
            label="IND" if name == 1 else "OOD",
        )
    ax.hlines(
        threshold_fixed,
        ax.get_xlim()[0],
        ax.get_xlim()[1],
        colors="r",
        zorder=100,
        label="Threshold",
    )
    ax.legend()
    plt.title(
        "Reconstruction error for in-distribution and out-of-distribution samples"
    )
    plt.ylabel("Reconstruction error")
    plt.xlabel("Data point index")
    plt.show()


# ===== PyTorch Helpers =====
def get_torch_vars(x):
    if torch.cuda.is_available():
        x = x.cuda()
    return Variable(x)
