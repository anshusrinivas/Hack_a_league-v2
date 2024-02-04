from flask import *
import pandas as pd
from flask_wtf import *

app = Flask(__name__)
app.secret_key = 'masnkbdkbsad'
csrf = CSRFProtect(app)

packages_df = pd.read_csv('pac_det.csv')
users_df = pd.read_csv('log.csv')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global username
        username = request.form['username']
        password = request.form['password']
        
        user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
        
        if not user.empty:
            return render_template('customer.html', username=username)  # Pass username to template
        else:
            return render_template('login_page.html', error="Invalid credentials")
    
    return render_template('login_page.html')

@app.route('/pac_id', methods=['POST', 'GET'])
def pac_id():
    if request.method == 'POST':
        package_id = request.form['package_id']
        secret_key = request.form['secret_key']
        re = users_df[(users_df['package_id'] == package_id) & (users_df['secret_key'] == secret_key)]
        if not re.empty:
            result = int(package_id[3:])
            dic = packages_df.to_dict(orient='list')  # Change 'list' here
            if result <= len(dic['driver_name']):
                driver_name = dic['driver_name'][result-1]
                transit_stage = dic['state'][result-1]
                lat = dic['latitude'][result-1]
                long = dic['longitude'][result-1]
                phone_number = dic['phone_number'][result-1]
                return render_template('result.html', driver_name=driver_name, transit_stage=transit_stage,
                                       latitude=lat, longitude=long, phone_number=phone_number)
            else:
                return render_template('customer.html', error='Package not found')
        else:
            return render_template('customer.html', error='Invalid Credentials')
    return render_template('customer.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
