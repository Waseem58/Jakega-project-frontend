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

@ app.route('/prediction')
def prediction():
    title = 'JakEGA Project'
    return render_template('prediction.html', title=title)


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
     

    Cherry = [
        
        {"Title": "Cherry",
        "Description": " Cherries are a type of small, round fruit that grow on cherry trees. They are typically red or black in color and have a sweet, juicy flesh. In Kashmir, cherry production is primarily focused on sweet cherries, which are grown for consumption fresh, as well as for processing into jams, jellies, and other products. ",
        "Production": " Production : Cherry production in Kashmir is concentrated mainly in the regions of Shopian, Pahalgam, and Srinagar. The fruit is grown on small-scale farms, often as a complement to other crops such as apricots and apples. The cherry trees are typically grown in orchards, and are trained and pruned to promote optimal fruit production. ",
        "Yield": " Yield : The yield of cherries in Kashmir can vary depending on factors such as weather conditions and disease pressures, but generally ranges from 5-15 tonnes per hectare. However, due to the effects of climate change, the yield of cherry has decreased significantly in recent years. ",
        
        "author": "Waseem Ahmad"
        }
    ]

    Walnut = [
        
        {"Title": "Walnut",
        "Description": " Walnut is an important fruit crop grown in the Kashmir valley of India. It is a major source of income for many farmers in the region. The walnut is native to the Himalayan region and is one of the most important fruits grown in the Kashmir Valley. Walnuts are an important source of income for many farmers in the Kashmir Valley. The nuts are used to make a variety of products such as walnut oil, walnut butter, and other food products. The nuts are also used in traditional medicines. The walnuts are exported to other countries, mainly to Europe and the United States. ",
        "Production": " Walnuts are grown mainly in the higher altitude regions of the valley where the climate is cool and dry. The main walnut producing areas in Kashmir are the districts of Anantnag, Pulwama, Shopian, and Kulgam. The crop is usually harvested between August and October. ",
        "Yield": " The average yield of walnuts in Kashmir is around 6-7 metric tons per hectare. The yield depends on the type of variety planted, soil fertility, and the availability of water. The quality of the nuts produced is also affected by the soil type, climate, and the age of the tree. The nuts are usually harvested when they reach maturity. ",
        
        "author": "Waseem Ahmad"
        }
    ]

    Apple = [
        
        {"Title": "Apple",
        "Description": " Apple is a major agricultural crop grown in the Kashmir region of India. It is a deciduous tree that produces sweet, juicy fruits. Apples are grown in the temperate climate of the Kashmir valley, where the summers are warm and the winters are cold. The apple harvest typically begins in late August and continues through October. Apples are grown in orchards, with each tree producing an average of 20-25 kg of fruit. The yield of apple production in Kashmir depends on the variety of apple grown and the level of care taken in the orchard. The Kashmiri apple is known for its sweetness and is highly sought after by consumers. ",
        "Production": " Around 7 lakh farming families, approximately 35 lakh people, are directly or indirectly associated with the horticulture sector. Apples contribute to around 8% of Jammu and Kashmir’s gross domestic product. Both dry and fresh fruits are grown over more than 3.37 lakh hectares of land and with every passing year, more land is brought under fruit cultivation. Alone apples are grown over 1.68 lakh hectares of land followed by pear which are grown on 14,161 hectares of land in the Valley.  ",
        "Yield": " High density Apples consume 70% less fertilizer and 80% less pesticide spray, adding that these Apple trees produce about 50 to 70 tons of fruit per hectare by the third year of plantation while traditional varieties produce about 10 to 15 tons",
        
        "author": "Waseem Ahmad"
        }
    ]

    Almond = [
        
        {"Title": "Almond",
        "Description": " The almond is a tree nut that is widely cultivated in many regions of the world, including the Kashmir region of India. Almond trees are typically grown for their nuts, which are encased in a hard shell and can be eaten raw or roasted. The tree produces white or pink flowers in the spring and the nuts are ready for harvest in the fall. ",
        "Production": " In the context of Kashmir, almond production is an important agricultural activity, although the yield may vary depending on factors such as weather conditions and disease. Almond trees require a specific type of soil and climate to grow properly, with a well-drained soil and a dry, warm climate being ideal. In Kashmir, almond trees are mostly grown in the hilly regions of the state where the soil and climate conditions are most suitable for the tree. ",
        "Yield": " Almond yields in Kashmir can vary greatly depending on the location, the tree's genetics and the care it receives. A mature almond tree can produce between 30 to 60 pounds of almonds per year, but yields can be significantly lower in years when the weather is not favorable. In addition, pests and diseases can also play a role in reducing the yield of almonds. ",
        
        "author": "Waseem Ahmad"
        }
    ]

    Rice = [
        
        {"Title": "Rice",
        "Description": " Rice is a staple crop grown in many parts of the world, including the region of Kashmir. It is a semi-aquatic grass that is typically grown in flooded fields, or paddies. The plant requires a warm climate and plenty of water to grow successfully. ",
        "Production": " rice is typically grown in the Jammu region, which is known for its fertile soil and ample water supply. The crop is usually planted in April and harvested in September. The yield per hectare varies depending on the variety of rice and the growing conditions, but it can range from 2 to 5 tons per hectare. ",
        "Yield": " rice is typically grown in the Jammu region, which is known for its fertile soil and ample water supply. The crop is usually planted in April and harvested in September. The yield per hectare varies depending on the variety of rice and the growing conditions, but it can range from 2 to 5 tons per hectare.",
        
        "author": "Waseem Ahmad"
        }
    ]



    ## Author waseem ## Returning Output
    return render_template('prediction.html', output=prediction, Cherry=Cherry, Walnut=Walnut, Apple=Apple, Almond=Almond, Rice=Rice)
    

if __name__ == '__main__':
    app.run(debug=True)