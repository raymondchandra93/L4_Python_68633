import string

letters = list(string.ascii_lowercase)
for l in letters:
    print(l)

while True:
    answer = input("Please enter a number OR 'stop' to quit: ")

    # if stop then stop the project
    if answer == "stop":
        break
    
    try:
        # Get and print the letter
        index = int(answer)-1
        print(letters[index])

    except ValueError:
        print("Not a number")
    
    except IndexError:
        print("Index is out of range. Please select 1-26 only")

    except:
        print("there is an error")
