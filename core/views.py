from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='login')
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



@login_required(login_url='login')
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


@login_required(login_url='login')
@csrf_exempt
def business_objective(request):
    form = BussinessObjectiveForm()
    if request.method == "POST":
        form = BussinessObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listbusiness')
    context = {"form":form}
    return render(request,'businessobjective.html', context)
    

#view for rendering listall profit center page

def business_objective_list(request):
    profit_objs = BusinessObjective.objects.all()
    return render(request, 'businesslist.html', {"profit_objs":profit_objs})


#view for rendering and handling update profit center

def update_business_objective(request, pk):
    profit_obj = BusinessObjective.objects.get(id = pk)
    form = BussinessObjectiveForm(instance=profit_obj)
    if request.method == "POST":
        form = BussinessObjectiveForm(request.POST, instance=profit_obj)
        if form.is_valid():
            form.save()
        return redirect('/listall')
    context = {"form":form, "id":pk}
    return render(request, 'business_update.html', context)


def delete_business_objective(request, pk):
    profit_obj = BusinessObjective.objects.get(id = pk)
    profit_obj.delete()
    return redirect('/listbusiness')       


@login_required(login_url='login')
@csrf_exempt
def bizneed(request):
    form = BizNeedForm()
    if request.method == "POST":
        form = BizNeedForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listbizneed')
    context = {"form":form}
    return render(request,'bizneed.html', context)
    

#view for rendering listall profit center page

def list_bizneed(request):
    profit_objs = BizNeed.objects.all()
    return render(request, 'listbizneed.html', {"profit_objs":profit_objs})


#view for rendering and handling update profit center

def update_bizneed(request, pk):
    profit_obj = BizNeed.objects.get(id = pk)
    form = BizNeedForm(instance=profit_obj)
    if request.method == "POST":
        form = BizNeedForm(request.POST, instance=profit_obj)
        if form.is_valid():
            form.save()
        return redirect('/listbizneed')
    context = {"form":form, "id":pk}
    return render(request, 'bizneed_update.html', context)


def delete_bizneed(request, pk):
    profit_obj = BizNeed.objects.get(id = pk)
    profit_obj.delete()
    return redirect('/listbizneed')       

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
