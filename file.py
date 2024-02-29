# f = open('test.txt','r')
# print(f.mode)
# f.close()

# using Context manager
with open('test.txt', 'r') as f:  # this way, File opened is implicitly closed
    pass
    # f_contents = f.read() # returns entire file
    # f_contents = f.readline() # returns a line of the file
    # f_contents = f.readlines()  # returns entire file as a lists of line

    # print(f_contents, end = '')

    # for line in f:
    #     print(line,end = '')

    # f_contents = f.read(1)  # reads specified number of characters and end with *
    # print(f_contents,end='*')

    # sizetoread = 1
    # f_contents = f.read(sizetoread)

    # print(f.tell()) # returns current position of file pointer in the file

    # f.seek(index) # shifts the file pointer to the index entered as parameter in the function

    # while len(f_contents)>0:
    #     print(f_contents,end='*')
    #     f_contents = f.read(sizetoread)

# with open('test2.txt', 'w') as f:   # creates the file if not existed
#     f.write('Test') # writes the characters in the file (might overwrite)

# with open('test.txt', 'r') as rf:
#     with open('test2.txt','w') as wf:
#         for line in rf:
#             wf.write(line)
#
# with open('test2.txt','r') as rf:
#     print(rf.read())

# # To work with image files
# with open('image.jpg','rb') as rf:
#     with open('image_copy.jpg','wb')as wf:
#         for line in rf:
#             wf.write(line)

# # to work with image files using chunks
# with open('image.jpg','rb') as rf:
#     with open('image_copy.jpg','wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk)>0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
