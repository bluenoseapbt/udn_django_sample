from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView

from udnParticipants.models import Participant
from udnParticipants.participantForm import ParticipantForm


class FormActionMixin:
    template_name = 'participants_list.html'

    def get(self, request):
        participants = Participant.objects.all()
        args = {'form': ParticipantForm, 'participants': participants}
        print("participants: ", participants)
        return render(request, self.template_name, args)

    def post(self, request):
        """Add 'Cancel' button redirect."""
        if 'cancel' in request.POST:
            return HttpResponseRedirect("/login_user")
        else:
            print('initializing the participant form with data from the request...')
            bound_form = ParticipantForm(request.POST)
            print('done.')
            if bound_form.is_valid():
                print('saving data...')
                bound_form.save()
                print('saving done.')

            return HttpResponseRedirect("/show_all_data")


class ParticipantCreateView(FormActionMixin, CreateView):
    """Create view for the Participant Model """
    form_class = ParticipantForm
    template_name = 'form.html'


class ParticipantListView(ListView):
    """List view for the Participant Models."""
    model = Participant
    context_object_name = 'participants'
    template_name = 'participant_list.html'


def DoLoginUser(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed")
    else:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        login(request,user)

        if user!=None:
            return HttpResponseRedirect('/form')
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect('/login_user')


def IndexPageController(request):
    return HttpResponseRedirect("/login_user")


def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/login_user")


def LoginUser(request):
    if request.user == None or request.user == "" or request.user.username == "":
        return render(request, "registration/login.html")
    else:
        return HttpResponseRedirect("/form")


@login_required(login_url="/login_user/")
def showAllData(request):
    all_participants = Participant.objects.all()

    return render(request,"participant_list.html",{'participants':all_participants})


@login_required(login_url="/login_user/")
def updateParticipant(request,participant_id):
    participant = Participant.objects.get(id=participant_id)
    if participant == None:
        return HttpResponse("Participant Not Found")
    else:
        return render(request,"participant_edit.html",{'participant':participant})


@login_required(login_url="/login_user/")
def editParticipant(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        participant = Participant.objects.get(id=request.POST.get('id',''))
        if participant == None:
            return HttpResponse("<h2>Participant Not Found</h2>")
        else:
            participant.fullname=request.POST.get('name','')
            participant.age=request.POST.get('age','')
            participant.siblings=request.POST.get('sibling', False)
            participant.environmentExposures=request.POST.get('environment','')
            participant.geneticMutations=request.POST.get('mutation','')
            participant.revieItem=request.POST.get('status','')
            participant.save()

            messages.success(request,"Updated Successfully")
            return HttpResponseRedirect("/show_all_data")


@login_required(login_url="/login_user/")
def deleteParticipant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    participant.delete()
    messages.error(request, "Deleted Successfully")

    return HttpResponseRedirect("/show_all_data")


@csrf_exempt
def saveParticipant(request):
    id = request.POST.get('id', '')
    type = request.POST.get('type', '')
    value = request.POST.get('value', '')
    participant =  Participant.objects.get(id=id)
    if type == "name":
        participant.fullname = value

    if type == "age":
        participant.age = value

    if type == "siblings":
        participant.siblings = value

    if type == "review":
        participant.reviewItem = value

    if type == "mutation":
        participant.geneticMutations = value

    if type == "environment":
        participant.environmentExposures = value

    if type == "created_at":
        participant.created_at = value

    participant.save()

    return JsonResponse({"success": "Updated"})
