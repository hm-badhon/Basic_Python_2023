# read the file (filename,mode: read)
file_to_work=open('ML.txt','r')
content=file_to_work.read()
print(content)
#file_to_work.close()

# if we want to read content byte by byte
just_one_char=file_to_work.read(1)
print(just_one_char)
print("..................")
remaining_five_char=file_to_work.read(5)
print(remaining_five_char)
print("....................")
rest_of_the_file=file_to_work.read()
print(rest_of_the_file)
file_to_work.close()
