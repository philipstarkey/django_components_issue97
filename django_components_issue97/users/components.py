from django_components import component

@component.register("container")
class Container(component.Component):
    template_name = "container.html"
