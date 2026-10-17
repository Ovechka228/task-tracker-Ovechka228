from django.http import HttpRequest, HttpResponse


class UserIsOwnerMixin:
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != self.request.user:
            return HttpResponse(status=403, content='Permission denied!')
        return super().dispatch(request, *args, **kwargs)
