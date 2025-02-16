from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    group_order_link = request.form.get('group_order_link')
    
    if not all([name, address, phone, group_order_link]):
        return "Error: All fields are required!", 400

    return f"Order received! Name: {name}, Address: {address}, Phone: {phone}, Link: {group_order_link}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
