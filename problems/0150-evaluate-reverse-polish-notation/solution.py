class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for ele in tokens :
            if ele not in "+-*/":
                numbers.append(int(ele))

            elif ele in "+-*/" :
                b = numbers.pop()
                a = numbers.pop()
                
                if ele == "+" :
                    numbers.append(a + b)
                elif ele == "-" :
                    numbers.append(a - b)
                elif ele == "*" :
                    numbers.append(a * b)
                elif ele == "/" :
                    numbers.append(int(a / b))

        return numbers[0]
