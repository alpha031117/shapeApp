from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm
from login_required import LoginNotRequiredMixin
from django.urls import reverse_lazy


class CustomLoginView(LoginNotRequiredMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accountAuth/login.html"

    def get_success_url(self):
        # Determine the user's group
        if self.request.user.groups.filter(name='Admin').exists():
            return reverse_lazy('adminPortal:admin_home')  # Redirect to adminPortal if user is in admin group
        else:
            return reverse_lazy('userPortal:user_home')  # Redirect to user home page if user is not in admin group


class CustomLogoutView(LogoutView):
    pass
