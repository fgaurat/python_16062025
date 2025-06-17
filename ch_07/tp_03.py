import json
from pprint import pprint
def main():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        },
        {
            "userId": 1,
            "id": 5,
            "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
            "completed": False
        },
        {
            "userId": 1,
            "id": 6,
            "title": "qui ullam ratione quibusdam voluptatem quia omnis",
            "completed": False
        },
        {
            "userId": 1,
            "id": 7,
            "title": "illo expedita consequatur quia in",
            "completed": False
        }
    ]

    with open("todo-list.json","w") as f:
        json.dump(data,f,indent=4)

    
    with open("todo-list.json","r") as f:
        data_from_file = json.load(f)
        pprint(data_from_file)



if __name__ == '__main__':
    main()
