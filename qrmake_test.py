from flask import Flask, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/gen')
def gen():
    # Data to encode
    data = "GeeksforGeeks"

    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
    # Adding data to the instance 'qr'
    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'red',
                        back_color = 'white')
    
    return send_file(img.open(fp, mode='r',formats=None), mimetype='image/gif')

app.run(host='0.0.0.0', port=81)


 