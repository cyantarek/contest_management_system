from django.urls import path
from . import views

urlpatterns = [
	path("", views.index_view),
	path("registration/", views.registration_view),
	path("recovery/", views.recovery_view),
	path("login/", views.login_view),
	path("logout/", views.logout_view),
	path("contests/", views.contest_list),
	path("question/<id>/", views.question_list),
	path("contests/<id>/", views.contest_detail),
	path("account/", views.account_detail),
	path("ranking/", views.ranking_list),
	path("submit_solution/", views.submit_solution),
]