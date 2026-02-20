import sys
import traceback


class ProjectException(Exception):
    """
    Custom exception class that shows
    file name and line number of the error.
    """

    def __init__(self, error_message: str):
        super().__init__(error_message)

        # Get current exception details
        exc_type, exc_value, exc_tb = sys.exc_info()

        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
        else:
            file_name = "Unknown"
            line_number = "Unknown"

        self.error_message = (
            f"\nError occurred in file: {file_name}"
            f"\nLine number: {line_number}"
            f"\nError message: {error_message}"
        )

    def __str__(self):
        return self.error_message