from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterationForm, ProfitCenterForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


# @login_required(login_url='login')
def main_index(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('registed'))
            return redirect('login')
    else:
        form = RegisterationForm()
        return render(request, 'register/register.html', {
            'form':form,
        })
    

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("valid User")
            return redirect('main')
        else:
            print("invalid user")
            messages.success(request, ("login error"))
            return redirect('login')
    else:    
        print("User Error")
        return render(request, 'register/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, ("logged out"))
    return redirect('login')




@csrf_exempt
def profit_center(request):
    form = ProfitCenterForm()
    if request.method == "POST":
        form = ProfitCenterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listall')
    context = {"form":form}
    return render(request,'profitcenter.html', context)
    

#view for rendering listall profit center page

def list_all(request):
    profit_objs = ProfitCenter.objects.all()
    return render(request, 'listall.html', {"profit_objs":profit_objs})


#view for rendering and handling update profit center

def update_profit(request, pk):
    profit_obj = ProfitCenter.objects.get(id = pk)
    form = ProfitCenterForm(instance=profit_obj)
    if request.method == "POST":
        form = ProfitCenterForm(request.POST, instance=profit_obj)
        if form.is_valid():
            form.save()
        return redirect('/listall')
    context = {"form":form, "id":pk}
    return render(request, 'update.html', context)


def delete_profit(request, pk):
    profit_obj = ProfitCenter.objects.get(id = pk)
    profit_obj.delete()
    return redirect('/listall')       


# @login_required(login_url='login/')
# @csrf_exempt
# def profitCenterApi(request, id=0):
#     if request.method=='GET':
#         user = BusinessObjective.objects.all()
#         profitcenter_serializers = ProfitCenterSerializer(user, many=True)
#         return JsonResponse(profitcenter_serializers.data, safe=False)
#     elif request.method=='POST':
#         user_data = JSONParser().parse(request)
#         profitcenter_serializers = ProfitCenterSerializer(data=user_data)
#         if profitcenter_serializers.is_valid():
#             profitcenter_serializers.save()
#             return JsonResponse('Added', safe=False)
#         return JsonResponse('not Added', safe=False)
#     elif request.method=='PUT':
#         user_data = JSONParser().parse(request)
#         user = BusinessObjective.objects.get(userId=user_data['userId'])
#         user_serializers = ProfitCenterSerializer(user, data=user_data)
#         if user_serializers.is_valid():
#             user_serializers.save()
#             return JsonResponse('updated', safe=False)
#         return JsonResponse('failed to update',safe=False)
#     elif request.method=='DELETE':
#         user = BusinessObjective.objects.get(userId=id)
#         user.delete()
#         return JsonResponse('deleted', safe=False)
#     return JsonResponse('delete failed', safe=False)


# @login_required(login_url='login/')
# @csrf_exempt
# def bizNeedApi(request, id=0):
#     if request.method=='GET':
#         user = BizNeed.objects.all()
#         profitcenter_serializers = ProfitCenterSerializer(user, many=True)
#         return JsonResponse(profitcenter_serializers.data, safe=False)
#     elif request.method=='POST':
#         user_data = JSONParser().parse(request)
#         profitcenter_serializers = ProfitCenterSerializer(data=user_data)
#         if profitcenter_serializers.is_valid():
#             profitcenter_serializers.save()
#             return JsonResponse('Added', safe=False)
#         return JsonResponse('not Added', safe=False)
#     elif request.method=='PUT':
#         user_data = JSONParser().parse(request)
#         user = BizNeed.objects.get(userId=user_data['userId'])
#         user_serializers = ProfitCenterSerializer(user, data=user_data)
#         if user_serializers.is_valid():
#             user_serializers.save()
#             return JsonResponse('updated', safe=False)
#         return JsonResponse('failed to update',safe=False)
#     elif request.method=='DELETE':
#         user = BizNeed.objects.get(userId=id)
#         user.delete()
#         return JsonResponse('deleted', safe=False)
#     return JsonResponse('delete failed', safe=False)