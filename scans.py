import os
from pathlib import Path, PurePath, PurePosixPath

class scan_for_media:
    def __init__(self) -> None:
        self.medias_with_extensions: list[str] = []
        self.medias_only_stem: list[str] = []
        self.medias_suffixes: list[str] = []

        self.medias_only_numbers: list[str] = []

    def find_media(self) -> list[str]:
        
        _pathway_for_media: str = "_media/"
        directory_media:Path = Path(_pathway_for_media)

        if not directory_media.exists():
            print("IT DOESN'T EXIST :'[")
            return []
        else:
            print("Folder '_media' exists!") 
        print()
        
        for index, file in enumerate(directory_media.glob("**/*")):
            print(f"current index: {index}")
            f_full_name: str = file.name

            f_suffixes:str = file.suffixes

            f_stem:str = None
            if len(f_suffixes) > 1: 
                f_stem = self.obtain_pure_stem(f_suffixes=f_suffixes, file=file)
            else:
                f_stem = file.stem


            print(f"Printing file's name with extensions: {f_full_name}")

            print(f"Printing file's stem: {f_stem}")
            
            print(f"Print suffixes: {f_suffixes}")
            
            # TODO - obtain ONLY numbers from file's string
            f_numbers: str = self.obtain_numbers(f_stem=f_stem)
            print(f"Printing only numbers: {f_numbers}")
            print()

            self.add_to_lists(f_full_name=f_full_name, f_stem=f_stem, f_suffixes=f_suffixes, f_numbers=f_numbers)
    
    def add_to_lists(self, f_full_name: str, f_stem: str, f_suffixes: str, f_numbers:str):
        self.medias_with_extensions.append(f_full_name)
        self.medias_only_stem.append(f_stem)
        self.medias_suffixes.append(f_suffixes)
        self.medias_only_numbers.append(f_numbers)

        print("FINISH ME!")

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

    def obtain_numbers(self, f_stem:str) -> str:
        output:str = None

        substrings_full_items:list[str] = f_stem.split()
        print(substrings_full_items)
        substrings_full_items.sort()
        print(substrings_full_items)

        img_grabbed:str = None
        for sub in substrings_full_items:
            if "IMG_" in sub:
                img_grabbed:str = sub
                break
        if img_grabbed is None:
            return

        substrings_img: list[str] = img_grabbed.split("_")
        print(substrings_img)
        for index, value in enumerate(substrings_img):
            if value == "IMG":
                substrings_img[index] = ""

        output = "".join(substrings_img)
        return output

    def new_method(self):
        print()

    def debug_print_lists(self):
        print(f"Media with extensions: {self.medias_with_extensions}")
        print()

        print(f"Medias with only stem: {self.medias_only_stem}")
        print()

        print(f"Medias suffixes: {self.medias_suffixes}")
        print()

        print(f"Medias' only numbers: {self.medias_only_numbers}")


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



