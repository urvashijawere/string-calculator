class Calculator:
    def add(self, numbers):
        """ numbers is a string, extract items from string and return their addition"""
        if len(numbers) == 0:
            return 0

        sum = 0
        for item in numbers:
            if item.isdigit():
                sum += int(item)

        return sum
