from enum import Enum
import xlsxwriter

class Spreadsheet_variant(Enum):
    foundation = "Foundation"
    scanned = "Scanned file"
    missing_Image = "Missing media"
    original_Image = "Original Image"
    duplicate_image = "Duplicate Image"
    misc_file = "Misc File"

class Foundation:

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.foundation

    def __init__(self) -> None:
        # self.files: list[list[str, str, list[str], bool,str, bool]] = []


        self.db_file_name: list[str] = []
        self.db_stem: list[str] = []
        self.db_suffixes: list[list[str]] = []

        self.db_is_it_IMG: list[bool] = []
        self.db_numbers: list[str] = []
        self.db_duplicate: list[bool] = []
    
    def __template___Instance_variables(self):
        """ Template as shortcut for instance variables
        """
        pass

        self.db_file_name
        self.db_stem
        self.db_suffixes
        self.db_is_it_IMG
        self.db_numbers
        self.db_duplicate

        # self.files
        
        pass

    def add_to_database(self, file_name: str, stem: str, suffixes: list[str], is_IMG: bool, numbers: str, duplicate: bool):
        self.db_file_name.append(file_name)
        self.db_stem.append(stem)
        self.db_suffixes.append(suffixes)
        self.db_is_it_IMG.append(is_IMG)
        self.db_numbers.append(numbers)
        self.db_duplicate.append(duplicate)
        
        
        # item: list[list[str, str, list[str], bool, str, bool]] = [
        #     file_name, 
        #     stem, 
        #     suffixes, 
        #     is_IMG, 
        #     numbers, 
        #     duplicate,
        # ]
        # self.files.append(item)
    
    def dissect_inbound_list(self, inbound_list: list[list[str, str, list[str], bool, str, bool]]):


        self.add_to_database()
    
    def show_spreadsheet_type(self) -> str:
        return self.spreadsheet_type.value
    
    def size(self) -> int:
        return len(self.db_file_name)
    
    def is_empty(self) -> bool:
        return len(self.db_file_name) == 0

    def pop_items_at_position(self, pos: int) -> list[list[str, str, list[str], bool, str, bool]]:
        item: list[list[str, str, list[str], bool, str, bool]] = [
            self.db_file_name.pop(pos),
            self.db_stem.pop(pos),
            self.db_suffixes.pop(pos),
            self.db_is_it_IMG.pop(pos),
            self.db_numbers.pop(pos),
            self.db_duplicate.pop(pos),
        ]

        return item
    
    def pop_front_item_list(self) -> list[list[str, str, list[str], bool, str, bool]]:
        position: int = 0
        output:list[list[str, str, list[str], bool, str, bool]] = self.pop_items_at_position(pos=position)

        return output

    def pop_last(self) -> list[list[str, str, list[str], bool, str, bool]]:
        position: int = -1
        output:list[list[str, str, list[str], bool, str, bool]] = self.pop_items_at_position(pos=position)

        return output
    
    def pop_front_and_export_as_dict(self, inbound_pop_front_list: list[list[str, str, list[str], bool, str, bool]]) -> dict:
        file_name: str = inbound_pop_front_list.pop(0)
        stem:str = inbound_pop_front_list.pop(0)
        suffixes: list[str] = inbound_pop_front_list.pop(0)
        is_IMG:bool = inbound_pop_front_list.pop(0)
        numbers:str = inbound_pop_front_list.pop(0)
        duplicate:bool = inbound_pop_front_list.pop(0)

        output: dict = self.create_dict(file_name=file_name, stem=stem, suffixes=suffixes, is_IMG=is_IMG, numbers=numbers, duplicate=duplicate)

        return

    def create_dict(self, file_name: str, stem: str, suffixes: list[str], is_IMG: bool, numbers: str, duplicate: bool) -> dict:
        the_goods:dict = {}

        the_goods["file name"] = file_name
        the_goods["stem"] = stem
        the_goods["suffixes"] = suffixes
        the_goods["is_it_IMG?"] = is_IMG
        the_goods["numbers"] = numbers
        the_goods["duplicates"] = duplicate

        return the_goods


    def save_to_xlsx(self):
        # TODO
        headers_column: list[str] = [
            "file name", 
            "stem", 
            "suffixes", 
            "is_it_IMG?",
            "numbers", 
            "duplicates", 
            "Note:",
        ]
        header: str = ",".join(headers_column)
        pass

    def debug_print_all_lists(self):
        print("--- debug print all instance lists ;3 ---")
        print()

        output_display:str = f'''
        File names: {self.db_file_name}
        Stems: {self.db_stem}
        Suffixes: {self.db_suffixes}
        Is it IMG?: {self.db_is_it_IMG}
        {self.db_numbers}
        {self.db_duplicate}
        '''
        print(output_display)

class Scanned(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.scanned

    def __init__(self) -> None:
        super().__init__()

class Original_Image(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.original_Image

    def __init__(self) -> None:
        super().__init__()


class Duplicate_Image(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.duplicate_image

    def __init__(self) -> None:
        super().__init__()

class Missing_Images(Foundation):
    
    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.missing_Image

    def __init__(self) -> None:
        super().__init__()

class Misc_file(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.misc_file

    def __init__(self) -> None:
        super().__init__()