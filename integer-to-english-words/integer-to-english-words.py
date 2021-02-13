class Solution(object):
    def convert_single_dig(self, num):
        translator = {
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
        
        return translator.get(num, None)
    
    def convert_two_dig(self, num):
        if num == 0:
            return None
        
        if num < 10:
            return self.convert_single_dig(num)
        elif 10 <= num < 20:
            return self.convert_two_dig_less_twenty(num)
        else:
            return self.convert_two_dig_greater_twenty(num)
            
        
    def convert_two_dig_less_twenty(self, num):
        translator = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        return translator.get(num)

    def convert_two_dig_greater_twenty(self, num):
        string = str(num)
        tens = int(string[0])
        
        translator = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        tensString = translator.get(tens) 
        singleString = self.convert_single_dig(int(string[1]))
        
        return tensString + " " + singleString if singleString else tensString
    
    def convert_three_dig(self, num):
        if 99 >= num:
            return self.convert_two_dig(num)
        else:

            string = str(num)
            single = int(string[0])
            double = int(string[1:])

            singleString = self.convert_single_dig(single) + " " + "Hundred"
            doubleString = self.convert_two_dig(double)

            if not doubleString:
                return singleString
            elif not singleString:
                return doubleString

            return singleString + " " + doubleString
        

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        out = ''
        
        if num == 0:
            return 'Zero'

        billion = num // 1000000000
        if billion > 0:
            out += self.convert_three_dig(billion) + ' Billion'
            num = num % 1000000000
        
        million = num // 1000000
        if million:
            out += ' ' if out else ''
            out += self.convert_three_dig(million) + " Million"
            num = num % 1000000
        
        thousand = num // 1000
        if thousand:
            out += ' ' if out else ''
            out += self.convert_three_dig(thousand) + " Thousand"
            num = num % 1000    
        
        if num:
            out += ' ' if out else ''
            out += self.convert_three_dig(num)
            
        return out
    
        