
def main():
    a=2
    b=3
    c = a/b

    result = f"{a=}, {b=}, {c=:.2%}"
    print(result)
    a=1000
    a=1_000


    results = [a,b,c]
    # s = "{1} {0} {2:.2%}".format(a,b,c)
    s = "{1} {0} {2:.2%}".format(*results)
    
    s = "{value_01} {value_02} {value_03:.2%}".format(value_01=a,value_02=b,value_03=c)
    d ={
        "value_01":a,
        "value_02":b,
        "value_03":c
    }
    s = "{value_01} {value_02} {value_03:.2%}".format(value_01=d['value_01'],value_02=d['value_02'],value_03=d['value_03'])
    s = "{value_01} {value_02} {value_03:.2%}".format(**d)
    print(s)

if __name__=='__main__':
    main()
