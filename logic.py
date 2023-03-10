from database import *
from dissect import *

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

    def action(self, db_range:Selected_Range, db_scanned:Scanned, db_original_img: Original_Image, db_misc_file: Misc_file, db_duplicate_img:Duplicate_Image, db_missing_IMG: Missing_Images) -> None:

        while not db_scanned.is_empty():
            current_item: dict = db_scanned.pop_front_file_dict()

            f_number: str = dissect_numbers(item_dict=current_item)
            f_duplicate: bool = dissect_duplicate(item_dict=current_item)
            f_is_it_IMG:bool = dissect_is_it_IMG(item_dict=current_item)

            if not f_is_it_IMG:
                db_misc_file.add_dict_to_database(current_item)
            elif f_duplicate: # Puts duplicate item into duplicate spreadshhet immediately
                db_duplicate_img.add_dict_to_database(current_item)
            elif f_number in db_range.db_numbers:
                index = db_range.db_numbers.index(f_number)
                db_range.db_numbers.pop(index)

                db_original_img.add_dict_to_database(current_item)
            else:
                db_misc_file.add_dict_to_database(current_item)

        if not db_range.is_empty():
            '''
                If there are numbers still within range.
            '''
            for number in db_range.export_remaining_numbers():
                db_missing_IMG.add_all_values_to_database(numbers=number)

        db_range.debug_print_all_lists()
        db_scanned.debug_print_all_lists()
        db_original_img.debug_print_all_lists()
        db_misc_file.debug_print_all_lists()
        db_duplicate_img.debug_print_all_lists()
        db_missing_IMG.debug_print_all_lists()




