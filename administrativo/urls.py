from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from administrativo import views


urlpatterns = [
    url(r'^$', login_required(views.AdministrativoView.as_view()),name='administrativo'),

    url(r'^gestores/$', login_required(views.GestorView.as_view()),name='gestores'),
    url(r'^gestores/actualizar/soportes/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarSoporteView.as_view())),
    url(r'^gestores/actualizar/seguro/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarSeguroView.as_view())),
    url(r'^gestores/actualizar/informacion/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarInformacionView.as_view())),
    url(r'^gestores/actualizar/foto/(?P<gestor_id>\w+)/$', login_required(views.GestorActualizarFotoView.as_view())),

    url(r'^formadores/$', login_required(views.FormadorView.as_view()),name='formadores'),
    url(r'^formadores/(?P<tipo_id>\w+)/$', login_required(views.FormadorTipoView.as_view())),
    url(r'^formadores/(?P<tipo_id>\w+)/actualizar/soportes/(?P<formador_id>\w+)/$', login_required(views.FormadorActualizarSoporteView.as_view())),
    url(r'^formadores/(?P<tipo_id>\w+)/actualizar/seguro/(?P<formador_id>\w+)/$', login_required(views.FormadorActualizarSeguroView.as_view())),
    url(r'^formadores/(?P<tipo_id>\w+)/actualizar/informacion/(?P<formador_id>\w+)/$', login_required(views.FormadorActualizarInformacionView.as_view())),
    url(r'^formadores/(?P<tipo_id>\w+)/actualizar/foto/(?P<formador_id>\w+)/$', login_required(views.FormadorActualizarFotoView.as_view())),

    url(r'^funcionarios/$', login_required(views.FuncionarioView.as_view()),name='formadores'),
    url(r'^funcionarios/actualizar/soportes/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarSoporteView.as_view())),
    url(r'^funcionarios/actualizar/seguro/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarSeguroView.as_view())),
    url(r'^funcionarios/actualizar/informacion/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarInformacionView.as_view())),
    url(r'^funcionarios/actualizar/foto/(?P<funcionario_id>\w+)/$', login_required(views.FuncionarioActualizarFotoView.as_view())),

    url(r'^cpe/$', login_required(views.CpeView.as_view())),
    url(r'^cpe/informes/$', login_required(views.CpeInformeView.as_view())),
    url(r'^cpe/informes/listado/$', login_required(views.CpeInformeTableView.as_view())),
    url(r'^cpe/informes/nuevo/$', login_required(views.CpeInformeNuevoView.as_view())),
    url(r'^cpe/informes/actualizar/(?P<informe_id>\w+)/$', login_required(views.CpeInformeUpdateView.as_view())),

    url(r'^cpe/obligaciones/$', login_required(views.CpeObligacionesView.as_view())),
    url(r'^cpe/obligaciones/nuevo/$', login_required(views.CpeNuevaObligacionView.as_view())),
    url(r'^cpe/obligaciones/listado/$', login_required(views.CpeObligacionTableView.as_view())),

    url(r'^cpe/obligaciones/editar/(?P<obligacion_id>\w+)/$', login_required(views.CpeEditarObligacion.as_view())),
    url(r'^cpe/obligaciones/agregar/(?P<obligacion_id>\w+)/$', login_required(views.CpeNuevoSoporteObligacion.as_view())),
    url(r'^cpe/obligaciones/editar/(?P<obligacion_id>\w+)/(?P<soporte_id>\w+)/$', login_required(views.CpeEditarSoporteObligacion.as_view())),
    url(r'^cpe/obligaciones/eliminar/(?P<obligacion_id>\w+)/(?P<soporte_id>\w+)/$', login_required(views.CpeEliminarSoporteObligacion.as_view())),
]