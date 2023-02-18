from PIL import Image


def visual_multi_img(img_files, title_list, row, col, figsize=(10, 10)):
    fig = plt.figure(figsize=figsize)
    for i, img in enumerate(img_files):
        img = Image.open(img_files[i])
        ax = fig.add_subplot(row, col, i+1)
        ax.imshow(img)
        ax.set_title(title_list[i])
        ax.axis('off')
