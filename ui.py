from logic import logic_time
from database import Foundation, Original_Image, Duplicate_Image, Misc_file
from scans import scan_for_media

def main():
    print("User interface: hello! Let's start :3")

    # Functions: logic and scans
    logic_magic:logic_time = logic_time()
    scanned_goods:scan_for_media = scan_for_media()

    # Database objects
    

    scanned_goods.find_media()
    scanned_goods.debug_print_lists()

    logic_magic.createRange(starting_point=38, end = 44)
    print(logic_magic.desired_range)

    for index, number in enumerate(scanned_goods.medias_only_numbers):
        print(f"Index #{index}: {number}") # Test


if __name__ == '__main__':
    main()