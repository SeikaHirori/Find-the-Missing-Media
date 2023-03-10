# class Dissecting:
def dissect_everything_in_dict(item_dict:dict):
    raise NotImplementedError

def dissect_file_name(item_dict:dict) -> str:
    the_key:str = "file name"
    return item_dict[the_key]

def dissect_stem(item_dict:dict) -> str:
    the_key:str = "stem"
    return item_dict[the_key]

def dissect_suffixes(item_dict:dict) -> list[str]:
    the_key:str = "suffixes"
    return item_dict[the_key]

def convert_suffixes_to_str(suffixes:list[str]) -> str:
    output: str = None
    if suffixes is not None:
        if len(suffixes) != 0:
            output = " | ".join(suffixes)
    
    return output

def dissect_is_it_IMG(item_dict:dict) -> bool:
    the_key:str = "is_it_IMG"
    return item_dict[the_key]

def dissect_numbers(item_dict:dict) -> str:
    the_key:str = "numbers"
    return item_dict[the_key]

def dissect_duplicate(item_dict:dict) -> bool:
    the_key:str = "duplicates"
    return item_dict[the_key]

