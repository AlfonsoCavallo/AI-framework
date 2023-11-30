import os.path

def create_experiment_path(exp_name: str):
    """
    Create the experiment path.
    :param exp_name: the name of the experiment.
    :return: the path of the experiment
    """
    path = os.path.join("experiments", exp_name)
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            raise IOError(f"Cannot create path {path}")

    return path

def get_experiment_path(exp_name: str):
    """
    Return the experiment path.
    :param exp_name: the name of the experiment.
    :return: the path of the experiment
    """
    return os.path.join("experiments", exp_name)

def is_numeric(value):
    """
    Check if a value is numeric.
    :param value: the value to check.
    :return: True if its float or int, False otherwise.
    """
    return type(value) == float or type(value) == int