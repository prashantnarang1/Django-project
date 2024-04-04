from django.shortcuts import render, HttpResponse,redirect

from gundepot.models import User,Product,Cart,Order

from django.contrib.auth import authenticate,login,logout

from django.db.models import Q

import random

import razorpay

# Create your views here.


def home(request):

    context={}
    p=Product.objects.filter(is_active=True)
    print(p)
    context['products']=p
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def product_details(request,pid):

    context={}
    p=Product.objects.filter(id=pid)
    context['products']=p
    
    return render(request,"product_details.html",context)



def register(request):

    context={}

    if request.method == 'POST':
        name=request.POST["uemail"]
        
        upass=request.POST["upass"]
        cpass=request.POST["ucpas"]

        if name=="" or  upass=="" or cpass=="":
            context["errormsg"]="Field set cannot be empty"
            return render(request,"register.html",context)
        
        elif upass!= cpass:
            context["errormsg"]="Password did not match"
            return render(request,"register.html",context)
        
        else:
            try:
                u=User.objects.create(username=name,password=upass)
                u.set_password(upass)
                u.save()

                context["successmsg"]="User created successfully"
                return render(request,"register.html",context)
            except Exception:
                context["errormsg"]="User already exist"
                return render(request,"register.html",context)
            
    else:
        return render(request,"register.html")



def user_login(request):    

    if request.method == 'POST':
        context={}
        
        name=request.POST["uemail"]
        upass=request.POST["upass"]
        

        if  name=="" or upass=="" :
            context["errormsg"]="Field set cannot be empty"
            return render(request,"register.html",context)
        
        else:
            u=authenticate(username=name,password=upass)

            if u is not None:

                login(request,u)

                return redirect("/home")
            
            else:
                context["errormsg"]="Invalid username or password"
                return render(request,"login.html",context)
            
    else:
        return render(request,"login.html")
    

def user_logout(request):
    logout(request)
    return redirect("/home")


def addtocart(request,pid):

    if request.user.is_authenticated:

        userid=request.user.id

        u=User.objects.filter(id=userid)
        print(u[0])

        p=Product.objects.filter(id=pid)
        print(p[0])

        c=Cart.objects.create(uid=u[0],pid=p[0])
        c.save()

        
        return redirect("/viewcart")
    
    else:
        return redirect("/login")
    

def viewcart(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    s=0
    np=len(c)

    for x in c:
        s=s+x.pid.price *x.qty                           
    context={}
    context['n']=np
    context['products']=c
    context['total']=s
    return render(request,"cart.html",context)


def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect("/viewcart")

def updateqty(request,qv,cid):


    c=Cart.objects.filter(id=cid)
    if qv == '1':
        t= c[0].qty+1
        c.update(qty=t)

    else:
        if c[0].qty > 1 :
            t=c[0].qty-1
            c.update(qty=t)

    return redirect("/viewcart")


def placeorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)
    print('orderid',oid)
    #print(c)
    
    for x in c:
        #print(x)
        #print(x.pid)
        #print(x.uid)
        #print(x.qty)
        
        o=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        o.save()
        x.delete()

    orders=Order.objects.filter(uid=request.user.id)
    
    s=0
    np=len(c)

    for x in c:
                 
        s=s+x.pid.price *x.qty                           
        context={}
        context['n']=np
        context['products']=c
        context['total']=s
    return render(request,"place_order.html",context)


def catfilter(request,cv):
    q1=Q(is_active=True)

    q2=Q(category=cv)

    p=Product.objects.filter(q1 & q2)
    print(p)
    context={}

    context["products"]=p
    return render(request,"home.html",context)

def sort(request,abc):
    if abc == '0':
        col = 'price'
    
    else:
        col='-price'

    p=Product.objects.filter(is_active=True).order_by(col)

    context={}
    context['products']=p
    return render(request,"home.html",context)

def range(request):
    min=request.GET['umin']
    max=request.GET['umax']
    

    q1=Q(price__gte = min)
    q2=Q(price__lte = max)
    q3=Q(is_active=True)

    p=Product.objects.filter(q1 & q2 & q3)
    print(p)
    context={}
    context['products']=p
    return render(request,"home.html",context)

def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    
    s=0
    

    for x in orders:
                 
        s=s+x.pid.price *x.qty 
        oid=x.order_id


    
    client = razorpay.Client(auth=("rzp_test_WujqEP9Z799fL2", "vlG0X3XWWfrYeaNavXdkxQTZ"))

    data = { "amount": s, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)

    print(payment)
    context={}
    context["data"]=payment
    return render(request,"pay.html",context)
            



        
        


    

