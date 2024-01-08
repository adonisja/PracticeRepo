def main():
    fileName = (input("Enter your file name: ")) 
    fileName = fileName.lower()
    '''creates a list that splits the file name into two sections along the . operator'''
    mediaType = fileName.split(".")
    print(mediaType) #check for the list members
    if len(mediaType) < 2: #throws an error if an extention was not entered
        print("You did not enter a file extention")
        exit()
    else:
        mediaType = mediaType[1] # assigns the mediatype to the second member of the list (the extention)
        print("Your media type is: ", end= "")
        #uses a switch function to compare the values in the mediaType variable and outputs a result depending on the value
        match mediaType: 
            case 'gif':
                print("image/gif")
            case 'jpeg':
                print("image/jpeg")
            case 'jpg':
                print("image/jpeg")
            case 'png':
                print("image/png")
            case 'pdf':
                print("application/pdf")
            case 'txt':
                print("text/plain")
            case 'zip':
                print("application/zip")
            case _: #switch-case default value 
                print("application/octet-stream")
        

main()