class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
         
        def convert_one_digit(num):
            mapping = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            
            return mapping.get(num)
        
        def convert_two_digit_less_twenty(num):
            mapping = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: "Nineteen"
            }
            
            return mapping.get(num)
        
        def convert_tens(num):
            mapping = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            
            return mapping.get(num)
        
        def convert_two_digit(num):
            if not num:
                return ''
            elif num < 10:
                return convert_one_digit(num)
            elif num < 20:
                return convert_two_digit_less_twenty(num)
            else:
                ten = num // 10
                tenString = convert_tens(ten)
                
                rest = num - (ten * 10)
                    
                if rest:
                    return tenString + ' ' + convert_one_digit(rest)
                else:
                    return tenString
        
        def convert_three_digit(num):
            hundreds = num // 100
            rest = num - (hundreds * 100)
            
            if hundreds and rest:
                return convert_one_digit(hundreds) + " Hundred " + convert_two_digit(rest)
            elif not hundreds and rest:
                return convert_two_digit(rest)
            elif hundreds and not rest:
                return convert_one_digit(hundreds) + " Hundred"
            
        billion = num // 1000000000
        million = (num - (billion * 1000000000)) // 1000000
        thousand = (num - (billion * 1000000000) - (million * 1000000)) // 1000
        rest = (num - (billion * 1000000000) - (million * 1000000) - (thousand * 1000))
        
        if not num:
            return 'Zero'
        
        result = ''
        
        if billion:
            billString = convert_three_digit(billion)
            result = billString + " Billion" 
        
        if million:
            millString = convert_three_digit(million)
            result += ' ' if result else ''
            result += millString + " Million"
            
        if thousand:
            thousandString = convert_three_digit(thousand)
            result += ' ' if result else ''
            result += thousandString + " Thousand"
        
        if rest:
            result += ' ' if result else ''
            result += convert_three_digit(rest)
        
        return result