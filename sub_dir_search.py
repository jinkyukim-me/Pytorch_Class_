import os

# for (path, dir, files) in os.walk("C:\dev\Pytorch_Class_"):
#     for filename in files:
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.jpg':
#             print("%s" % (filename))

i=0
for (path, dir, files) in os.walk("C:\dev\Pytorch_Class_\"):
    for filename in files:
        dst = "catpic" + str(i) + ".jpg"
        src = filename


    os.rename(src, dst)
    i += 1
# def main():
#     i = 0
#
#     for filename in os.listdir(): #xyz is folder's name
#         dst = "catpic" + str(i) + ".jpg"
#         src = filename
#
#         # rename() function will
#         # rename all the files
#         os.rename(src, dst)
#         i += 1
#
#
# # Driver Code
# if __name__ == '__main__':
#     # Calling main() function
#     main()