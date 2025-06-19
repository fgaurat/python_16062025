from flask import Flask,render_template
from CustomerDAO import CustomerDAO

app = Flask(__name__)

# flask run --debug

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/old")
def oldcustomers():
    dao = CustomerDAO('../customers.db')
    customers = dao.findAll()

    html= "<h1>Customers</h1><table>"
    for customer in customers:
        html+=f"""<tr>
        <td>{customer.id}</td>
        <td>{customer.firstName}</td>
        <td>{customer.lastName}</td>
        <td>{customer.email}</td>
        <td>{customer.gender}</td>
</tr>
"""
    html+="</table>"

    return html

@app.route("/")
def customers():
    dao = CustomerDAO('../customers.db')
    customers = dao.findAll()
    return render_template("customers.html",customers=customers )
