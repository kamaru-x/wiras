from django.shortcuts import render
from Core.models import Course,Department,Post,Album,Album_Image,Faculty,Enquiry

# Create your views here.

#---------------------------------------------- INDEX -----------------------------------------------#

def index(request):
    return render(request,'frontpage/index.html')

#------------------------------------------ ABOUT WIRAS ---------------------------------------------#

def about_wiras(request):
    return render(request,'frontpage/about-wiras.html')

#------------------------------------------- ACHIVEMENTS --------------------------------------------#

def activities(request):
    return render(request,'frontpage/activities.html')

#------------------------------------------- ACTIVITIES --------------------------------------------#

def achivements(request):
    return render(request,'frontpage/achievements.html')

#---------------------------------------- ADMINISTRATION --------------------------------------------#

def administration(request):
    return render(request,'frontpage/administration.html')

#-------------------------------------------- ADMISSION ---------------------------------------------#

def admission(request):
    return render(request,'frontpage/admission.html')

#-------------------------------------------- ALUMNI ------------------------------------------------#

def alumni(request):
    return render(request,'frontpage/alumni.html')

#----------------------------------------- ALUMNI REPORTS -------------------------------------------#

def alumni_reports(request):
    return render(request,'frontpage/alumni-reports.html')

#--------------------------------------- ANTI RAGGING CELL ------------------------------------------#

def anti_ragging_cell(request):
    return render(request,'frontpage/anti-ragging-cell.html')

#-------------------------------------------- AQAR -------------------------------------------------#

def aqar(request):
    return render(request,'frontpage/aqar.html')

#------------------------------------------- BICYCLE CLUB ------------------------------------------#

def bicycle_club(request):
    return render(request,'frontpage/bicycle-club.html')

#---------------------------------------- COLLAGE COUNCIL -------------------------------------------#

def collage_council(request):
    return render(request,'frontpage/college-council.html')

#----------------------------------------- COLLAGE RULES ------------------------------------------#

def collage_rules(request):
    return render(request,'frontpage/college-rules.html')

#----------------------------------------- COLLAGE UNION ------------------------------------------#

def collage_union(request):
    return render(request,'frontpage/college-union.html')

#-------------------------------------------- COMPLAINTS ------------------------------------------#

def complaints(request):
    return render(request,'frontpage/complaint.html')

#--------------------------------------------- CONTACT -------------------------------------------#

def contact(request):
    return render(request,'frontpage/contact.html')

#--------------------------------------------- COURSE -----------------------------------------------#

def courses(request,type):
    if type == 'UG':
        courses = Course.objects.filter(Course_Type='UG Course')
    elif type == 'PG':
        courses = Course.objects.filter(Course_Type='PG Course')
    return render(request,'frontpage/courses.html',{'courses':courses})

#----------------------------------------- COURSE DETAILS -----------------------------------------#

def course_details(request,crs):
    course = Course.objects.filter(Course_Title=crs).last()
    return render(request,'frontpage/course-details.html',{'course':course})

#----------------------------------------- DIGITAL WING -----------------------------------------#

def digital_wing(request):
    return render(request,'frontpage/digital-wing.html')

#----------------------------------------- DOWNLOADS --------------------------------------------#

def downloads(request):
    return render(request,'frontpage/downloads.html')

#-------------------------------------------- DQAC ---------------------------------------------#

def dqac(request):
    return render(request,'frontpage/dqac.html')

#--------------------------------------- ETHIC COMMITTEE ---------------------------------------#

def ethic_committee(request):
    return render(request,'frontpage/ethic-committee.html')

#----------------------------------------- EXAM RESULTS ---------------------------------------#

def exam_results(request):
    return render(request,'frontpage/exam-result.html')

#----------------------------------------- EXAM SCHEDULE ---------------------------------------#

def exam_schedule(request):
    return render(request,'frontpage/exam-schedule.html')

#------------------------------------------ FILM CLUB -----------------------------------------#

def film_club(request):
    return render(request,'frontpage/film-club.html')

#------------------------------------------ GALLERY ----------------------------------------------#

def gallery(request):
    albums = Album.objects.all()
    return render(request,'frontpage/gallery.html',{'album':albums})

#---------------------------------------- VIEW GALLERY -------------------------------------------#

def view_gallery(request,album):
    images = Album_Image.objects.filter(Album=album)
    return render(request,'frontpage/view-gallery.html',{'images':images})

#--------------------------------------- GOVERNING BODY ------------------------------------------#

def governing_body(request):
    return render(request,'frontpage/governing-body.html')

#----------------------------------------- GREEN CLUB -------------------------------------------#

def green_club(request):
    return render(request,'frontpage/green-club.html')

#-------------------------------------- GRIEVANCE CELL -------------------------------------------#

def grievance_cell(request):
    return render(request,'frontpage/grievance-cell.html')

#----------------------------------------- INSTITUTES --------------------------------------------#

def institutes(request):
    return render(request,'frontpage/institutes.html')

#-------------------------------------- IQAC COMPOSITION ------------------------------------------#

def iqac_composition(request):
    return render(request,'frontpage/iqac-composition.html')

#-------------------------------------- IQAC COMPOSITION ------------------------------------------#

def iqac_goals(request):
    return render(request,'frontpage/iqac-goals.html')

#-------------------------------------- IQAC OBJECTIVES ------------------------------------------#

def iqac_objectives(request):
    return render(request,'frontpage/iqac-objectives.html')

#-------------------------------------- MANAGER MESSAGES ------------------------------------------#

def managers_message(request):
    return render(request,'frontpage/managers-message.html')

#----------------------------------------- MINUTS ATR ---------------------------------------------#

def minutes_atr(request):
    return render(request,'frontpage/minutes-atr.html')

#--------------------------------------- MISSION AND VISSION ----------------------------------------#

def mission_vision(request):
    return render(request,'frontpage/mission-and-vision.html')

#----------------------------------------- MUSIC CLUB ----------------------------------------------#

def music_club(request):
    return render(request,'frontpage/music-club.html')

#----------------------------------------- NATURE CLUB ----------------------------------------------#

def nature_club(request):
    return render(request,'frontpage/nature-club.html')

#--------------------------------------------- NEWS -------------------------------------------------#

def news(request):
    return render(request,'frontpage/news.html')

#---------------------------------------- NEWS DETAILS ---------------------------------------------#

def news_details(request,news):
    return render(request,'frontpage/news-details.html')

#--------------------------------------------- NSS -------------------------------------------------#

def nss(request):
    return render(request,'frontpage/nss.html')

#---------------------------------------- OFFICE BEARERS -------------------------------------------#

def office_bearers(request):
    return render(request,'frontpage/office-bearers.html')

#------------------------------------------- OTHERS ------------------------------------------------#

def others(request):
    return render(request,'frontpage/others.html')

#------------------------------------------- PRINCIPAL MESSAGE -------------------------------------#

def principal_message(request):
    return render(request,'frontpage/principal-message.html')

#--------------------------------------------- PTA -------------------------------------------------#

def pta(request):
    return render(request,'frontpage/pta.html')

#------------------------------------------ REGISTRATION -------------------------------------------#

def registration(request):
    return render(request,'frontpage/registration.html')

#-------------------------------------------- REPORTS ---------------------------------------------#

def reports(request):
    return render(request,'frontpage/reports.html')

#-------------------------------------- ROLL OF HONOUR ---------------------------------------------#

def roll_of_honour(request):
    return render(request,'frontpage/roll-of-honour.html')

#------------------------------------------ RURAL CLUB ---------------------------------------------#

def rural_club(request):
    return render(request,'frontpage/rural-club.html')

#--------------------------------------- SEMINAR WORKSHOPS -----------------------------------------#

def seminar_workshops(request):
    return render(request,'frontpage/seminars-workshops.html')

#--------------------------------------- SEXUAL HARRASMENT -----------------------------------------#

def sexual_harrasment(request):
    return render(request,'frontpage/sexual-harassment.html')

#---------------------------------------- SPEAKERS FORUM ------------------------------------------#

def speakers_forum(request):
    return render(request,'frontpage/speakers-forum.html')

#--------------------------------------------- SSR -------------------------------------------------#

def ssr(request):
    return render(request,'frontpage/ssr.html')

#------------------------------------------ TOURISM CLUB ------------------------------------------#

def tourism_club(request):
    return render(request,'frontpage/tourism-club.html')

#------------------------------------------ UPDATE SOON ------------------------------------------#

def update_soon(request):
    return render(request,'frontpage/updated-soon.html')

#------------------------------------------ WOMEN CELL ------------------------------------------#

def women_cell(request):
    return render(request,'frontpage/women_cell.html')

#------------------------------------------ YOGA CLUB ------------------------------------------#

def yoga_club(request):
    return render(request,'frontpage/yoga-club.html')