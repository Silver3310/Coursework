from django.contrib.auth.views import redirect_to_login


class RequireLoginMixin:

    def dispatch(self, request, *args, **kwargs):
        """
        Checks if a user is authenticated before the a view performs
        """
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        return super(RequireLoginMixin, self).dispatch(request, *args, **kwargs)
