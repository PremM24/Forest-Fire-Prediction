

import numpy as np
import pandas as pd
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import pickle


                  
password_list=[]
password_list1=[]
username_list=[]
username_list1=[]




from flask import Flask, request, jsonify, render_template

import joblib


# Load the model from the file 
model = joblib.load('forest_fire.pkl') 


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('register.html')


@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]

    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    r3=int_features2[2]
    print(r3)
    name=int_features2[0]
    username=int_features2[1]
    passw1=int_features2[2]
        
    

    


    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"database" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT username FROM user_register")
    result1=cursor.fetchall()

    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      username_list1.append(str(row1[0]))
                      

                      
    print(username_list1)
    if username in username_list1:
                      
                      return render_template('register.html',text="This Username is Already in Use ")
    else:

                 
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(name,username,password) VALUES (%s,%s,%s)"
                  val = (r1,r2,r3)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                  
                  return render_template('register.html',text="Succesfully Registered")



                      
                      
@app.route('/login')
def login(): 
    return render_template('login.html')         
                      

@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]


    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","database" )
  
# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT username FROM user_register")
    result1=cursor.fetchall()

            
    for row2 in result1:
                      print(row2)
                      print(row2[0])
                      username_list.append(str(row2[0]))
                      
              
                      
    print(username_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
             
    for row3 in result2:
                      print(row3)
                      print(row3[0])
                      password_list.append(str(row3[0]))
                      
                 
                      
    print(password_list)

    if((logu not in username_list) or (passw not in password_list)):
        return render_template('login.html',text='Use Proper Username and Password')
    elif(username_list.index(logu)==password_list.index(passw)):
        return render_template('index1.html')
    else:
        return render_template('login.html',text='Use Proper Username and Password')
        
                  




@app.route('/production')
def production(): 
    return render_template('index1.html')


@app.route('/production/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [str(x) for x in request.form.values()]
    a=int_features

  

    data = {'Oxygen':[float(a[2])],'Temperature':[float(a[0])],'Humidity':[float(a[1])]} 
  
# Create DataFrame 
    df = pd.DataFrame(data)
    print(df)



    prediction=model.predict_proba(df)
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    print(output)
    output=str(output)
    output=float(output)
    fire=output*100


    if(fire <=100 and fire >= 90):
        print("The place is in Danger!! The percentage of  forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='The place is in Danger!! The percentage of  forest fire occurence in the area is {:.2f}%'.format(fire))

    elif(fire < 90 and fire >= 80):
        print("The place is in Danger!!! The percentage of  forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='The place is in Danger!! The percentage of  forest fire occurence in the area is {:.2f}%'.format(fire))
                           
    elif(fire < 80 and fire >= 70):
        print("Don't ever let fire to grow! The percentage of  forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='Do not ever let fire to grow! The percentage of  forest fire occurence in the area is {:.2f}%'.format(fire))
                              
    elif(fire< 70 and fire >= 60):
        print("Don't ever let fire to grow! The percentage of  forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='Do not ever let fire to grow! The percentage of  forest fire occurence in the area is {:.2f}%'.format(fire))
                               
    elif(fire< 60 and fire > 50):
        print("Fire prevention is the only option! The percentage of forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='Fire prevention is the only option! The percentage of forest fire occurence in the area is {:.2f}%'.format(fire))
                               
    elif(fire <= 50 and fire >40):
        print("Fire prevention is the only option! The percentage of forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='Fire prevention is the only option! The percentage of forest fire occurence in the area is  {:.2f}%'.format(fire))

    elif(fire < 40 and fire >= 30):
        print("Small fire will be tall soon! The percentage of forest fire occurence in the area is " , fire )
        return render_template('index1.html',prediction_text='Small fire will be tall soon ! The percentage of forest fire occurence in the area is {:.2f}%'.format(fire))

    else:
        print("Think of fire before it starts! The percentage of forest fire occurence in the area is " , fire)
        return render_template('index1.html',prediction_text='Think of fire before it starts! The percentage of forest fire occurence in the area is {:.2f}%'.format(fire))



if __name__ == "__main__":
    app.run(debug=False)
