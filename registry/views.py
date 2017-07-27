from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.apps import apps
from django.urls import reverse

from . import models

def field_as_cell():
    pass

class ProjectDetailView(generic.DetailView):
    model = models.Project

def object_list_view(request, model_name):
    model = apps.get_model('registry', model_name)
    request.model_name = model_name
    request.verbose_name_plural = model._meta.verbose_name_plural
    return generic.ListView.as_view(model=model, template_name='registry/object_list.html')(request)

def object_detail_view(request, model_name, pk):
    try:
        model = apps.get_model('registry', model_name)
    except:
        raise Http404("{model_name}: no such model.".format(model_name=model_name))
    
    as_view_arguments = dict(
        model=model, 
        template_name='registry/object_detail.html',
        # fields=model.display_order,
        # success_url=reverse('registry:object_list', kwargs={'model_name': model_name}),
    )   
    return generic.DetailView.as_view(**as_view_arguments)(request, pk=pk)

def object_view(request, model_name, pk):
    try:
        model = apps.get_model('registry', model_name)
    except:
        raise Http404("{model_name}: no such model.".format(model_name=model_name))
    
    as_view_arguments = dict(
        model=model, 
        template_name='registry/object_form.html',
        fields=[field.name for field in model._meta.fields[1:] if field.editable],
        success_url=reverse('registry:object_list', kwargs={'model_name': model_name}),   
    )
    view_function_arguments = dict()
    if pk == "new":
        generic_view_object = generic.CreateView
    else:
        generic_view_object = generic.UpdateView
        view_function_arguments['pk'] = pk
        
    return generic_view_object.as_view(**as_view_arguments)(request, **view_function_arguments)
        # except:
            # raise Http404("Can't find {model_name} {pk}.".format(model_name=model_name, pk=pk))
