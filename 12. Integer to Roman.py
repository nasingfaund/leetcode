class Solution:
    def intToRoman(self, val: int) -> str:
        mapping = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            500: 'D',
            400: 'CD',
            900: 'CM',
            1000: 'M',
        }
        divisors = list(sorted(mapping.items(), key=lambda x: x[0], reverse=True))
        pointer = 0
        result = ''

        while val:
            d, symbol = divisors[pointer]
            rem = val % d
            if rem != val:
                result += mapping.get(d)
                val -= d
            else:
                pointer += 1

        return result
