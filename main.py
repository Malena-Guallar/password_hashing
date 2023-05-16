import bcrypt
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])



def getInput() : 
    if request.method == "POST":
        global password
        password = request.form["password"]
        hashed = hashing(password)
        result = comparing(password, hashed)
        return render_template("result.html", password=password, hashed=hashed, result=result)
    else :
        password = request.args.get('password')
        return render_template("result.html")
    

def hashing(password) :
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def comparing(password, hashed):
    if bcrypt.checkpw(password.encode(), hashed.encode()):
        return "Matches"
    else:
        return "No match"


if __name__ == '__main__':
    app.run(debug=True)    


# plaintext_password = b"motdepasse"

# # generating the salt
# salted = bcrypt.gensalt()
# # hashing the password
# hashed = bcrypt.hashpw(plaintext_password, salted)

# print(hashed)

# # comparing the original password to the hashed one
# if bcrypt.checkpw(plaintext_password, hashed):
#     print("Matches")
# else:
#     print("No match")