from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')


@app.route('/form')
def form():
    #print(location_names)
    return render_template('index.html')


@app.route('/commit_vals')
def commit_vals():
    try:
        lon = float(request.args.get('lon'))
        lat = float(request.args.get('lat'))
    except Exception as e:
        return str(e), 400

    try:
        return render_template('index.html', Result=f"The Latitude is {lat} and Longitude is {lon}!")
    except Exception as e:
        return str(e), 400



if __name__ == '__main__':
   app.run(debug=True)