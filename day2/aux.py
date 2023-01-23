import numpy as np
import visdom
import torch
import torchvision
import matplotlib.pyplot as plt
from torch.autograd import Variable


def create_plot_window(vis, xlabel, ylabel, title):
    return vis.line(X=np.array([1]), Y=np.array([np.nan]), opts=dict(xlabel=xlabel, ylabel=ylabel, title=title))

def imshow(img):
    npimg = img.cpu().numpy()
    plt.axis('off')
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()
    
def get_torch_vars(x):
    if torch.cuda.is_available():
        x = x.cuda()
    return Variable(x)