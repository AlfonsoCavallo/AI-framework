import abc

class Model(abc.ABC):
    """
    Interface that includes all the method an ML model should implement.
    """
    def __init__(self, name: str):
        """
        Initialize the model.
        :param name: the model name.
        :return: void.
        """
        self.name = name

    @abc.abstractmethod
    def forward(self, x):
        """
        Propagate the input through the model.
        :param x: the input data.
        :return: the model's output.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def inference_forward(self, x):
        """
        Propagate the input through the model at inference time. If not implemented it calls the forward method.
        :param x: the input data.
        :return: the model's output.
        """
        return self.forward(x)

    @abc.abstractmethod
    def reset_parameters(self):
        """
        Initializes the model parameters randomly.
        :return: void.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    @abc.abstractmethod
    def save(self, path):
        """
        Save the model into a file.
        :param path: the path of the file.
        :return: void.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    @abc.abstractmethod
    def load(self, path):
        """
        Load model from file.
        :param path: the path of the file.
        :return: void.
        """
        raise NotImplementedError("Subclasses should implement this method.")
