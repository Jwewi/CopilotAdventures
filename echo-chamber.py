echoes= [3, 6, 9, 12]
memories = []
def predictNext(echoes):
"""
Predicts the next value in a sequence based on the given echoes.

Parameters:
echoes (list): A list of numbers representing the previous values in the sequence.

Returns:
int: The predicted next value in the sequence.

Notes:
- The function calculates the difference between the second and first element in the echoes list.
- It then adds this difference to the last element in the echoes list to predict the next value.
- The predicted value is appended to the memories list, which stores the full sequence including the predicted number.
"""
   difference = echoes[1] - echoes[0]
   next_value = echoes[-1] + difference
   memories.extend(echoes + [next_value])    
   return next_value
    # Store the full sequence including the predicted number in memories
print(predictNext(echoes))

