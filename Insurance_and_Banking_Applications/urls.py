"""Insurance_and_Banking_Applications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('team/',views.team,name="team"),
    path('medical-insurance-premium/',views.medical_insurance_premium,name="Medical-Insurance-Premium"),
    path('medical-insurance-premium-result/',views.medical_insurance_premium_result,name="medical-insurance-premium-result"),
    path('Insurance-company-complaints-index/',views.insurance_company_complaints_index,name="Insurance-company-complaints-index"),
    path('Insurance-company-complaints-result/',views.insurance_company_complaints_result,name="Insurance-company-complaints-result"),
    path('Customer-life-time-value-index/',views.customer_life_time_value_index,name="Customer-life-time-value-index"),
    path('Customer-life-time-value-result/',views.customer_life_time_value_result,name="Customer-life-time-value-result"),
    path('Credi-card-fraud-detection',views.credit_card_fraud_index,name="Credit-card-fraud-index"),
    path('Credit-card-fraud-result',views.credit_card_fraud_result,name="Credit-card-fraud-result"),
    path('Credit-card-approval-index/',views.credit_card_approval_index,name="Credit-card-approval-index"),
    path('Credit-card-approval-result/',views.credit_card_approval_result,name="Credit-card-approval-result"),
    path('Home-loan-prediction-index/',views.home_loan_prediction_index,name="Home-loan-prediction-index"),
    path('Home-loan-prediction-result/',views.home_loan_prediction_result,name="Home-loan-prediction-result"),
    path('Bank-Customer-Churn-Prediction-index/',views.bank_customer_churn_prediction_index,name="Bank-Customer-Churn-Prediction-index"),
    path('Bank-Customer-Churn-Prediction-result/',views.bank_customer_churn_prediction_result,name="Bank-Customer-Churn-Prediction-result"),
]
