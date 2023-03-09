from logic import logic_time
from database import Foundation, Original_Image, Duplicate_Image, Misc_file, Scanned, Missing_Images
from scans import scan_for_media

def main():
    print("User interface: hello! Let's start :3")

    # Functions: logic and scans
    logic_magic:logic_time = logic_time()
    scanned_goods:scan_for_media = scan_for_media()

    # Database objects
    db_original_img: Original_Image = Original_Image()
    db_duplicate_img: Duplicate_Image = Duplicate_Image()
    db_misc_file: Misc_file = Misc_file()
    db_scanned:Scanned = Scanned()
    db_missing_IMG: Missing_Images = Missing_Images()
    print(f"Spreadsheet type: {db_duplicate_img.show_spreadsheet_type()}")

    scanned_goods.find_media(db_scanned=db_scanned)
    # scanned_goods.debug_print_lists()

    select_range:list[str] = logic_magic.createRange(starting_point=38, end = 44)
    print(logic_magic.desired_range)
    print(select_range)

    range_object:Foundation = Foundation()
    range_object.db_numbers = select_range
    print(f"{range_object.__str__}: {range_object.db_numbers}\n")


    test_output = range_object.pop_front_only_numbers()
    print(f"Popped front number only: {test_output}")
    range_object.debug_print_all_lists()
    



if __name__ == '__main__':
    main()