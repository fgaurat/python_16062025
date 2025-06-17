
def main():
    csv_file = "MOCK_DATA.csv"
    with open(csv_file) as f:
        for line in f:
            print(line)

if __name__=='__main__':
    main()
