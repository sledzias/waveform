from django.template import Context, loader, RequestContext
from waveformeditor.models import Circuit
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.shortcuts import render_to_response, get_object_or_404
import simplejson as json
from django.contrib.auth.decorators import login_required
@login_required
def show(request, circuit_id):
    c = get_object_or_404(Circuit, pk=circuit_id)
    return render_to_response('waveformeditor/show.html', {'circuit': c},context_instance=RequestContext(request))


@login_required
def circuits_list(request):
    context = RequestContext(request)
    u = request.user
    return render_to_response('waveformeditor/circuit_list.html', {'user' : u}, context)

def root_view(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login/')
    else:
        return redirect('/circuits/')


