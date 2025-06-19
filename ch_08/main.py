import traceback

def div(a,b):
    return a/b

def call_div(a,b):
    c=0
    try:
        print("OPEN LOG")
        c = div(a,b)
    # except Exception as e:
    #     print(e)
    finally:
        print("CLOSE LOG")
    
    return c
    


def main():
    try:
        a = 2
        # b = int(input('b: '))
        b = 0
        c = call_div(a,b)

        print(c)
    except ValueError as e:
        print(e)
        traceback.print_exc()
    except TypeError as e:
        print(e)
        traceback.print_exc()
    except ZeroDivisionError as e:
        print(e)
        traceback.print_exc()
    except Exception as e:
        print(e)
        traceback.print_exc()
    else:
        print("le else")

    print("La suite ...")

if __name__=='__main__':
    main()
