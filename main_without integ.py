from flask import *
from flask_wtf import *
import pandas as pd
import numpy as np

login_det=pd.DataFrame(pd.read_csv())
pac_det=pd.DataFrame(pd.read_csv())


app=Flask(__name__)
app.secret_key='jsdnkjfsalfhsdkfjsd'
CSRFProtect(app)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form('username')
        password=request.form('password')
        ind1=login_det.index(username)
        try:
            ind2=login_det.index(password)
        except:
            ind2=0
        if ind1==ind2:
            if login[ind1]['type']=='customer':
                return render_template(url_for('customer'))
            else:
                return render_template(url_for(''))
        
    return render_template('home.html')
app.route('/customer')
def customer():
    pac_id=request.form('pac_id')
    sec_code=request.form('sec_code')
    ind3=pac_det.index(pac_id)
    ind4=pac_det.index(sec_code)
    if(ind3==ind4):
        return render_template(url_for('suc_track'))
    return render_template('')

if __name__=='__main__':
    app.run()
    