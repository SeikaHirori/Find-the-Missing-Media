from logic import Create_Range, Sorting_items
from database import Foundation, Original_Image, Duplicate_Image, Misc_file, Selected_Range, Scanned, Missing_Images
from scans import scan_for_media

def main():
    print("User interface: hello! Let's start :3")

    print("Let's get the range! Range should be between 0 to 1000")
    template_type_and_enter:str = "Type the number, then press the Enter key :3"

    starting_point:int = int_user_input(f"What's the starting point? {template_type_and_enter}")
    
    ending_point:int = None
    while True:
        ending_point = int_user_input(f"What's the ending point? {template_type_and_enter}")

        if ending_point >= starting_point:
            break

        print()
        print(f"The ending point '{ending_point}' should be greater than or equal to '{starting_point}'")



    # Functions: logic and scans
    logic_magic:Create_Range = Create_Range()
    scanned_goods:scan_for_media = scan_for_media()

    # Database objects
    db_scanned:Scanned = Scanned()
    db_original_img: Original_Image = Original_Image()
    db_duplicate_img: Duplicate_Image = Duplicate_Image()
    db_misc_file: Misc_file = Misc_file()
    db_missing_IMG: Missing_Images = Missing_Images()
    
    scanned_goods.find_media(db_scanned=db_scanned)

    desired_range:list[str] = logic_magic.createRange(starting_point=starting_point, end = ending_point)

    db_range:Selected_Range = Selected_Range()
    db_range.add_to_database(desired_range)

    db_scanned.import_list_of_dict(scanned_goods.export_list_of_dict())

    sorting_goods: Sorting_items = Sorting_items()


    sorting_goods.action(db_range=db_range, db_scanned=db_scanned, db_original_img=db_original_img, db_misc_file=db_misc_file, db_missing_IMG=db_missing_IMG, db_duplicate_img=db_duplicate_img)

    print(f"Program finished!")

def int_user_input(prompt: str) -> int:
    prompt += "\n"
    output:int = None

    while True:
        try:
            print()
            output = int(input(prompt))

            if output < 0:
                print("Value is too small.")
            elif output > 1000:
                print("Value is too big")
            else:
                break
        except ValueError:
            print("Please input valid number!")


    return output

if __name__ == '__main__':
    main()