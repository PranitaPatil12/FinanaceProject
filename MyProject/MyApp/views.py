from django.shortcuts import render

def homeView(request):
    return render(request,"index.html")

def eligibility_view(request):
    return render(request, "eligibility.html")

def nav_view(req):
    return render(req,'navbar_loan.html')

def feature_view(req):
    return render(req,'features.html')

def fees_charges_view(req):
    return render(req,'fees_charges.html')

def req_doc_view(req):
    return render(req,'RequiredDocs.html')