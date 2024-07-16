from itertools import permutations

def numbers_game_solver(numbers, target):
    def helper(numbers, path, current_sum):
        if not numbers:
            if current_sum == target:
                return path
            else:
                return None
        
        for i in range(len(numbers)):
            num = numbers[i]
            remaining = numbers[:i] + numbers[i+1:]
            
            # Try addition
            result = helper(remaining, path + [f'{current_sum} + {num}'], current_sum + num)
            if result:
                return result
            
            # Try subtraction
            result = helper(remaining, path + [f'{current_sum} - {num}'], current_sum - num)
            if result:
                return result
            
            # Try multiplication
            result = helper(remaining, path + [f'{current_sum} * {num}'], current_sum * num)
            if result:
                return result
            
            # Try division
            if num != 0 and current_sum % num == 0:
                result = helper(remaining, path + [f'{current_sum} / {num}'], current_sum // num)
                if result:
                    return result
        
        return None
    
    result = helper(numbers, [], 0)
    return result

# Example usage:
numbers = []
for i in range(6):
    numbers.append(int(input(f"Enter number {i+1}: ")))
target = int(input("Enter the target number: "))

solution = numbers_game_solver(numbers, target)
if solution:
    print(f"Solution found: {' '.join(solution)}")
else:
    print("No solution found.")