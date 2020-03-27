class Calculator:
    def add(string):
        lis = string.split(",")

        sum = 0
        for i in lis:
            if i.isdigit():
                sum += int(i)

        return sum

        
        
    
