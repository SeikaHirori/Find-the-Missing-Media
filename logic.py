class logic_time:

    def __init__(self) -> None:
        self.desired_range: list[str] = []


    def run_experiments(self):
        self.createRange(starting_point=0, end=50)

    def createRange(self, starting_point:int = 0, end:int = 9999) -> list[str]:
        print(f"hello {self.createRange.__name__}")

        # RFER #1
        output_range: list[str] =  ["%04d" % x for x in range(starting_point, end + 1)]

        # print(output_range)
        self.desired_range = output_range
        return output_range
    
    def pop_front(self):
        return self.desired_range.pop(0)
    
    def is_number_in_list(self, number:str) -> bool:
        # Use binary search here
        return #TODO

