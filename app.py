## Author @Waseem
## Jakega Project


from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

## Author @Waseem ##Routing Flask To Pages

@ app.route('/')
def home():
    title = 'JakEGA Project'
    return render_template('index.html', title=title)

@ app.route('/crop-recommend')

def crop_recommend():
    title = 'JakEGA Project'
    return render_template('crop.html', title=title)

@ app.route('/AI Chatbot')
def yember():
    title = 'JakEGA Project'   
    return render_template('yember.html', title=title)

@ app.route('/weather')
def weather(): 
    title = 'JakEGA Project' 
    return render_template('weather.html', title=title)


@ app.route('/About Us')
def AboutUs():
    title = 'JakEGA Project'
    return render_template('About.html', title=title)

@ app.route('/Farmer Login')
def Login():
    title = 'JakEGA Project'
    return render_template('Login.html', title=title)


## Author @Waseem ## Loading Model
model=pickle.load(open('randomforrest2.pkl','rb'))


## Author @Waseem ## POST request To Form Values
@app.route('/predict',methods=['POST','GET'])
def predict():
    float_features=[float(x) for x in request.form.values()]
    ##data=[np.array(int_features)]
    ##print(int_features)
    data=[np.array(float_features)]
    print(float_features)
    print(data)
   ##prediction=randomforrest2.predict_proba(data)

    prediction=model.predict(data)
     
    ## Author waseem ## Returning Output
    return render_template('crop.html', output='Best suitable crop based on your inputs is {}'.format(prediction))
    

if __name__ == '__main__':
    app.run(debug=True)
