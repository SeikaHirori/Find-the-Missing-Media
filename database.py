from enum import Enum
import xlsxwriter

class Spreadsheet_variant(Enum):
    foundation = "Foundation"
    original_Image = "Original Image"
    duplicate_image = "Duplicate Image"
    misc_file = "Misc File"

class Foundation:

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.foundation

    def __init__(self) -> None:
        self.files: list[list[str, str, list[str], str, bool]] = []

    def add_to_database(self, file_name: str, stem: str, suffixes: list[str], numbers: str, duplicate: bool):
        item: list[list[str, str, list[str], str, bool]] = [
            file_name, 
            stem, 
            suffixes, 
            numbers, 
            duplicate,
        ]


        self.files.append(item)
    
    def save_to_xlsx():
        # TODO
        headers_column: list[str] = [
            "file name", 
            "stem", 
            "suffixes", 
            "numbers", 
            "duplicates", 
            "Note:",
        ]
        header: str = ",".join(headers_column)
        pass 

class Original_Image(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.original_Image

    def __init__(self) -> None:
        super().__init__()


class Duplicate_Image(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.duplicate_image

    def __init__(self) -> None:
        super().__init__()

class Misc_file(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.misc_file

    def __init__(self) -> None:
        super().__init__()