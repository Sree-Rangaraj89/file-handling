file_read = open('Codingal.txt','r')
print("File in Read mode -")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')

file_write.write("file in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr old")
file_write.close()

file_append = open('Codingal.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write("Hi! I am penguin. I am 1 yr. old")
file_append.close()