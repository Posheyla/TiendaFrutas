from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    usuario={
        "num_strawberry":request.form["strawberry"],
        "num_raspberry":request.form["raspberry"],
        "num_apple": request.form["apple"],
        "nombre": request.form["first_name"],
        "apellido": request.form["last_name"],
        "id": request.form["student_id"]
    }
    num_strawberry = int(usuario["num_strawberry"])
    num_raspberry = int(usuario["num_raspberry"])
    num_apple = int(usuario["num_apple"])

    total = num_strawberry + num_raspberry + num_apple

    return render_template("checkout.html",usuario=usuario,total=total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    