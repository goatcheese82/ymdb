from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import User, Ward, Stake, Event


# def index(req):
#    event_list = Event.objects.all()
#    context = {
#       "events": event_list
#    }
#    return render(req, "index.html", context)


class IndexView(generic.ListView):
    template_name = "index.html"

    events = Event.objects.all()

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by("date")

#Ward routes

class WardDetailView(generic.DetailView):
   model = Ward
   template_name = "wards/index.html"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["members"] = User.objects.filter(ward=self.object.id)
      return context


# def ward_detail(req, ward_id):
#    ward = get_object_or_404(Ward, pk=ward_id)
#    members_list = User.objects.filter(ward=ward_id)
#    context = {
#    "members_list": members_list,
#    "ward": ward,
#    }
#    return render(req, "wards/index.html", context)


#Stake Routes


class StakeDetailView(generic.DetailView):
   model = Stake
   template_name = "stakes/index.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["wards"] = Ward.objects.filter(stake=self.object.id)
      return context

# def stake_detail(req, stake_id):
#    stake = get_object_or_404(Stake, pk=stake_id)
#    wards_list = Ward.objects.filter(stake=stake_id)
#    context = {
#       "wards": wards_list,
#       "stake": stake,
#    }
#    return render(req, "stakes/index.html", context)


#Event Routes
   
class UserDetailView(generic.DetailView):
   template_name = "users/index.html"
   model = User


class EventDetailView(generic.DetailView):
   model = Event
   template_name = "events/index.html"

# def event_detail(req, event_id):
#    event = get_object_or_404(Event, pk=event_id)
#    context = {
#       "event": event,
#    }
#    return render(req, "events/detail.html")

def add_event(req, stake_id):
   stake = get_object_or_404(Stake, pk=stake_id)
   return HttpResponseRedirect(reverse("directories:index", args=(stake_id)))