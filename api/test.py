file1 = open("dataset.txt","r") 
dictionary = eval(file1.read())
print(eval(file1.read())[1])
file1.close()