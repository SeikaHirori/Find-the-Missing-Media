from enum import Enum
from dissect import *
import xlsxwriter

class Spreadsheet_variant(Enum):
    foundation = "Foundation"
    scanned = "Scanned file"
    missing_Image = "Missing media"
    original_Image = "Original Image"
    duplicate_image = "Duplicate Image"
    misc_file = "Misc File"
    desired_range = "Desired range"

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

    def add_all_values_to_database(self, file_name: str, stem: str, suffixes: list[str], is_IMG: bool, numbers: str, duplicate: bool):
        # This is here for debug
        # self.db_file_name.append(file_name)
        # self.db_stem.append(stem)
        # self.db_suffixes.append(suffixes)
        self.db_is_it_IMG.append(is_IMG)
        self.db_numbers.append(numbers)
        self.db_duplicate.append(duplicate)

        new_dict_item: dict = self.create_dict(file_name=file_name, stem=stem, suffixes=suffixes, is_IMG=is_IMG, numbers=numbers, duplicate=duplicate)
        self.db_dict_items.append(new_dict_item)

    def add_dict_to_database(self, item_dict:dict) -> None:
        self.db_dict_items.append(item_dict)

        file_name: str = dissect_file_name(item_dict=item_dict)
        stem:str = dissect_stem(item_dict=item_dict)
        suffixes:list[str] = dissect_suffixes(item_dict=item_dict)
        numbers:str = dissect_numbers(item_dict=item_dict)
        is_IMG:bool = dissect_is_it_IMG(item_dict=item_dict)
        duplicate:bool = dissect_duplicate(item_dict=item_dict)

        self.db_file_name.append(file_name)
        self.db_stem.append(stem)
        self.db_suffixes.append(suffixes)
        self.db_is_it_IMG.append(is_IMG)
        self.db_numbers.append(numbers)
        self.db_duplicate.append(duplicate)




    def __dissect_inbound_list(self, inbound_list: list[list[str, str, list[str], bool, str, bool]]):
        pass

        self.add_to_database()
    
    def show_spreadsheet_type(self) -> str:
        return self.spreadsheet_type.value
    
    def size(self) -> int:
        return len(self.db_dict_items)
    
    def is_empty(self) -> bool:
        return self.size() == 0

    def check_first_item(self) -> dict:
        return self.db_dict_items[0]

    def check_last_item(self) -> dict:
        return self.db_dict_items[-1]

    def is_inbound_number_in_list(self, inbound_number:str):
        raise NotImplementedError


    def __pop_individual_items_at_position(self, pos: int) -> list[list[str, str, list[str], bool, str, bool]]:
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

    def __pop_last(self) -> list[list[str, str, list[str], bool, str, bool]]:
        position: int = -1
        output:list[list[str, str, list[str], bool, str, bool]] = self.pop_items_at_position(pos=position)

        return output
    
    def __pop_front_create_from_list_and_export_as_new_dict(self, inbound_pop_front_list: list[list[str, str, list[str], bool, str, bool]]) -> dict:
        """Create dict from list by popping first item.

        Args:
            inbound_pop_front_list (list[list[str, str, list[str], bool, str, bool]]): _description_

        Returns:
            dict: _description_
        """
        file_name: str = inbound_pop_front_list.pop(0)
        stem:str = inbound_pop_front_list.pop(0)
        suffixes: list[str] = inbound_pop_front_list.pop(0)
        is_IMG:bool = inbound_pop_front_list.pop(0)
        numbers:str = inbound_pop_front_list.pop(0)
        duplicate:bool = inbound_pop_front_list.pop(0)

        output: dict = self.create_dict(file_name=file_name, stem=stem, suffixes=suffixes, is_IMG=is_IMG, numbers=numbers, duplicate=duplicate)

        return

    def pop_front_file_dict(self) -> dict: # USE THIS
        """Extract only one dict item, but also delete values at front of list.

        Returns:
            dict: _description_
        """
        position = 0
        output: dict = self.db_dict_items.pop(position)

        # self.__delete_item_at_position(position=position)


        return output

    def __pop_front_only_numbers(self) -> str:
        position = 0
        return self.db_numbers.pop(position)

    def __delete_item_at_position(self, position: int):
        del self.db_file_name[position]
        del self.db_stem[position]
        del self.db_suffixes[position]
        del self.db_is_it_IMG[position]
        del self.db_numbers[position]
        del self.db_duplicate[position]

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
        
        raise NotImplementedError

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

    def add_dict_to_database(self, item_dict: dict) -> None:
        return super().add_dict_to_database(item_dict)

    def add_all_values_to_database(self, numbers: str, file_name: str=None, stem: str=None, suffixes: list[str]=None, is_IMG: bool=None, duplicate: bool=None):
        return super().add_all_values_to_database(file_name, stem, suffixes, is_IMG, numbers, duplicate)

    
    def debug_print_all_lists(self):
        print()
        self.debug_print_look_down_here()
        print("--- debug print all instance lists ;3 ---")
        self.debug_current_class_type()

        output_display:str = f'''
        Missing Numbers: {self.db_numbers}

        - Dict: {self.db_dict_items}

        - Current size: {self.size()}
        '''
        print(output_display)

        self.debug_print_look_up_here()

class Misc_file(Foundation):

    spreadsheet_type: Spreadsheet_variant = Spreadsheet_variant.misc_file

    def __init__(self) -> None:
        super().__init__()

class Selected_Range(Foundation):
    """Contains selected range only

    Args:
        Foundation (_type_): _description_
    """

    spreadsheet_type:Spreadsheet_variant = Spreadsheet_variant.desired_range

    def __init__(self) -> None:
        self.db_numbers:list[str ]= []
    
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

    def save_to_xlsx(self):
        header_columns: list[str] = [
            "Missing Numbers",
        ]
        header:str = ",".join(header_columns)
        
        raise NotImplementedError

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