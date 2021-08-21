from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from accounts.models import Profile
from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserChangePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import update_session_auth_hash

# Create your views here.


# def register_view(request, *args, **kwargs):
#     context = {}
#     form = UserRegisterForm()
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             form.save()
#             # return redirect('album-list')
#     context['form'] = form
#     return render(request, 'registration/register.html', context=context)


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    # def get_context_data(self, **kwargs):
    #     albums = self.get_object().albums.all()
    #     paginator = Paginator(albums, self.paginate_related_by, orphans=self.paginate_related_orphans)
    #     page_number = self.request.GET.get('page', 1)
    #     page = paginator.get_page(page_number)
    #     kwargs['page_obj'] = page
    #     kwargs['albums'] = page.object_list
    #     kwargs['is_paginated'] = page.has_other_pages()
    #     return super().get_context_data(**kwargs)


# class UserListView(PermissionRequiredMixin, ListView):
#     template_name = 'user_list.html'
#     model = Profile
#     context_object_name = 'profiles'
#     permission_required = 'accounts.view_profile'

