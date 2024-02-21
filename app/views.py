from django.shortcuts import render
import random, qrcode




def openLoginPage(request):
    return render(request, "Login.html")


def validateuser(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "oleg" and password == "123":
        rno = random.randint(10000, 9999999)
        global otp
        otp = rno
        im = qrcode.make(str(rno))
        im.save(r"app/static/qrimages/qrimg.jpg")
        return render(request, "qrcode_page.html")
    else:
        return render(request, "login.html", {"message": "Invalid User"})


def validateOTP(request):
    user_otp = request.POST.get("otp")
    if user_otp == str(otp):
        return render(request, "welcome.html")
    else:
        return render(request, "login.html", {"message": "Invalid OTP"})
