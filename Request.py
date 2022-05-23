class Request:
    """
    Class representation of a Request.
    """
    def __init__(self):
        """
        Initializer for the Request.
        """
        self.mode = None
        self.data_input = None
        self.input_file = None
        self.expanded = None
        self.output = None

    def __str__(self):
        """
        String representation of Request.
        :return: str
        """
        return f"---Request---: Mode: {self.mode}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Expanded: {self.expanded}, " \
               f"Output: {self.output}"
