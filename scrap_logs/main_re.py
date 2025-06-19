from glob import glob
import re

def main():
    logs = glob('*.log')

    for log in logs:
        with open(log) as f:
            for line in f:
                r = re.findall(r"^(.+?)\s",line.strip())
                print(r)


if __name__=='__main__':
    main()
