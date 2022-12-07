from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def cal_PCA(df):
    """
    Description
    -----------
    Calculate PCA from input dataframe
    Parameters
    ----------
        df :
    Returns
    -------
        pca :
        reduced :
    """
    pca = PCA(n_components = 0.95)
    pca.fit(df)
    reduced = pca.transform(df)
    return pca, reduced

def plot_cumulative_var(pca, name):
    """
    Description
    -----------
    Plot cumulative variable from pca
    Parameters
    ----------
        pca :
        name :
    Returns
    -------
        show plot
    """
    fig, ax = plt.subplots()
    xi = np.arange(1, len(pca.explained_variance_ratio_)+1, step=1)
    y = np.cumsum(pca.explained_variance_ratio_)

    plt.ylim(0.0,1.1)
    plt.plot(xi, y, marker='o', linestyle='--', color='b')

    plt.xlabel('Number of Components')
    plt.xticks(np.arange(0, len(pca.explained_variance_ratio_), step=int(len(pca.explained_variance_ratio_)/10))) #change from 0-based array index to 1-based human-readable label
    plt.ylabel('Cumulative variance (%)')
    plt.title('The number of components needed to explain variance '+ name)

    plt.axhline(y=0.95, color='r', linestyle='-')
    plt.text(0.5, 0.85, '95% cut-off threshold', color = 'red', fontsize=16)

    ax.grid(axis='x')
    plt.show()