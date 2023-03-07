import logic
from scans import scan_for_media

if __name__ == '__main__':
    logic.run_experiments()
    print("------")
    scanned_media: scan_for_media() = scan_for_media()
    scanned_media.find_media() 
    scanned_media.debug_print_lists()