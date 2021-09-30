import time


banner = '''
  _______   __                  __        ______  ________  __ 
 /       \ /  |                /  |      /      |/        |/  |
 $$$$$$$  |$$/  _______    ____$$ |      $$$$$$/ $$$$$$$$/ $$ |
 $$ |__$$ |/  |/       \  /    $$ |        $$ |     $$ |   $$ |
 $$    $$< $$ |$$$$$$$  |/$$$$$$$ |        $$ |     $$ |   $$ |
 $$$$$$$  |$$ |$$ |  $$ |$$ |  $$ |        $$ |     $$ |   $$/ 
 $$ |__$$ |$$ |$$ |  $$ |$$ \__$$ |       _$$ |_    $$ |    __ 
 $$    $$/ $$ |$$ |  $$ |$$    $$ |      / $$   |   $$ |   /  |
 $$$$$$$/  $$/ $$/   $$/  $$$$$$$/       $$$$$$/    $$/    $$/ 
                                                           '''
                                                          
def print_menu():    
    print(banner)   
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Bind files to image")
    print("2. Unbind files from image")
    print("3. Read Hex from file")
    print("4. Download a random image")
    print("5. Exit")
    print(67 * "-")
  
loop=True      
  
while loop:          
    print_menu()    
    choice = eval(input("Enter your choice [1-5]: "))
     
    if choice==1:     
        print("Menu 1 has been selected")
        imagename = input("Picture name to bind files: ")
        filename = input('File name to bind into '+ imagename+ ' : ')
        with open(imagename, 'ab') as f, open(filename, 'rb') as e:
            f.write(e.read())
            time.sleep(3)
            print('\n')
            print(filename + ' has been bindend to '+ imagename +' successfully!')

    elif choice==2:
        print("Menu 2 has been selected")
        import os
        import time
        image = input("Picture name: ")
        newfilename = input('Name of your newfile: ')
        with open(image, 'rb') as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            with open(newfilename, 'wb') as e:
                e.write(f.read())
                time.sleep(2)
                print(newfilename + ' has been bindend to '+ image)
                time.sleep(2)
                print('Opening ' + newfilename + '')
        os.startfile(newfilename)

    elif choice==3:
        print("Menu 3 has been selected")
        import binascii
        imagename = input("File name to read hex from: ")
        file = imagename
        with open(file, 'rb') as f:
            content = f.read()
        print(binascii.hexlify(content))

    elif choice==4:
        print("Menu 4 has been selected")
        import urllib.request

        def download_image(url):
            name = 'photo'
            fullname = str(name)+".jpg"
            urllib.request.urlretrieve(url,fullname)     
        download_image("https://picsum.photos/200")
        print("New photo.jpg downloaded and replaced the old one")
        time.sleep(4)


    elif choice==5:
        print("Good byeeeeeeeeeeeeee!")
        loop=False 
    else:
        input("Wrong option selection. Enter any key to try again..")
