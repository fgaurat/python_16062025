
from CustomerDAO import CustomerDAO
from pprint import pprint
def getMale(gen):
    for g in gen:
        if g.gender == "Male":
            yield g

def main():
    dao = CustomerDAO('customers.db')
    customers = dao.findAll()
    customersMale = getMale(customers)
    all = list(customersMale)
    pprint(all)
    # c = next(customers)
    # print(c)
    # c = next(customers)
    # print(c)
    # for customer in customers:
    #     print(customer)
if __name__=='__main__':
    main()
