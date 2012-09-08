from djangorestframework.mixins import ModelMixin
from djangorestframework.permissions import IsAuthenticated
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

from waveformeditor.resources import CircuitResource

class RestrictToUserMixin(ModelMixin):
    """
    Mixin powodujacy, ze uzytkownicy maja dostep tylko do swoich danych
    """
    def get_queryset(self):
        """
        zwraca obiekty nalezace do zalogowanego uzytkownika
        """
        return self.resource.model.objects.filter(created_by=self.user)

    def get_instance_data(self, model, content, **kwargs):
        """
        ustawia pole created_by na zalogowanego uzytkownika
        """
        content['created_by'] = self.user
        return super(RestrictToUserMixin, self).get_instance_data(model, content, **kwargs)

class CircuitListView(RestrictToUserMixin, ListOrCreateModelView):
    """
    widok listy dla schematow
    """
    resource = CircuitResource
    permissions = (IsAuthenticated, )

class CircuitInstanceView(RestrictToUserMixin, InstanceModelView):
    """
    widok dla konkretnego schematu
    """
    resource = CircuitResource
    permissions = (IsAuthenticated, )
