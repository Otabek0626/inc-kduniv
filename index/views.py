from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Navigation, Content
from django.db.models import Prefetch
# Create your views here.
def main(request, html='index'):
    data = {}
    navs = Navigation.objects.prefetch_related(Prefetch('contents', queryset=Content.objects.all())).all().order_by('order')
    
    
    context = {
        "data": navs
    }
    try:
        context['content'] = Content.objects.filter(id=int(html)).first()

        return render(request, f"main.html", context)
    except:
        return render(request, f"index.html", context)


def form(request):
    if request.method == "POST":
        first_name = request.POST["firstName"]
        middle_name = request.POST["middleName"]
        last_name = request.POST["lastName"]
        gender = request.POST["gender"]
        image = request.FILES["photograph"]
        country = request.POST["country"]
        nationality = request.POST["nationality"]
        passport_number = request.POST["passport"]
        home_address = request.POST["homeAddress"]
        current_address = request.POST["currentAddress"]
        tel_number_home = request.POST["homeTelNumber"]
        tel_number_mobile = request.POST["MobileTelNumber"]
        email = request.POST["email"]
        name_of_institution = request.POST["name_institution"]
        address_of_institution = request.POST["address_inst"]
        degree = request.POST["degree"]
        department = request.POST["department"]
        major = request.POST["major"]
        tem_number_of_institution = request.POST["institureTel"]
        email_of_institution = request.POST["instituteEmail"]
        english = request.POST["proficiencyEnglish"]
        korean = request.POST["proficiencyKorean"]
        statement_of_interest = request.POST["Statement"]
        
        profile = Profile(first_name=first_name, middle_name=middle_name, last_name=last_name, gender=gender, image=image, country=country, nationality=nationality, passport_number=passport_number, home_address=home_address, current_address=current_address, tel_number_home=tel_number_home, tel_number_mobile=tel_number_mobile, email=email, name_of_institution=name_of_institution, address_of_institution=address_of_institution, degree=degree, department=department, major=major, tem_number_of_institution=tem_number_of_institution, email_of_institution=email_of_institution, english=english, korean=korean, statement_of_interest=statement_of_interest)
        profile.save()
        return redirect('main')
    return render(request, 'form.html')