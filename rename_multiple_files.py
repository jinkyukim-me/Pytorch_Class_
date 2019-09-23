# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    i = 0

    for filename in os.listdir("cats"): #xyz is folder's name
        dst = "catpic" + str(i) + ".jpg"
        src = 'cats' + filename
        dst = 'cats' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()