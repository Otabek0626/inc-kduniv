from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Navigation, Content
from django.db.models import Prefetch
# Create your views here.
def main(request, html='index'):
    data = {}
    navs = Navigation.objects.prefetch_related(Prefetch('contents', queryset=Content.objects.all().order_by('order'))).all().order_by('order')
    
    
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
        dateofbirth = request.POST["dateofbirth"]
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
        docs = request.FILES["docs"]
        
        profile = Profile(first_name=first_name, dateofbirth=dateofbirth, last_name=last_name, gender=gender, image=image, country=country, nationality=nationality, passport_number=passport_number, home_address=home_address, current_address=current_address, tel_number_home=tel_number_home, tel_number_mobile=tel_number_mobile, email=email, name_of_institution=name_of_institution, address_of_institution=address_of_institution, degree=degree, department=department, major=major, tem_number_of_institution=tem_number_of_institution, email_of_institution=email_of_institution, english=english, korean=korean, statement_of_interest=statement_of_interest, docs=docs)
        profile.save()
        return render(request, 'success.html')
    
    context = {
        "countries": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]



    }

    return render(request, 'form.html', context)