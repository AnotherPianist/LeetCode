class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        for i in range(1, n + 1):
            string = ""
            
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            
            if len(string) == 0:
                string = str(i)
            
            res.append(string)
        
        return res