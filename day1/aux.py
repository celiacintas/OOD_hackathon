import matplotlib.pyplot as plt

## Auxiliary functions for the ipynb

def show_samples(images, groundtruth):
    """
    Show examples of ISIC 2019 along with
    condition classification.
    Input: paths, labels
    Output: grid images
    """

    f, axarr = plt.subplots(3, 4)
    f.suptitle("Samples from ISIC 2019")
    curr_row = 0
    for index, name in enumerate(images[:12]):
        # print(name.stem)
        a = plt.imread(name)
        # find the column by taking the current index modulo 3
        col = index % 3
        # plot on relevant subplot
        axarr[col, curr_row].imshow(a)
        axarr[col, curr_row].text(
            5,
            5,
            str(groundtruth.loc[name.stem].idxmax(axis=0)),
            bbox={"facecolor": "white"},
        )
        if col == 2:
            curr_row += 1

    f.tight_layout()
    return f

def plot_pca(X_pca, y):
    """
    plot a 2D PCA for OOD samples
    """
    plt.figure()
    colors = ["navy", "turquoise", "darkorange"]
    lw = 2

    for color, i, target_name in zip(colors, [0, 1], ["inliers", "outliers"]):
        plt.scatter(
            X_pca[y == i, 0], X_pca[y == i, 1], color=color, alpha=0.5, lw=lw, label=target_name
        )
    plt.legend(loc="best", shadow=False, scatterpoints=1)
    plt.title("PCA of ISIC2019 dataset")
