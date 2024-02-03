from flask import *
import googlemaps
from flask_wtf import *

app=Flask(__name__)
#gm=googlemaps.Client(key='    ')
#gmaps=googlemaps.Client()

@app.route('/')
def map():
    #center={'lat':'12.9258','long':'77.5266'}
    #static_map_url = gmaps.static_map(size=(400, 400), center=center, zoom=12)
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
