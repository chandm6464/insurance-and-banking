from django.shortcuts import render
import joblib
import pandas as pd
import datetime
from datetime import date,datetime
import numpy as np

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html') 

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def medical_insurance_premium(request):
    return render(request,'Medical-Insurance-Premium-index.html')

def medical_insurance_premium_result(request):
    model = joblib.load('Medical_Insurance_Premium.sav')
    data = { 
        'Age' : request.POST['Age'],
        'Diabetes' : request.POST['Diabetes'],
        'BloodPressureProblems' : request.POST['Blood Sugar Problems'],
        'AnyTransplants' : request.POST['AnyTransplants'],
        'AnyChronicDiseases' : request.POST['AnyChronicsDiseases'],
        'Height' : request.POST['Height'],
        'Weight' : request.POST['Weight'],
        'KnownAllergies' : request.POST['KnownAllergies'],
        'HistoryOfCancerInFamily' : request.POST['HistoryOfCancerInFamily'],
        'NumberOfMajorSurgeries' : request.POST['NumberOfMajorSurgeries'],
        'AgeLabel_Teen' : 0,
        'AgeLabel_Young' : 0,
        'AgeLabel_Middle' : 0,
        'AgeLabel_Old' : 0,
        'AgeLabel_SuperOld' : 0,
        'PremiumLabel_Low' : 1,
        'PremiumLabel_Basic' : 1,
        'PremiumLabel_Average' : 1,
        'PremiumLabel_High' : 1,
        'PremiumLabel_SuperHigh' :1
    }
    data['AgeLabel_Teen'] = int(int(data['Age'])<=19)
    data['AgeLabel_Young'] = int(int(data['Age'])<=30 and int(data['Age'])>=20)
    data['AgeLabel_Middle'] = int(int(data['Age'])<= 45 and int(data['Age'])>30)
    data['AgeLabel_Old'] = int(int(data['Age'])<=60 and int(data['Age'])>45)
    data['AgeLabel_SuperOld'] = int(int(data['Age'])>60)
    print(data)
    data_frame = pd.DataFrame(data,[1])
    ans=model.predict(data_frame)
    message = "The predicted medical insurance premium of "+str(request.POST['first_name'])+" is $"+str(int(ans[0]))
    app_page = 'Medical-Insurance-Premium'
    return render(request,'result.html',{'message': message , 'app_page': app_page}) 
    

def insurance_company_complaints_index(request):
    return render(request,'Insurance-company-complaints-index.html')   

def insurance_company_complaints_result(request):
    model = joblib.load('Insurance_Company_Complaints.sav')
    data = {
          'Company': 0,
          'Coverage' : request.POST['Coverage'],
          'SubReason' : request.POST['SubReason'],
          'Disposition' : request.POST['Disposition'],
          'Conclusion' : request.POST['Conclusion'],
          'Recovery' : request.POST['Recovery'],
          'year_open' : datetime.fromisoformat(request.POST['Opened']).year,
          'month_open' : datetime.fromisoformat(request.POST['Opened']).month,
          'date_open' : datetime.fromisoformat(request.POST['Opened']).day,
          'year_close' : datetime.fromisoformat(request.POST['Close']).year,
          'month_close' : datetime.fromisoformat(request.POST['Close']).month,
          'date_close' : datetime.fromisoformat(request.POST['Close']).day,
          'status' : 0
         }
    data_frame = pd.DataFrame(data,[1])
    ans = model.predict(data_frame)
    #print(datetime.fromisoformat(request.POST['Opened']).year)
    message = "The Reason for the closure of the company "+str(request.POST['Company']).upper()+" is "+str(ans[0]).upper()   
    return render(request,'result.html',{'message' : message})
    return render(request,'Insurance-company-complaints-index.html') 

def customer_life_time_value_index(request):
    return render(request,'Customer-life-time-value-index.html')   

def customer_life_time_value_result(request):
    model = joblib.load('LTV_PRediction.sav')
    data={
        'Coverage' : request.POST['Coverage'],
        'Monthly Premium Auto' : request.POST['Monthly Premium Auto'],
        'Number of Policies' : request.POST['Number of Policies'],
        'Renew Offer Type' : request.POST['Renew Offer Type'],
        'Total Claim Amount' : request.POST['Total Claim Amount'],
        'Vehicle Class' : request.POST['Vehicle Class'],
        'Number of Open Complaints' : request.POST['Number of open Complaints']
    }
    data_frame = pd.DataFrame(data,[1])
    ans = model.predict(data_frame)
    message = "The estimated Life Time Value of "+str(request.POST['first_name'])+" is $"+str(int(ans[0]))
    return render(request,'result.html',{'message': message})
    

def credit_card_fraud_index(request):
    return render(request, 'Credit-card-fraud-index.html')

def credit_card_fraud_result(request):
    today = date.today()
    #print(today)
    #print((request.GET['trans_hour'] )[0:2])
    
    model=joblib.load('Credit_card_fraud.sav')
    data = { 
          'amt'                    : request.POST['amt'],
          'city_pop'               : request.POST['city_pop'],
          'trans_hour'             : (request.POST['trans_hour'] )[0:2],
          'age'                    : int((today - date.fromisoformat(request.POST['DAYS_BIRTH'] )).days),
          'category_food_dining'   : 0, 
          'category_gas_transport' : 0, 
          'category_grocery_net'   : 0, 
          'category_grocery_pos'   : 0, 
          'category_health_fitness': 0,
          'category_home'          : 0, 
          'category_kids_pets'     : 0, 
          'category_misc_net'      : 0, 
          'category_misc_pos'      : 0, 
          'category_personal_care' : 0, 
          'category_shopping_net'  : 0,
          'category_shopping_pos'  : 0, 
          'category_travel'        : 0, 
          'gender_M'               : 0, 
          'week_Monday'            : 0, 
          'week_Tuesday'           : 0, 
          'week_Wednesday'         : 0, 
          'week_Thursday'          : 0, 
          'week_Saturday'          : 0, 
          'week_Sunday'            : 0
         } 
    
    data=pd.DataFrame(data,[1])
    if request.POST['gender']=='1':
        data['gender_M']=1
        
    if request.POST['category']=='1':
        data['category_misc_net']=1
    elif request.POST['category']=='2':
        data['category_grocery_pos']=1
    elif request.POST['category']=='4':
        data['category_gas_transport']=1
    elif request.POST['category']=='5':
        data['category_misc_pos']=1
    elif request.POST['category']=='6':
        data['category_grocery_net' ]=1
    elif request.POST['category']=='7':
        data['category_shopping_net']=1
    elif request.POST['category']=='8':
        data['category_shopping_pos']=1
    elif request.POST['category']=='9':
        data['category_food_dining']=1
    elif request.POST['category']=='10':
        data['category_personal_care']=1
    elif request.POST['category']=='11':
        data['category_health_fitness']=1
    elif request.POST['category']=='12':
        data['category_travel']=1
    elif request.POST['category']=='13':
        data['category_kids_pets']=1
    elif request.POST['category']=='14':
        data['category_home']=1
    

    if request.POST['Day_Of_Week']=='1':
        data['week_Monday']=1
    elif request.POST['Day_Of_Week']=='2':
        data['week_Tuesday']=1
    elif request.POST['Day_Of_Week']=='3':
        data['week_Wednesday']=1
    elif request.POST['Day_Of_Week']=='4':
        data['week_Thursday']=1
    elif request.POST['Day_Of_Week']=='6':
        data['week_Saturday']=1
    elif request.POST['Day_Of_Week']=='7':
        data['week_Sunday']=1
        



    print(int(data['age']))
    output=model.predict(data)
    if output[0]==0:
        message="Fraud not Detected!!"
    else:
        message="Fraud Detected!!"

    

    return render(request,'result.html',{'message': message})  
    return render(request, 'Credit-card-fraud-result.html') 

def credit_card_approval_index(request):
    return render(request,'Credit-card-approval-index.html')    

def credit_card_approval_result(request):
    model = joblib.load('Credit_card_approval.sav')
    dob = datetime.fromisoformat(request.POST['DAYS_BIRTH'])
    doj = datetime.fromisoformat(request.POST['DAYS_EMPLOYED'])
    doa = datetime.fromisoformat(request.POST['MONTHS_BALANCE'])
    today = datetime.today()
    days_birth = today-dob
    days_employed = today-doj
    months_balance = today-doa
    data={
        'FLAG_OWN_CAR'  :request.POST['FLAG_OWN_CAR'],
        'FLAG_OWN_REALTY'  : request.POST['FLAG_OWN_REALTY'],
        'AMT_INCOME_TOTAL' : request.POST['AMT_INCOME_TOTAL'],
        'NAME_INCOME_TYPE'  : request.POST['NAME_INCOME_TYPE'],
        'NAME_EDUCATION_TYPE' : request.POST['NAME_EDUCATION_TYPE'],
        'NAME_HOUSING_TYPE'  : request.POST['NAME_HOUSING_TYPE'],
        'DAYS_BIRTH'  : -1*days_birth.days,
        'DAYS_EMPLOYED'  : -1*days_employed.days,
        'OCCUPATION_TYPE' :request.POST['OCCUPATION_TYPE'],
        'CNT_FAM_MEMBERS'  : request.POST['CNT_FAM_MEMBERS'],
        'MONTHS_BALANCE'  : int((-1*months_balance.days)/30)
       }
     
    data_frame = pd.DataFrame(data,[1])
    ans = model.predict(data_frame)
    if ans[0] == 1:
        message = str(request.POST['first_name'])+" can be approved a credit card"
    else:
        message = str(request.POST['first_name'])+" cannot be approved a credit card"    
    return render(request,'result.html',{'message': message.upper()})
    return render(request,'Credit-card-approval-index.html')        

def home_loan_prediction_index(request):
    return render(request,'Home-Loan-Prediction-index.html')

def home_loan_prediction_result(request):
    model = joblib.load('Home_Loan_Model.sav')
    data={
        'Loan_ID':request.POST['Loan_ID'],
        'ApplicantIncome':request.POST['ApplicantIncome'],
        'CoapplicantIncome':request.POST['CoapplicantIncome'],
        'LoanAmount':request.POST['LoanAmount'],
        'Loan_Amount_Term':request.POST['Loan_Amount_Term'],
        'Credit_History':request.POST['Credit_History'], 
        #'Property_Area':request.POST['Property_Area'],
        'Gender_Female':0,
        'Gender_Male':0,
        'Married_No':0,
        'Married_Yes':0,
        'Dependents_0':0,
        'Dependents_1':0,
        'Dependents_2':0,
        'Dependents_3':0,
        'Education_Graduate':0,
        'Education_Not Graduate':0,
        'Self_Employed_No':0,
        'Self_Employed_Yes':0,
        'Property_Area_Rural':0,
        'Property_Area_Semiurban':0,
        'Property_Area_Urban':0
    }
    data=pd.DataFrame(data,[1])
    #print(data)
    
    data['LoanAmount_log'] = np.log(int(data['LoanAmount']))
    data["TotalIncome"]=int(data["ApplicantIncome"])+int(data["CoapplicantIncome"])
    data["TotalIncome_log"] = np.log(int(data["TotalIncome"]))
    data["EMI"]=int(data["LoanAmount"])/int(data["Loan_Amount_Term"])
    data["Balance_Income"] = int(data["TotalIncome"])-int(data["EMI"])
    data = data.drop(["ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Loan_ID"],axis=1)
    #print(data)
    if request.POST['Gender']=="Male":
        
        data['Gender_Male']=1
    else:
        data['Gender_Female']=1

    if request.POST['Married']=="Yes":
        data['Married_Yes']=1
    else:
        data['Married_No']=1



    if request.POST['Dependents']=="0":
        data['Dependents_0']=1
    elif request.POST['Dependents']=="1":
        data['Dependents_1']=1
    elif request.POST['Dependents']=="2":
        data['Dependents_2']=1
    else:
         data['Dependents_3']=1

    if request.POST['Education']=="Graduate":
        data['Education_Graduate']=1
    else:
        data['Education_Not Graduate']=1
    
    if request.POST['Self_Employed']=="Yes":
        data['Self_Employed_Yes']=1
    else:
        data['Self_Employed_No']=1
    
    

    if request.POST['Property_Area']== "Urban":
        data['Property_Area_Urban']=1
    elif request.POST['Property_Area']=="Semiurban":
        data['Property_Area_Semiurban']=1
    else:
        data['Property_Area_Rural']=1
        

    #print(data)    
    output=model.predict(data)
    if output[0]==0:
        message=str(request.POST['first_name'])+ " is most likely to not get a Home Loan"
    else:
        message=str(request.POST['first_name'])+" is most likely get the Home Loan"


    return render(request,'result.html',{'message':message})    
    return render(request,'Home-loan-prediction-index.html')    

def bank_customer_churn_prediction_index(request):
    return render(request, 'Bank-Customer-Churn-Prediction-index.html')    

def bank_customer_churn_prediction_result(request):
    model= joblib.load('Bank_Customer_Churn_Model.sav')
    data={
        'CreditScore': request.POST['CreditScore'],
        'Age' : request.POST['Age'],
        'Tenure': request.POST['Tenure'],
        'Balance' : request.POST['Balance'],
        'NumOfProducts':  request.POST['NumOfProducts'],
        'EstimatedSalary': request.POST['EstimatedSalary'],
        'Geography_Spain':-1,
        'Geography_France':-1,
        'Geography_Germany':-1,
        'Gender_Female':-1,
        'Gender_Male':-1
    }
    data['BalanceSalaryRatio'] = int(data['Balance'])/int(data['EstimatedSalary'])
    data['TenureByAge'] = int(data['Tenure'])/int(data['Age'])
    data['CreditScoreGivenAge'] = int(data['CreditScore'])/int(data['Age'])

    if request.POST['HasCrCard']=="Yes":
        data['HascrCard']=1
    
    if request.POST['IsActiveMember']=="Yes":
        data['IsActiveMember']=1
    
    if request.POST['Country'] =="France":
        data['Geography_France']=1
    elif request.POST['Country']=="Germany":
        data['Geography_Germany']=1
    else:
        data['Geography_Spain']=1

    if request.POST['Gender']=="Male":
        data['Gender_Male']=1
    else:
        data['Gender_Female']=1
    print(data)
    data_frame = pd.DataFrame(data,[1])
    output=model.predict(data_frame)
    print(output)
    if output[0] == 0:
        message = str(request.POST['first_name'])+" is most likely to exit"
    else:
        message = str(request.POST['first_name'])+" is most likely to be retained"    
    return render(request,'result.html',{'message': message})

    return render(request, 'Bank-Customer-Churn-Prediction-index.html')

   


      

       
