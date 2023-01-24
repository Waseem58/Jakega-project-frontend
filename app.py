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
        
        {"Title": "Paddy",
        "Description": " Rice is a staple crop grown in many parts of the world, including the region of Kashmir. It is a semi-aquatic grass that is typically grown in flooded fields, or paddies. The plant requires a warm climate and plenty of water to grow successfully. ",
        "Production": " rice is typically grown in the Jammu region, which is known for its fertile soil and ample water supply. The crop is usually planted in April and harvested in September. The yield per hectare varies depending on the variety of rice and the growing conditions, but it can range from 2 to 5 tons per hectare. ",
        "Yield": " rice is typically grown in the Jammu region, which is known for its fertile soil and ample water supply. The crop is usually planted in April and harvested in September. The yield per hectare varies depending on the variety of rice and the growing conditions, but it can range from 2 to 5 tons per hectare.",
        
        "author": "Waseem Ahmad"
        }
    ]


    Mustard = [
        
        {"Title": "Mustard",
        "Description": " Mustard is a crop that is grown in many regions of the world, including the state of Jammu and Kashmir in India. It is a cool-season crop that is typically planted in the fall and harvested in the spring. The main commercial varieties grown in Jammu and Kashmir are yellow sarson and toria. ",
        "Production": " The crop is grown on a variety of soils, such as clay loam, sandy loam and loamy sand. The state has a good potential for mustard cultivation as the agro-climatic conditions are suitable for its growth. In terms of production, mustard is a major crop in the state of Jammu and Kashmir, with a significant area under cultivation.",
        "Yield": " The yield of mustard in Jammu and Kashmir varies depending on the variety and the growing conditions, but it can be quite high. In recent year, the average yield of mustard in the state was around 1,000-1,500 kg per hectare.py",
        
        "author": "Waseem Ahmad"
        }
    ]


    Mushroom = [
        
        {"Title": "Mushroom",
        "Description": " Mushroom cultivation is an important agricultural activity in the Indian state of Jammu and Kashmir. The most commonly cultivated mushroom in the region is the Agaricus bisporus, also known as the white button mushroom. This mushroom is grown in caves, sheds and tunnels, and is produced year-round.  ",
        "Production": " Mushroom production involves growing edible mushrooms for consumption. This can be done in a variety of settings, including indoor and outdoor farms, as well as in home gardens. The most common types of mushrooms grown commercially include white button, shiitake, and oyster mushrooms. The process of mushroom cultivation typically involves preparing a substrate, such as straw or sawdust, inoculating it with mushroom spores or spawn, and providing the right conditions for the mushrooms to grow. Factors that can affect mushroom production include temperature, humidity, light, and air circulation.",
        "Yield": " The yield of the crop depends on various factors such as the cultivation method, the strain of mushroom being grown, and the environmental conditions. In general, yields of around 15-20 kg of mushrooms per square meter per year are typical. The mushroom cultivation in kashmir has good market potential due to its high nutritional value, low calorie content and medicinal properties.",
        
        "author": "Waseem Ahmad"
        }
    ]



    
    Pulses = [
        
        {"Title": "Pulses",
        "Description": " Pulses are a type of legume that are commonly grown for their protein-rich seeds. They include crops such as lentils, peas, and chickpeas. In the context of Kashmir, pulses are an important crop for farmers as they provide a source of food and income. ",
        "Production": " the pulse production in the region is increasing due to the adoption of new technologies and farming practices that can help improve yields. For example, farmers are using improved seed varieties, irrigation systems, and crop management techniques to boost their yields.",
        "Yield": " The yield of pulses in Kashmir can vary depending on factors such as weather conditions, soil quality, and farming practices. However, the yield is generally considered to be lower compared to other regions in India due to the harsh weather conditions and less favorable soil quality.",
        
        "author": "Waseem Ahmad"
        }
    ]




    Peach = [
        
        {"Title": "Peach",
        "Description": " Peaches are a type of fruit that belong to the rose family. They have a fuzzy skin and a sweet, juicy flesh. They are typically round in shape and can vary in color from yellow to red.",
        "Production": " In the context of Kashmir, peach production is a major agricultural industry. The region has a suitable climate and soil for growing peaches, and the fruit is a popular crop among farmers. Peach orchards are found throughout the region, and the fruit is typically harvested during the summer months.",
        "Yield": " The yield of peaches in Kashmir can vary depending on factors such as weather conditions and farming practices. However, the region is known for producing high-quality peaches with a sweet taste.",
        
        "author": "Waseem Ahmad"
        }
    ]




    Plum = [
        
        {"Title": "Plum",
        "Description": " The plum is a small, round fruit that is typically red, purple, or yellow in color. It is a member of the rose family and is related to other fruits such as peaches, apricots, and cherries.",
        "Production": " In the context of Kashmir, plums are grown primarily in the southern regions of the state. The fruit is known for its sweet and juicy taste, and is often used for making jams, jellies, and preserves. Plum production in Kashmir is largely done on a small scale, with most farmers cultivating the fruit on their own land. The yield of plums in Kashmir can vary depending on factors such as weather conditions, soil quality, and farming practices. However, generally the yield is considered to be moderate.",
        "Yield": " The yield of plums in Kashmir can vary depending on factors such as weather conditions and farming practices. However, the region is known for producing high-quality peaches with a sweet taste.",
        
        "author": "Waseem Ahmad"
        }
    ]



    Pear = [
        
        {"Title": "Pear",
        "Description": " The pear is a type of fruit that belongs to the Rosaceae family, which also includes other fruits such as apples and peaches. Pears are typically round or bell-shaped and have a smooth, skin that can be green, yellow, or red in color. The flesh of a pear is juicy and sweet, and it has a small core in the center that contains the seeds.",
        "Production": " In the context of Kashmir, pears are grown mainly in the Srinagar and Shopian districts. The main variety of pear grown in the region is 'Williams', which is known for its large size and sweet taste. The pear trees are grown on a small scale, mostly by local farmers. The fruit is typically harvested in the months of August and September.",
        "Yield": "The yield of pears in Kashmir can vary depending on the growing conditions and the specific variety of pear being grown. However, the overall yield tends to be low compared to other fruit-producing regions due to the hilly terrain and lack of modern agricultural practices. Additionally, the pear fruit is prone to various pests and diseases which also affects the yield. ",
        
        "author": "Waseem Ahmad"
        }
    ]







    ## Author waseem ## Returning Output
    return render_template('prediction.html', output=prediction, Cherry=Cherry, Walnut=Walnut, Apple=Apple, Almond=Almond, Rice=Rice, Mustard=Mustard, Mushroom=Mushroom, Pulses=Pulses, Peach=Peach, Plum=Plum, Pear=Pear)
    

if __name__ == '__main__':
    app.run(debug=True)