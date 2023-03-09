from database import *

class Create_Range:

    def __init__(self) -> None:
        self.desired_range: list[str] = []


    def run_experiments(self):
        self.createRange(starting_point=0, end=50)

    def createRange(self, starting_point:int = 0, end:int = 9999) -> list[str]:
        print(f"hello {self.createRange.__name__}")

        # RFER #1
        output_range: list[str] =  ["%04d" % x for x in range(starting_point, end + 1)]

        # print(output_range)
        self.desired_range = output_range
        return output_range
    
    def pop_front(self):
        return self.desired_range.pop(0)
    
    def is_number_in_list(self, number:str) -> bool:
        # Use binary search here
        return #TODO

class Sorting_items:

    def hello_world(self):
        print()
        print("hello mates from Sorting_items class ;3")

    def action(self, db_range:Selected_Range, db_scanned:Scanned, db_original_img: Original_Image, db_misc_file: Misc_file, db_missing_IMG: Missing_Images) -> None:

        for item_scanned in db_scanned.db_dict_items:
            print(item_scanned)

            print(self.dissect_numbers(item_scanned))
    
    def dissect_everything_in_dict(self, item_dict:dict):
        raise NotImplementedError
    
    def dissect_file_name(self, item_dict:dict) -> str:
        the_key:str = "file_name"
        return item_dict[the_key]
    
    def dissect_stem(self, item_dict:dict) -> str:
        the_key:str = "stem"
        return item_dict[the_key]
    
    def dissect_suffixes(self, item_dict:dict) -> list[str]:
        the_key:str = "suffixes"
        return item_dict[the_key]
    
    def dissect_is_it_IMG(self, item_dict:dict) -> bool:
        the_key:str = "is_it_IMG"
        return item_dict[the_key]
    
    def dissect_numbers(self, item_dict:dict) -> str:
        the_key:str = "numbers"
        return item_dict[the_key]
    
    def dissect_duplicate(self, item_dict:dict) -> bool:
        the_key:str = "duplicates"
        return item_dict[the_key]
