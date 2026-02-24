from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        "title":"home page",
        "bdata":"Welcome To My Website",
        "student_details":[
            {"no":1,"name":"ankit savita","phone":8957544752},
            {"no":2,"name":"mohit savita","phone":7235033878},
        ]
    }
    return render(request,"index.html",data)
    
def aboutus(request):
    return HttpResponse("welcome to ankitswebsite")

def course(request):
    return HttpResponse("welcome to firstproject")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

