words = ["aardvark","cookies","asterisk","cowabunga","gryphon","angular","cringe"]

index = 0
c_counter = 0

while index < len(words):
    if words[index][0:1] == "c":
        print(words[index])
        c_counter = c_counter + 1
        
    index = index + 1