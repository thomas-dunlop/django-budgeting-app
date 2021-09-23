from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from .models import Envelope, Transaction

# Create your views here.
def homePage(request):
    envelope_list = Envelope.objects.order_by('env_name')
    context = {'envelope_list': envelope_list}
    return render(request, 'envelopeBudgeting/homePage.html', context)

def envelopes(request, env_id):
    envelope = get_object_or_404(Envelope, pk = env_id)
    return render(request, 'envelopeBudgeting/envelopes.html', {'envelope': envelope})

def addEnvelope(request):
    name = request.POST['env_name']
    budget = request.POST['env_budget']
    funds = request.POST['env_funds']
    env = Envelope(env_name = name, env_budget = budget, env_funds = funds)
    env.save()
    return HttpResponseRedirect(reverse('envelopeBudgeting:homePage'))

def updateEnvelope(request, env_id):
    envelope = get_object_or_404(Envelope, pk = env_id)
    envelope.env_budget = request.POST['env_budget']
    envelope.env_funds = request.POST['env_funds']
    envelope.save()
    return HttpResponseRedirect(reverse('envelopeBudgeting:envelopes', args=(env_id,)))

def deleteEnvelope(request): 
    id = request.POST['deleteButton']
    envelope = Envelope.objects.get(pk=id)
    envelope.delete()
    return HttpResponseRedirect(reverse('envelopeBudgeting:homePage'))

def addTransaction(request, env_id):
    t_date = request.POST['t_date']
    amount = request.POST['amount']
    recipient = request.POST['recipient']
    transaction = Transaction(env_id = env_id, t_date = t_date, amount = amount, recipient = recipient)
    transaction.save()
    updateEnvelopeWithTransaction(env_id, amount)
    return HttpResponseRedirect(reverse('envelopeBudgeting:envelopes', args=(env_id,)))

def updateTransaction(request):
    return HttpResponse("This will return the logic for updating a transaction")

def deleteTransaction(request, env_id): 
    id = request.POST['deleteButton']
    transaction = Transaction.objects.get(pk=id)
    amount = float(transaction.amount) * -1
    transaction.delete()
    updateEnvelopeWithTransaction(env_id, amount)
    return HttpResponseRedirect(reverse('envelopeBudgeting:envelopes', args=(env_id,)))

#helper functions 
def updateEnvelopeWithTransaction(env_id, amount):
    envelope = Envelope.objects.get(pk=env_id)
    envelope.env_funds = float(envelope.env_funds) - float(amount)
    envelope.save()