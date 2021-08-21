from webapp.models import Announcement
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import AnnouncementForm
from django.contrib.auth.mixins import PermissionRequiredMixin



class AnnouncementList(ListView):
    template_name = 'index.html'
    model = Announcement
    context_object_name = 'announcements'
    ordering = ('title',)
    paginate_by = 5


class AnnouncementView(DetailView):
    template_name = 'view.html'
    model = Announcement
    context_object_name = 'announcements'


class AnnouncementCreate(CreateView):
    template_name = 'create.html'
    model = Announcement
    form_class = AnnouncementForm

    def get_success_url(self):
        return reverse('announcement-list')


class AnnouncementUpdate(UpdateView):
    model = Announcement
    template_name = 'update.html'
    form_class = AnnouncementForm
    context_object_name = 'announcements'

    def get_success_url(self):
        return reverse('announcement-view', kwargs={'pk': self.object.pk})


class AnnouncementDelete(DeleteView):
    template_name = 'delete.html'
    model = Announcement
    context_object_name = 'announcements'

    def get_success_url(self):
        return reverse('announcement-list')

    # def has_permission(self):
    #     return self.get_object().author == self.request.user or super().has_permission()


