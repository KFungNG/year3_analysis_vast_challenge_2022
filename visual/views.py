from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'index.html')

def t1_age_vs_edu(request):
    return render(request, 't1/age_vs_edu.html')

def t1_kidsNo_age_edu(request):
    return render(request, 't1/kidsNo_age_edu.html')

def t1_familymemNo_age_edu(request):
    return render(request, 't1/familymemNo_age_edu.html')

def t1_edu_vs_interest(request):
    return render(request, 't1/edu_vs_interest.html')

def t1_class_clustering(request):
    return render(request, 't1/class_clustering.html')

def t1_wealth_vs_joviality(request):
    return render(request, 't1/wealth_vs_joviality.html')

def t1_class_attribute(request):
    return render(request, 't1/class_attribute.html')

def t1_sleeping_status(request):
    return render(request, 't1/sleeping_status.html')

def t1_ageEdu(request):
    return render(request, 't1/ageEdu.html')

def t1_work_time(request):
    return render(request, 't1/work_time.html')

def t2_social_network(request):
    return render(request, 't2/social_network.html')

def t2_lidao(request):
    return render(request, 't2/lidao.html')

def t2_entertainment(request):
    return render(request, 't2/entertainment.html')

def t2_relationship(request):
    return render(request, 't2/relationship.html')

def t2_pub(request):
    return render(request, 't2/pub.html')

def t2_finance_indices_2002(request):
    return render(request, 't2/financial_indices_2002.html')

def t3_seasonal_income(request):
    return render(request, 't3/seasonal_income.html')

def t3_rental_cost(request):
    return render(request, 't3/rental_cost.html')

def t3_restaurant(request):
    return render(request, 't3/restaurant.html')

def t3_clubs(request):
    return render(request, 't3/clubs.html')

def t3_building_type(request):
    return render(request, 't3/building_type.html')

def t3_company_size(request):
    return render(request, 't3/company_size.html')

def t3_building_type2(request):
    return render(request, 't3/building_types.html')

def t3_bar(request):
    return render(request, 't3/bar.html')

def t3_GDP(request):
    return render(request, 't3/GDP.html')

def t3_rent(request):
    return render(request, 't3/rent.html')

def t3_salary(request):
    return render(request, 't3/salary.html')
