import os

class Epoch:
    """
    This class is the epoch of a training identified with an index and containing a list of results.
    """
    def __init__(self, index, results):
        """
        Initialize the epoch with its results.
        :param index: The index of the epoch.
        :param results: A list of results.
        """
        self.index = index
        self.results = results

    def get_string(self, delimiter = "\n", only_numeric = True):
        """
        Logs the current epoch.
        :param delimiter: the delimiter of the metric values.
        :return: a string with the results.
        """
        output = f">>> Epoch {self.index}\n"
        for result in self.results:
            # Skip non-numeric results
            if only_numeric and not result.is_numeric():
                continue
            # Add results to the output
            output += f"{result.metric}: {result.value}{delimiter}"

        return output

class History:
    """
    This class is a history of epochs for a training.
    """
    def __init__(self):
        """
        Initialize the history.
        """
        self.epochs = []

    def append_epoch(self, epoch):
        """
        Append the epoch to the history.
        :param epoch: the epoch to append.
        :return: void.
        """
        self.epochs.append(epoch)

    def save(self, path):
        """
        Save the history at a path.
        :param path: the path to save the history at.
        :return: void.
        """
        # Create history path
        history_path = path
        if not os.path.exists(history_path):
            try:
                os.mkdir(history_path)
            except:
                raise IOError(f"Cannot create history path {history_path}")

        # Create first row with numeric metrics name
        numeric_results_csv = "index"
        for result in self.epochs[0].results:
            if result.is_numeric():
                numeric_results_csv += "," + str(result.metric)
        numeric_results_csv += "\n"

        # For each epoch
        for epoch in self.epochs:
            # Initialize the row string
            row = str(epoch.index)

            # For each result...
            for result in epoch.results:
                # ... if the result is numeric add it to the csv
                if result.is_numeric():
                    row += "," + str(result.value)
                # ... else save the result in a folder name as the index of the epoch inside the history folder
                else:
                    epoch_path = os.path.join(history_path, str(epoch.index))
                    if not os.path.exists(epoch_path):
                        try:
                            os.mkdir(epoch_path)
                        except:
                            raise IOError(f"Cannot create epoch path {epoch_path}")
                    result.save(epoch_path)

            # Finally add the row for this epoch to the csv
            numeric_results_csv += row + "\n"

        with open(os.path.join(history_path, "history.csv"), "w+") as f:
            f.write(numeric_results_csv)

