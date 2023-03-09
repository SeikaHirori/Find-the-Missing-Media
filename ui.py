from logic import Create_Range, Sorting_items
from database import Foundation, Original_Image, Duplicate_Image, Misc_file, Selected_Range, Scanned, Missing_Images
from scans import scan_for_media

def main():
    print("User interface: hello! Let's start :3")

    # Functions: logic and scans
    logic_magic:Create_Range = Create_Range()
    scanned_goods:scan_for_media = scan_for_media()

    # Database objects
    

    db_scanned:Scanned = Scanned()

    db_original_img: Original_Image = Original_Image()
    db_duplicate_img: Duplicate_Image = Duplicate_Image()
    db_misc_file: Misc_file = Misc_file()
    db_missing_IMG: Missing_Images = Missing_Images()
    print(f"Spreadsheet type: {db_duplicate_img.show_spreadsheet_type()}")
    
    scanned_goods.find_media(db_scanned=db_scanned)
    # scanned_goods.debug_print_lists()

    desired_range:list[str] = logic_magic.createRange(starting_point=38, end = 44)

    db_range:Selected_Range = Selected_Range()
    db_range.add_to_database(desired_range)
    # db_range.debug_print_all_lists()

    db_scanned.import_list_of_dict(scanned_goods.export_list_of_dict())
    # db_scanned.debug_print_all_lists()

    sorting_goods: Sorting_items = Sorting_items()
    sorting_goods.hello_world()
    sorting_goods.action(db_range=db_range, db_scanned=db_scanned, db_original_img=db_original_img, db_misc_file=db_misc_file, db_missing_IMG=db_missing_IMG)

if __name__ == '__main__':
    main()