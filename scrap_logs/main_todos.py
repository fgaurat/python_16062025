import requests
def main():
    url="https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url)
    todos = r.json()
    print(todos[0]['title'])
if __name__=='__main__':
    main()
