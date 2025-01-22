class Calculator:
    def __init__(self, delimiter):
        # assumption: test case inputs will adhere to delimiter of the object
        self.delimiter = delimiter

    def add(self, numbers):
        """ numbers is a string, extract items from string and return their addition"""
        if len(numbers) == 0:
            return 0

        if numbers.endswith('\n'):
            return "invalid"

        new_numbers = numbers.replace('\n', ',').split(self.delimiter)
        negatives = [x for x in new_numbers if int(x) < 0]
        if len(negatives) > 0:
            neg_numbers = ",".join(negatives)
            raise ValueError("Negative numbers not allowed: {}".format(neg_numbers))

        total = 0
        for item in new_numbers:
            total += int(item)
        return total
