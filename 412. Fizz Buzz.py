# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        num = n
        while num > 0:    
            if num % 5 == 0 and num % 3 == 0:
                answer.insert(0, 'FizzBuzz')
            elif num % 3 == 0:
                answer.insert(0, 'Fizz')
            elif num % 5 == 0:
                answer.insert(0, 'Buzz')
            else:
                answer.insert(0, str(num))
            num = num - 1
        return answer