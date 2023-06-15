from django.urls import path
from FrontPage import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about-wiras/',views.about_wiras,name='about-wiras'),
    path('achivements/',views.achivements,name='achivements'),
    path('activities/',views.activities,name='activities'),
    path('administration/',views.administration,name='administration'),
    path('admission/',views.admission,name='admission'),
    path('alumni/',views.alumni,name='alumni'),
    path('alumni-reports/',views.alumni_reports,name='alumni-reports'),
    path('anti-ragging-cell/',views.anti_ragging_cell,name='anti-ragging-cell'),
    path('aqar/',views.aqar,name='aqar'),
    path('bicycle-club/',views.bicycle_club,name='bicycle-club'),
    path('collage-council/',views.collage_council,name='collage-council'),
    path('collage-rules/',views.collage_rules,name='collage-rules'),
    path('collage-union/',views.collage_union,name='collage-union'),
    path('complaints/',views.complaints,name='complaints'),
    path('contact/',views.contact,name='contact'),
    path('courses/<str:type>',views.courses,name='courses'),
    path('department/<str:dep_url>/',views.department_view,name='department-view'),
    path('digital-wing/',views.digital_wing,name='digital-wing'),
    path('downloads/',views.downloads,name='downloads'),
    path('dqac/',views.dqac,name='dqac'),
    path('ethic-committee/',views.ethic_committee,name='ethic-committee'),
    path('exam-results/',views.exam_results,name='exam-results'),
    path('exam-schedule/',views.exam_schedule,name='exam-schedule'),
    path('film-club/',views.film_club,name='film-club'),
    path('gallery/',views.gallery,name='gallery'),
    path('gallery/<str:page>/',views.gallery2,name='gallery2'),
    path('view-gallery/<str:album_url>/',views.view_gallery,name='view-gallery'),
    path('governing-body/',views.governing_body,name='governing-body'),
    path('green-club/',views.green_club,name='green-club'),
    path('grievance-cell/',views.grievance_cell,name='grievance-cell'),
    path('institutes/',views.institutes,name='institutes'),
    path('iqac-composition/',views.iqac_composition,name='iqac-composition'),
    path('iqac-goals/',views.iqac_goals,name='iqac-goals'),
    path('iqac-objectives/',views.iqac_objectives,name='iqac-objectives'),
    path('managers-message/',views.managers_message,name='managers-message'),
    path('minutes-atr/',views.minutes_atr,name='minutes-atr'),
    path('mission-vision/',views.mission_vision,name='mission-vision'),
    path('music-club/',views.music_club,name='music-club'),
    path('nature-club/',views.nature_club,name='nature-club'),
    path('news/',views.news,name='news'),
    path('news/<str:page>/',views.news2,name='news2'),
    path('news_details/<str:news_url>/',views.news_details,name='news-details'),
    path('nss/',views.nss,name='nss'),
    path('office-bearers/',views.office_bearers,name='office-bearers'),
    path('others/',views.others,name='others'),
    path('principal-message/',views.principal_message,name='principal-message'),
    path('pta/',views.pta,name='pta'),
    path('registration/',views.registration,name='registration'),
    path('reports/',views.reports,name='reports'),
    path('roll-of-honour/',views.roll_of_honour,name='roll-of-honour'),
    path('rural-club/',views.rural_club,name='rural-club'),
    path('seminar-workshops/',views.seminar_workshops,name='seminar-workshops'),
    path('sexual-harassment/',views.sexual_harrasment,name='sexual-harassment'),
    path('speakers-forum/',views.speakers_forum,name='speakers-forum'),
    path('ssr/',views.ssr,name='ssr'),
    path('tourism-club/',views.tourism_club,name='tourism-club'),
    path('update-soon/',views.update_soon,name='update-soon'),
    path('women-cell/',views.women_cell,name='womens-cell'),
    path('yoga-club/',views.yoga_club,name='yoga-club'),
    path('news_letter/',views.news_letter,name='news_letter'),
    path('contact-ajax/',views.contact_ajax,name='contact-ajax'),
    path('library-facility/',views.library_facelity,name='library-facility'),
    path('hostel-facility/',views.hostel_facilities,name='hostel-facility'),
    path('bus-facility/',views.bus_facilities,name='bus-facility'),
    path('canteen-facility/',views.canteen_facilities,name='canteen-facility'),
    path('sports-facility/',views.sports_facilities,name='sports-facility'),
    path('store-facility/',views.store_facilities,name='store-facility'),
    path('seminarhall-facility/',views.seminarhall_facilities,name='seminar-facility'),
    path('auditorium-facility/',views.auditorium_facilities,name='auditorium-facility')
]