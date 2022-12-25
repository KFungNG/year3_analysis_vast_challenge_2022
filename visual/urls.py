from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.mainpage),
    path('t1/age_vs_edu/', views.t1_age_vs_edu),
    path('t1/kidsNo_age_edu/', views.t1_kidsNo_age_edu),
    path('t1/familymemNo_age_edu/', views.t1_familymemNo_age_edu),
    path('t1/edu_vs_interest/', views.t1_edu_vs_interest),
    path('t1/class_clustering/', views.t1_class_clustering),
    path('t1/wealth_vs_joviality/', views.t1_wealth_vs_joviality),
    path('t1/class_attribute/', views.t1_class_attribute),
    path('t1/sleeping_status/', views.t1_sleeping_status),
    path('t1/ageEdu/', views.t1_ageEdu),
    path('t1/work_time/', views.t1_work_time),
    path('t2/social_network/', views.t2_social_network),
    path('t2/lidao/', views.t2_lidao),
    path('t2/entertainment/', views.t2_entertainment),
    path('t2/relationship/', views.t2_relationship),
    path('t2/pub/', views.t2_pub),
    path('t2/financial_indices_2002/', views.t2_finance_indices_2002),
    path('t3/seasonal_income/', views.t3_seasonal_income),
    path('t3/rental_cost/', views.t3_rental_cost),
    path('t3/restaurant/', views.t3_restaurant),
    path('t3/clubs/', views.t3_clubs),
    path('t3/building_type/', views.t3_building_type),
    path('t3/company_size/', views.t3_company_size),
    path('t3/building_types/', views.t3_building_type2),
    path('t3/bar/', views.t3_bar),
    path('t3/GDP/', views.t3_GDP),
    path('t3/salary/', views.t3_salary),
    path('t3/rent/', views.t3_rent),

]
