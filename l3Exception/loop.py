while True:
    try:
        x=int(input("what is x?" ))
        #break
    except ValueError:
        print("X is not an integer")
    else:
        break
print(f"x is {x}")           