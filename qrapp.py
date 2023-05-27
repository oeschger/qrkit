from flask import Flask, send_file, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stuff')
def stuff():
    return render_template('stuff.html')


@app.route('/generate', methods = ['POST', 'GET'])
def generate():
    # Data to encode
    data = request.form['url']

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

 
