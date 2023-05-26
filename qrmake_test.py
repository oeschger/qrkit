from flask import Flask, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return '<b>QRKit</b> - Add information to your stuff'

@app.route('/generate')
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
    img = qr.make_image(fill_color = 'black',
                        back_color = 'white')
    
    fn = 'assets/myfile.png'
    img.save(fn)
    return send_file(fn, mimetype='image/png')

app.run(host='0.0.0.0', port=81)

## prototype for managing args from form submit (?)
# @app.route(...)
# def login():
#     username = request.args.get('username')
#     password = request.args.get('password')

 
