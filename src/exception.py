import sys


def error_message(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    return f"""
Error:
{str(error)}

File:
{exc_tb.tb_frame.f_code.co_filename if exc_tb else 'Unknown file'}

Line:
{exc_tb.tb_lineno if exc_tb else 'Unknown line'}
"""


class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error, error_detail=sys):
        _, _, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown file"
        line_no = exc_tb.tb_lineno if exc_tb else "Unknown line"
        return f"Error:\n{str(error)}\n\nFile:\n{filename}\n\nLine:\n{line_no}"

    def __str__(self):
        return self.error_message
