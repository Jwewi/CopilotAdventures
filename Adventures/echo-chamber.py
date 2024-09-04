echoes= [3, 6, 9, 12]
memories = []
def predictNext(echoes):
   difference = echoes[1] - echoes[0]
   next_value = echoes[-1] + difference
   memories.extend(echoes + [next_value])    
   return next_value
    # Store the full sequence including the predicted number in memories
print(predictNext(echoes))

