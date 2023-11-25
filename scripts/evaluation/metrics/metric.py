import sys
sys.path.append('../../..')

from scripts.utils.utils import is_numeric

class Result:
    """
    This class is a result of a metric computation.
    """
    def __init__(self, metric, value):
        """
        Initialize the result.
        :param metric: the metric that computed the value.
        :param value: the result of the computation.
        """
        self.metric = metric
        self.value = value

    def save(self, path):
        """
        Saves the result.
        :param path: the path to save the result at.
        :return: void.
        """
        self.metric.save(self.value, path)

    def is_numeric(self):
        """
        Check if the result is numeric.
        :return: True if its numeric, False otherwise.
        """
        return is_numeric(self.value)


class Metric:
    """This class calculates a metric results."""
    def __init__(self, name):
        """
        Initialize the metric.
        :param name: name of the metric that will appear in files.
        :return: the instance.
        """
        self.name = name

    def compute(self, params):
        """
        Compute the metric value and return it as a result.
        :param params: the inputs required by the metric to compute the result.
        :return: the result.
        """
        # TODO: the metric implementation goes here
        return

    def save(self, result, path):
        """
        Saves the result computed by this metric
        :param result: the result to save.
        :param path: the path to save the result at.
        :return: void
        """
        pass # TODO: save code here

    def __str__(self):
        """
        :return: Return the name of the metric.
        This can be edited to manipulate the metric's name according to its parameters
        """
        return self.name

    def __repr__(self):
        """
        :return: Return the name of the metric.
        This can be edited to manipulate the metric's name according to its parameters
        """
        return self.name

