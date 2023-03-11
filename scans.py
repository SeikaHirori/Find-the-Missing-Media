import os
from pathlib import Path, PurePath, PurePosixPath
from database import Scanned

class scan_for_media:
    def __init__(self) -> None:
        self.__class_name:str = "scan_for_media"
        
        self.medias_with_extensions: list[str] = []
        self.medias_only_stem: list[str] = []
        self.medias_suffixes: list[list[str]] = []


        self.medias_only_numbers: list[str] = []
        self.potential_duplicate: list[bool] = []
        self.is_it_IMG:list[bool] = []

        self.files_dict: list[dict] = []



    def find_media(self, db_scanned: Scanned) -> list[dict]:
        
        _pathway_for_media: str = "_media/"
        directory_media:Path = Path(_pathway_for_media)

        if not directory_media.exists():
            # print("IT DOESN'T EXIST :'[")
            return None
        else:
            # print("Folder '_media' exists!") 
            print()
        
        

        files_in_folder = directory_media.glob("**/*")
        files_in_folder = sorted(files_in_folder)
        if len(files_in_folder) <= 0:
            raise NotImplementedError


        for index, file in enumerate(files_in_folder):
            # print(f"current index: {index}")

            f_full_name: str = file.name
            f_suffixes:str = file.suffixes
            f_relative_path:str = str(file)

            f_stem:str = None
            if len(f_suffixes) > 1: 
                f_stem = self.obtain_pure_stem(f_suffixes=f_suffixes, file=file)
            else:
                f_stem = file.stem
            
            # TODO - obtain ONLY numbers from file's string
            dict_is_IMG_and_has_numbers: dict = self.obtain_numbers_from_IMG_file(f_stem=f_stem)
            # print(dict_is_IMG_and_has_numbers)
            f_numbers: str = dict_is_IMG_and_has_numbers["numbers"]

            is_it_IMG:bool = dict_is_IMG_and_has_numbers["is_it_img"]

            is_duplicate: bool = self.is_it_a_duplicate(f_numbers=f_numbers)
            
            pure_numbers:str = None
            if f_numbers is not None:
                pure_numbers_splitter = f_numbers.split(" ")
                pure_numbers = pure_numbers_splitter[0]
            

            new_dict = self.create_dict(file_name=f_full_name, stem=f_stem, suffixes=f_suffixes, relative_path=f_relative_path, is_IMG=is_it_IMG, numbers=pure_numbers, duplicate=is_duplicate)

            self.files_dict.append(new_dict)


    def create_dict(self, file_name: str, stem: str, suffixes: list[str], relative_path:str, is_IMG: bool, numbers: str, duplicate: bool) -> dict:
        the_goods:dict = {}

        the_goods["file name"] = file_name
        the_goods["stem"] = stem
        the_goods["suffixes"] = suffixes
        the_goods["relative_path"] = relative_path
        the_goods["is_it_IMG"] = is_IMG
        the_goods["numbers"] = numbers
        the_goods["duplicates"] = duplicate

        return the_goods
        
    
    def add_to_lists(self, f_full_name: str, f_stem: str, f_suffixes: str, f_numbers:str, is_it_img: bool):
        self.medias_with_extensions.append(f_full_name)
        self.medias_only_stem.append(f_stem)
        self.medias_suffixes.append(f_suffixes)

        is_it_a_possible_duplicate: bool = False
        if f_numbers is not None:
            if len(f_numbers) > 4:
                is_it_a_possible_duplicate = True

                split_f_num: list[str] = f_numbers.split(" ")
                f_numbers = split_f_num[0]
        self.potential_duplicate.append(is_it_a_possible_duplicate)
        self.medias_only_numbers.append(f_numbers)
        self.is_it_IMG.append(is_it_img)

        # print("FINISH ME!\n---")

    def is_it_a_duplicate(self, f_numbers:str) -> dict:
        is_it_a_possible_duplicate: bool = False
        if f_numbers is not None:
            if len(f_numbers) > 4:
                is_it_a_possible_duplicate = True
        
        return is_it_a_possible_duplicate


    def check_number_string_is_greater_than_4(self, f_numbers:str) -> bool:

        if f_numbers is not None:
            if len(f_numbers) > 4:
                split_f_num: list[str] = f_numbers.split(" ")
                f_numbers = split_f_num[0]
                return True
        
        return False

    def obtain_pure_stem(self, f_suffixes:list[str],file:Path) -> str:
        """ This ensures that the stem is PURE if there's more than one suffix.

        Args:
            f_suffixes (list[str]): _description_
            file (Path): _description_

        Returns:
            str: _description_
        """
        output:Path = file.stem

        index = 0
        while index < len(f_suffixes):
            output = PurePosixPath(output).stem
            index += 1
        return output

    def obtain_numbers_from_IMG_file(self, f_stem:str) -> dict:
        output:str = None
        # print()

        substrings_full_items:list[str] = f_stem.split("_")
        # print(substrings_full_items)
        # substrings_full_items.sort()
        # print(substrings_full_items)

        img_grabbed:str = None
        # for sub in substrings_full_items:
        #     if "IMG" in sub:
        #         img_grabbed:str = ""
        #         break
        is_it_IMG:bool = False
        if "IMG" in substrings_full_items:
            substrings_full_items.pop(0)
            is_it_IMG = True
            img_grabbed = "".join(substrings_full_items)
            # print(f"img_grabbed: {img_grabbed}")
        # if img_grabbed is None:
        #     return None

        numbers:str = None
        if not img_grabbed is None:
            substrings_img: list[str] = img_grabbed.split()
            # print(substrings_img)
            numbers = " ".join(substrings_img)


        output:dict = {
            "numbers": numbers,
            "is_it_img": is_it_IMG }
        return output

    def debug_print_look_down_here(self):
        print("--- Look down here :3 --- \n")
        print(f"*Class: {self.__class_name} \n")

    def debug_print_look_up_here(self):
        print("\n--- Look up here :3 ---")


    def debug_print_lists(self):
        self.debug_print_look_down_here()

        print("--- DEBUG AREA :3 ---")

        print(f"* Media with extensions: {self.medias_with_extensions}")
        print(f"size: {len(self.medias_with_extensions)}")
        print()

        print(f"* Medias with only stem: {self.medias_only_stem}")
        print(f"size: {len(self.medias_only_stem)}")
        print()

        print(f"* Medias suffixes: {self.medias_suffixes}")
        print(f"size: {len(self.medias_suffixes)}")
        print()

        print(f"* Medias' only numbers: {self.medias_only_numbers}")
        print(f"size: {len(self.medias_only_numbers)}")
        print()

        print(f"* Potential duplicates: {self.potential_duplicate}")
        print(f"size: {len(self.potential_duplicate)}")
        print()

        print(f"Dictionary items: {self.files_dict}")

        print(f"* Total amount of files: {self.size()}")

        self.debug_print_look_up_here()

    def size(self):
        return len(self.files_dict)

    
    def export_list_of_dict(self) -> list[dict]:
        return self.files_dict


def run_experiments():
    def print_spacers():
        print("------")

    scan_for_media.find_media()

    # experiment_finding_absolute_path() 
    # print_spacers()

    # experiment_finding_relative_path()
    # print_spacers()

    # experiment_pathlib()

def experiment_finding_absolute_path():
    print("Finding absolute path:")
    output:str = os.path.abspath("checkAllPhotos")
    print(output)

def experiment_finding_relative_path():
    print("Finding relative path:")

    dirname = os.path.dirname("")

def experiment_pathlib():
    print("hello pathlib :3")
    cwd:Path = Path.cwd()
    print(cwd)

    output = Path(r'_docs/').glob("**/*")
    print(output)
    print()

    for file in output:
        print(file)
        print(file.__format__)

        convert_to_string:str = str(file.stem)
        print(f"print conversion: {convert_to_string}")
        print()



