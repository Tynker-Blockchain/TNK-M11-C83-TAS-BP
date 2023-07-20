from flask import Flask, render_template, request
import os
from cipher import cipher, decipher
# import generateKeys, encrypt from encrypt.py


STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True



@app.route("/", methods= ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        
        blockData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }

        # Call generateKeys() function and recieve publicKey and privateKey 


        # Use encrypt() function to hide data of sender, reciever and amount        
        sender = cipher(sender, 2)
        receiver = cipher(receiver, 2)
        amount = cipher(amount, 2)

        encryptedData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }

        sender = decipher(sender, 2)
        receiver = decipher(receiver, 2)
        amount = decipher(amount, 2)

        decryptedData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }

        return render_template('index.html', blockData = blockData, encryptedData = encryptedData, decryptedData = decryptedData)

if __name__ == '__main__':
    app.run(debug = True, port=4000)