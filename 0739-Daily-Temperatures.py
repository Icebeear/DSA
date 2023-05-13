temperatures = [73,74,75,71,69,72,76,73]
answer = [0] * len(temperatures)
for x in range(len(temperatures)):
    for y in range(x, len(temperatures)):
        if temperatures[y] > temperatures[x]:
            answer[x] = y
            break 



print(answer) 