from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Courses, Register, Trainer, Payments, Attendance
from django.contrib import messages
# Create your views here.


def index(request):

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phone')
        desc = request.POST.get('desc')
        contac = Contact(name=name, email=email, phone=phoneNo, description=desc)
        contac.save()
        messages.success(request, 'Thank you for reaching out to us, we will get back to you as soon as possible')
        return redirect('index')
    return render(request, 'contact.html')


def courses(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)


def course(request, course_name):
    courses = Courses.objects.filter(pk=course_name)
    print(courses)
    return render(request, 'course.html', {'courses': courses})


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Login or Register with us')
        return redirect('handle_login')
    courses = Courses.objects.all

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('num')
        alternative_number = request.POST.get('altnum')
        email = request.POST.get('email')
        college_name = request.POST.get('cname')
        address = request.POST.get('address')
        street = request.POST.get('street')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        computer_knowledge = request.POST.get('cmp')
        course = request.POST.get('scourse')
        emailPresent = Register.objects.filter(email=email)
        if emailPresent:
            messages.error(request, 'Email is already taken')
            return redirect('enroll')
        query = Register(first_name=fname, last_name=lname, Phone_number=phone, alternate_number=alternative_number,
                         email=email, college_name=college_name, address=address, street=street, city=city, pincode=pin,
                         computer_knowledge=computer_knowledge, course=course)
        query.save()
        messages.success(request, 'You have been successfully enrolled')
        return redirect('candidate_profile')

    return render(request, 'enroll.html', {'courses': courses})


def candidate_profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, ' Please Login to View Your Profile')
        return redirect('handle_login')
    current_user = request.user.username
    print(current_user)
    details = Register.objects.get(email=current_user)
    payment = Payments.objects.all()
    paymentstatus = ""
    amount = 0
    balance = 0
    for j in payment:
        if str(j.name) == current_user:
            paymentstatus = j.status
            amount = j.amount_paid
            balance = j.balance
    paymentstats = {'paymentstatus': paymentstatus, 'amount': amount,'balance': balance}
    attendstats = Attendance.objects.filter(email=current_user)
    context = {'details': details, 'status': paymentstats, 'attendstats': attendstats}
    return render(request, 'candidate_profile.html', {'details': details, 'stats': paymentstats, 'attendstats': attendstats })


def candidate_update(request, candidate_id):
    data = Register.objects.get(pk=candidate_id)
    courses = Courses.objects.all()
    context = {'data': data, 'courses': courses}
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('num')
        alternative_number = request.POST.get('altnum')
        email = request.POST.get('email')
        college_name = request.POST.get('cname')
        address = request.POST.get('address')
        street = request.POST.get('street')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        course = request.POST.get('scourse')

        edit = Register.objects.get(pk=candidate_id)
        edit.first_name = fname
        edit.last_name = lname
        edit.Phone_number = phone
        edit.alternate_number = alternative_number
        edit.college_name = college_name
        edit.address = address
        edit.street = street
        edit.city = city
        edit.pincode = pin
        edit.course = course
        edit.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('candidate_profile')

    return render(request, 'candidate_update.html', context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to access this page')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            date = request.POST.get('date')
            email = request.POST.get('email')
            logintime = request.POST.get('logintime')
            logouttime = request.POST.get('logouttime')
            attend = Attendance(name=name, date=date, email=email,  logintime=logintime, logouttime=logouttime)
            attend.save()
            messages.success(request, 'You attendance application has been received')
            return redirect('candidate_profile')
    return render(request, 'attendance.html')


def search(request):
    query = request.GET['search']
    if len(query) > 50:
        post = Courses.objects.none()
    else:
        post = Courses.objects.filter(course_name__icontains=query)
    if post.count() == 0:
        messages.warning(request, 'No search Results')
    params = {'post': post, 'query': query}
    return render(request, 'search.html', params)
