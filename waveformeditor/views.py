from django.template import RequestContext
from waveformeditor.models import Circuit
from django.shortcuts import render_to_response, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def show(request, circuit_id):
    """
     widok dla konkretnego schemtu ukladu logicznego
    """
    c = get_object_or_404(Circuit, pk=circuit_id)
    return render_to_response('waveformeditor/show.html', {'circuit': c},context_instance=RequestContext(request))


@login_required
def circuits_list(request):
    """
     widok dla listy schematow ukladow logicznych
    """
    context = RequestContext(request)
    u = request.user
    return render_to_response('waveformeditor/circuit_list.html', {'user' : u}, context)

def root_view(request):
    """
     widok dla root adresu, przekierowuje na strone logowania dla niezarejestrowanego
     uzytkownika lub strone z lista schematow dla zalogowanego.
    """
    if not request.user.is_authenticated():
        return redirect('/accounts/login/')
    else:
        return redirect('/circuits/')


