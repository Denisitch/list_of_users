from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from users.models import Users
from django.db.models import Q
from users.forms import UsersForm
from django.urls import reverse_lazy


class ListUsers(ListView):
    model = Users
    template_name = "users/index.html"
    context_object_name = "users"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListUsers, self).get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(patronymic__icontains=query)
                | Q(date_of_birth__icontains=query)
                | Q(phone_number__icontains=query)
                | Q(status__icontains=query)
            )
        return queryset


class ViewUser(DetailView):
    model = Users
    template_name = "users/view_user.html"
    context_object_name = "item_user"


class CreateUser(CreateView):
    form_class = UsersForm
    template_name = "users/add_user.html"


class UpdateUser(UpdateView):
    model = Users
    template_name = "users/edit_user.html"
    context_object_name = "item_user"
    fields = "__all__"


class DeleteUser(DeleteView):
    model = Users
    template_name = "users/delete_user.html"
    context_object_name = "item_user"
    success_url = reverse_lazy("list_of_users")
