
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from forms import AuthorForm, BookForm, PublisherForm
from models import Author, Book, Publisher

@require_http_methods(['GET', 'POST'])
def list_and_add_view(request, template_name, model, formclass):
    if request.method == 'GET':
        form = formclass()
    else:
        form = formclass(request.POST)
    
    if not form.is_valid() or request.method == 'GET':
        return render_to_response(template_name,
                                  {'form': form,
                                   'object_list': Author.objects.all()},
                                  context_instance=RequestContext(request))
    else:
        newitem = form.save()
        messages.success(request, "Item %s was added" % newitem)
        return HttpResponseRedirect(request.build_absolute_uri())

