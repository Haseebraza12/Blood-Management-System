from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from blood import forms as bforms
from blood import models as bmodels

def ngo_signup_view(request):
    userForm=forms.NgoUserForm()
    ngoForm=forms.NgoForm()
    mydict={'userForm':userForm,'ngoForm':ngoForm}
    if request.method=='POST':
        userForm=forms.NgoUserForm(request.POST)
        ngoForm=forms.NgoForm(request.POST,request.FILES)
        if userForm.is_valid() and ngoForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            ngo=ngoForm.save(commit=False)
            ngo.user=user
            ngo.bloodgroup=ngoForm.cleaned_data['bloodgroup']
            ngo.save()
            my_donor_group = Group.objects.get_or_create(name='NGO')
            my_donor_group[0].user_set.add(user)
        return HttpResponseRedirect('ngologin')
    return render(request,'ngo/donorsignup.html',context=mydict)


def ngo_dashboard_view(request):
    donor= models.Ngo.objects.get(user_id=request.user.id)
    dict={
        'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_ngo=donor).filter(status='Pending').count(),
        'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_ngo=donor).filter(status='Approved').count(),
        'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_ngo=donor).count(),
        'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_ngo=donor).filter(status='Rejected').count(),
    }
    return render(request,'ngo/donor_dashboard.html',context=dict)


def ngo_blood_view(request):
    donation_form=forms.DonationForm()
    if request.method=='POST':
        donation_form=forms.DonationForm(request.POST)
        if donation_form.is_valid():
            blood_donate=donation_form.save(commit=False)
            blood_donate.bloodgroup=donation_form.cleaned_data['bloodgroup']
            ngo= models.Ngo.objects.get(user_id=request.user.id)
            blood_donate.ngo=ngo
            blood_donate.save()
            return HttpResponseRedirect('donation-history')  
    return render(request,'ngo/donate_blood.html',{'donation_form':donation_form})

def donation_history_view(request):
    ngo= models.Ngo.objects.get(user_id=request.user.id)
    donations=models.BloodDonate.objects.all().filter(ngo=ngo)
    return render(request,'ngo/donation_history.html',{'donations':donations})

def make_request_view(request):
    request_form=bforms.RequestForm()
    if request.method=='POST':
        request_form=bforms.RequestForm(request.POST)
        if request_form.is_valid():
            blood_request=request_form.save(commit=False)
            blood_request.bloodgroup=request_form.cleaned_data['bloodgroup']
            donor= models.Ngo.objects.get(user_id=request.user.id)
            blood_request.request_by_ngo=donor
            blood_request.save()
            return HttpResponseRedirect('request-history')  
    return render(request,'ngo/makerequest.html',{'request_form':request_form})

def request_history_view(request):
    donor= models.Ngo.objects.get(user_id=request.user.id)
    blood_request=bmodels.BloodRequest.objects.all().filter(request_by_ngo=donor)
    return render(request,'ngo/request_history.html',{'blood_request':blood_request})
