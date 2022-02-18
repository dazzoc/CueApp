from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Device
from .forms import ListeningForm



# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def albums_index(request):
    albums = Album.objects.filter(user=request.user)
    return render(request, 'albums/index.html', { 'albums': albums })


@login_required
def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    if album.user_id != request.user.id:
        return redirect('index')
    listening_form = ListeningForm()
    devices_album_doesnt_have = Device.objects.exclude(id__in = album.devices.all().values_list('id'))
    return render(request, 'albums/detail.html', {
        'album': album, 'listening_form': listening_form,
        'devices': devices_album_doesnt_have
    })


@login_required
def add_listening(request, album_id):
    form = ListeningForm(request.POST)
    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.album_id = album_id
        new_listening.save()
    return redirect('detail', album_id=album_id)



@login_required
def assoc_device(request, album_id, device_id):
    Album.objects.get(id=album_id).devices.add(device_id)
    return redirect('detail', album_id=album_id)


#==========================Album Class Views====================


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ('name', 'img', 'artist', 'genre', 'description')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ('name', 'img', 'artist', 'genre', 'description')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('index')
        return super(AlbumUpdate, self).dispatch(request, *args, **kwargs)

class AlbumDelete(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = '/albums/'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('index')
        return super(AlbumDelete, self).dispatch(request, *args, **kwargs)


#========================Devices===============================


@login_required
def devices_index(request):
    devices = Device.objects.all()
    return render(request, 'devices/index.html', { 'devices': devices })

@login_required
def devices_detail(request, device_id):
    device = Device.objects.get(id=device_id)
    return render(request, 'devices/detail.html', { 'device': device })

class DeviceCreate(LoginRequiredMixin, CreateView):
    model = Device
    fields = '__all__'
    # easy way not refered 
    success_url = '/devices/'

class DeviceUpdate(LoginRequiredMixin, UpdateView):
    model = Device
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ('name', 'img')
    success_url = '/devices/'

class DeviceDelete(LoginRequiredMixin, DeleteView):
    model = Device
    success_url = '/devices/'