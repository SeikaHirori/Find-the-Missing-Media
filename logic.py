
def run_experiments():
    createRange(starting_point=0, end=50)

def createRange(starting_point:int = 0, end:int = 9999) -> list[str]:
    print(f"hello {createRange.__name__}")

    # RFER #1
    output_range: list[str] =  ["%04d" % x for x in range(starting_point, end)]

    print(output_range)
    return output_range

