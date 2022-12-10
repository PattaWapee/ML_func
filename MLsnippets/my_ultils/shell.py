import os

def make_dir(dir_name):
    """
    create directory if it is not exist
    Parameters
    ----------
    dir_name : str
        directory name

    Returns
    -------
    print
        "Create directory name $dir_name"

    Raises
    ------
    OtherError
        when an other error
    """
    if not os.path.exists(dir_name):
        print('create new directory name '+ dir_name)
        os.makedirs(dir_name)
    elif os.path.exists(dir_name):
        print(dir_name+ ' already exists')