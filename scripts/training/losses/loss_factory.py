class LossFactory:
    """This class provides a static method to instantiate the losses by their name."""
    @staticmethod
    def get_loss(name: str):
        """
        Returns the class of the loss with the input name.
        :param name: the name of the loss.
        :return: the loss class.
        """
        if name == "loss 0":
            pass # TODO: return loss class here
        elif name == "loss 1":
            pass # TODO: return loss class here

        # Return None if no class corresponds
        return None