from datetime import datetime
from dissect import *
from enum import Enum
from pathlib import Path
import xlsxwriter

class Spreadsheet_variant(Enum):
    foundation = "foundation"
    scanned = "scanned_file"
    missing_Image = "missing_media"
    original_Image = "original_image"
    duplicate_image = "duplicate_image"
    misc_file = "misc_file"
    desired_range = "desired_range"

class Subdirectory_variant(Enum):
    foundation = "Foundation"
    scanned = "Scanned_file"
    missing_Image = "Missing_media"
    original_Image = "Original_Image"
    duplicate_image = "Duplicate_Image"
    misc_file = "Misc_File"
    desired_range = "Desired_range"

class Foundation:

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.foundation
    subdirectory_type: Subdirectory_variant = Subdirectory_variant.foundation

    excel_path: str = "_excel"

    def __init__(self) -> None:
        # self.files: list[list[str, str, list[str], bool,str, bool]] = []


        self.db_file_name: list[str] = []
        self.db_stem: list[str] = []
        self.db_suffixes: list[list[str]] = []
        self.db_relative_paths: list[str] = []

        self.db_is_it_IMG: list[bool] = []
        self.db_numbers: list[str] = []
        self.db_duplicate: list[bool] = []

        self.db_dict_items: list[dict] = []
    
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

        self.db_dict_items
        # self.files
        
        pass

    def import_list_of_dict(self, inbound_list_of_dict:list[dict]) -> None:
        self.db_dict_items = inbound_list_of_dict

    def add_all_values_to_database(self, numbers: str, file_name: str = None, stem: str = None, suffixes: list[str] = None, relative_path:str = None, is_IMG: bool = None, duplicate: bool = None):


        # This is here for debug
        # self.db_file_name.append(file_name)
        # self.db_stem.append(stem)
        # self.db_suffixes.append(suffixes)
        self.db_is_it_IMG.append(is_IMG)
        self.db_numbers.append(numbers)

        self.db_duplicate.append(duplicate)

        new_dict_item: dict = self.create_dict(file_name=file_name, stem=stem, suffixes=suffixes, relative_path=relative_path, is_IMG=is_IMG, numbers=numbers, duplicate=duplicate)

        self.db_dict_items.append(new_dict_item)

    def add_dict_to_database(self, item_dict:dict) -> None:
        self.db_dict_items.append(item_dict)

        file_name: str = dissect_file_name(item_dict=item_dict)
        stem:str = dissect_stem(item_dict=item_dict)
        suffixes:list[str] = dissect_suffixes(item_dict=item_dict)
        relative_path:str = dissect_relative_path(item_dict=item_dict)
        numbers:str = dissect_numbers(item_dict=item_dict)
        is_IMG:bool = dissect_is_it_IMG(item_dict=item_dict)
        duplicate:bool = dissect_duplicate(item_dict=item_dict)

        self.db_file_name.append(file_name)
        self.db_stem.append(stem)
        self.db_suffixes.append(suffixes)
        self.db_relative_paths.append(relative_path)
        self.db_is_it_IMG.append(is_IMG)
        self.db_numbers.append(numbers)
        self.db_duplicate.append(duplicate)

    
    def show_spreadsheet_type(self) -> str:
        return self.spreadsheet_type.value
    
    def show_subdirectory(self) -> str:
        return self.subdirectory_type.value



    def size(self) -> int:
        return len(self.db_dict_items)
    
    def is_empty(self) -> bool:
        return self.size() == 0

    def check_first_item(self) -> dict:
        return self.db_dict_items[0]

    def check_last_item(self) -> dict:
        return self.db_dict_items[-1]


    def pop_front_item_list(self) -> list[list[str, str, list[str], bool, str, bool]]:
        position: int = 0
        output:list[list[str, str, list[str], bool, str, bool]] = self.pop_items_at_position(pos=position)

        return output


    def pop_front_file_dict(self) -> dict: # USE THIS
        """Extract only one dict item, but also delete values at front of list.

        Returns:
            dict: _description_
        """
        position = 0
        output: dict = self.db_dict_items.pop(position)

        # self.__delete_item_at_position(position=position)


        return output

    def create_dict(self, numbers: str, file_name: str = None, stem: str = None, suffixes: list[str] = None, relative_path:str = None, is_IMG: bool = None, duplicate: bool = None) -> dict:
        the_goods:dict = {}

        the_goods["file name"] = file_name
        the_goods["stem"] = stem
        the_goods["suffixes"] = suffixes
        the_goods["relative_path"] = relative_path
        the_goods["is_it_IMG"] = is_IMG
        the_goods["numbers"] = numbers
        the_goods["duplicates"] = duplicate

        return the_goods

    def create_subdirectory(self) -> None:
        #TODO
        subdirectory: str = f"{self.excel_path}/{self.subdirectory_type.value}/"

        print(f"Checking if subdirectory '{subdirectory}' exists")
        p = Path(f"{subdirectory}")
        if p.exists():
            print("It exists!")
        else:
            print("It doesn't exist, so let's make it!")

        p.mkdir(exist_ok=True)

    def create_excel_directory(self) -> None:
        # TODO - check if _excel folder exists
        p = Path(f"{self.excel_path}")


        p.mkdir(exist_ok=True)

    def save_to_xlsx(self):
        # TODO
        headers_column: list[str] = [
            "file name", 
            "stem", 
            "suffixes", 
            "relative path",
            "is_it_IMG?",
            "numbers", 
            "duplicates", 
            "Note",
        ]
        # header: str = ",".join(headers_column)

        self.create_excel_directory()
        self.create_subdirectory()

        spreadsheet_name:str = self.show_spreadsheet_type()
        folder_name:str = self.show_subdirectory()
        date = datetime.now()

        # RFER #3
        workbook:xlsxwriter.Workbook = xlsxwriter.Workbook(f"_excel/{folder_name}/{spreadsheet_name}___{date}.xlsx")
        worksheet = workbook.add_worksheet()

        for index, head in enumerate(headers_column):
            # print(f"Index #{index}: {head}")
            worksheet.write(0, index, head)

        row:int = 1
        col:int = 0

        for current_dict in self.db_dict_items:
            file_name:str = dissect_file_name(current_dict)
            stem:str = dissect_stem(current_dict)

            suffixes: list[str] = dissect_suffixes(current_dict)
            # combined_suffixes:str = None
            # if suffixes is not None:
            #     if len(suffixes) != 0:
            #         combined_suffixes = ", ".join(suffixes)
            combined_suffixes:str = convert_suffixes_to_str(suffixes)

            relative_path:str = dissect_relative_path(current_dict)

            is_it_IMG:bool = dissect_is_it_IMG(current_dict)
            numbers:str = dissect_numbers(current_dict) or "N/A" # RFER #4
            duplicate:bool = dissect_duplicate(current_dict)

            worksheet.write(row, col, file_name)
            worksheet.write(row, col + 1, stem)
            worksheet.write(row, col + 2, combined_suffixes)
            worksheet.write(row, col + 3, relative_path)

            worksheet.write(row, col + 4, is_it_IMG)
            worksheet.write(row, col + 5, numbers)
            worksheet.write(row, col + 6, duplicate)


            row += 1

        workbook.close()




    def create_row_for_xlsx(self):
        raise NotImplementedError

    def debug_print_all_lists(self):
        print()
        self.debug_print_look_down_here()
        print("--- debug print all instance lists ;3 ---")
        self.debug_current_class_type()

        output_display:str = f'''
        File names: {self.db_file_name}
        Stems: {self.db_stem}
        Suffixes: {self.db_suffixes}
        Is it IMG?: {self.db_is_it_IMG}
        Numbers: {self.db_numbers}
        Duplidate?: {self.db_duplicate}

        - Dict: {self.db_dict_items}

        - Current size: {self.size()}
        '''
        print(output_display)

        self.debug_print_look_up_here()

    def debug_print_look_down_here(self):
        print("--- Look down here :3 --- \n")

    def debug_print_look_up_here(self):
        print("\n--- Look up here :3 ---\n")

    def debug_current_class_type(self) -> None:
        output:str = f'''
        Current class type:
        - {self.show_spreadsheet_type()}
        '''
        
        print(output)
    

class Scanned(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.scanned
    subdirectory_type:Subdirectory_variant = Subdirectory_variant.scanned

    def __init__(self) -> None:
        super().__init__()

class Original_Image(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.original_Image
    subdirectory_type: Subdirectory_variant = Subdirectory_variant.original_Image


    def __init__(self) -> None:
        super().__init__()


class Duplicate_Image(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.duplicate_image

    subdirectory_type:Subdirectory_variant = Subdirectory_variant.duplicate_image

    def __init__(self) -> None:
        super().__init__()

class Missing_Images(Foundation):
    
    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.missing_Image

    subdirectory_type:Subdirectory_variant = Subdirectory_variant.missing_Image

    def __init__(self) -> None:
        super().__init__()

    def add_all_values_to_database(self, numbers: str, file_name: str = None, stem: str = None, suffixes: list[str] = None, relative_path: str = None, is_IMG: bool = None, duplicate: bool = None):
        return super().add_all_values_to_database(numbers, file_name, stem, suffixes, relative_path, is_IMG, duplicate)


    def debug_print_all_lists(self):
        print()
        self.debug_print_look_down_here()
        print("--- debug print all instance lists ;3 ---")
        self.debug_current_class_type()

        output_display:str = f'''
        Missing IMG numbers: {self.db_numbers}

        - Current size: {self.size()}
        '''
        print(output_display)

        self.debug_print_look_up_here()

class Misc_file(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.misc_file

    subdirectory_type:Subdirectory_variant = Subdirectory_variant.misc_file

    def __init__(self) -> None:
        super().__init__()

class Selected_Range(Foundation):
    """Contains selected range only

    Args:
        Foundation (_type_): _description_
    """

    spreadsheet_type:Spreadsheet_variant = Spreadsheet_variant.desired_range
    subdirectory_type:Subdirectory_variant = Subdirectory_variant.desired_range

    def __init__(self) -> None:
        super().__init__()
    
    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self.db_numbers)

    def add_to_database(self, range: list[str]):
        self.db_numbers = range
    
    def export_remaining_numbers(self) -> list[str]:
        output:list[str] = self.db_numbers

        self.db_numbers = []

        return output

    # def save_to_xlsx(self):
    #     header_columns: list[str] = [
    #         "Missing Numbers",
    #     ]
    #     header:str = ",".join(header_columns)
        
    #     raise NotImplementedError

    def create_row_for_xlsx(self):
        raise NotImplementedError

    def debug_print_all_lists(self):
        print()
        self.debug_print_look_down_here()

        class_name: str = '*Selected_Range'
        numbers_list:str = f"Numbers: {self.db_numbers}"
        list_size:str = f"Size: {self.size()}"

        output_print:str = f'''Class: 
            {class_name}

            {numbers_list}
            {list_size}
        '''

        print(output_print)
        self.debug_print_look_up_here()