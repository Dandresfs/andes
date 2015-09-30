from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from financiero import views

urlpatterns = [
    url(r'^$', login_required(views.FinancieroView.as_view())),

    url(r'^gestores/$', login_required(views.GestorView.as_view())),
    url(r'^gestores/nuevo/$', login_required(views.NuevoGestorView.as_view())),

    url(r'^formadores/$', login_required(views.FormadorView.as_view())),
    url(r'^formadores/nuevo/$', login_required(views.NuevoFormadorView.as_view())),

    url(r'^funcionarios/$', login_required(views.FuncionarioView.as_view())),
    url(r'^funcionarios/nuevo/$', login_required(views.NuevoFuncionarioView.as_view())),
]