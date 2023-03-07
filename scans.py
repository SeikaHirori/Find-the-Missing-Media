import os
from pathlib import Path

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
            f_name: str = file.name
            f_stem: str = file.stem
            f_suffix:str = file.suffixes

            print(f"Printing file's name with extensions: {f_name}")

            print(f"Printing file's stem: {f_stem}")
            
            print(f"Print suffixes: {f_suffix}")
            
            # TODO - obtain ONLY numbers from file's string
            f_numbers: str = "WIP"
            print(f"Printing only numbers: {f_numbers}")
            print()
    
    def add_to_lists(self, f_name: str, f_stem: str, f_suffix: str, f_numbers:str):
        

        print("FINISH ME!")

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



