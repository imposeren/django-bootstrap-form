from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()

@register.filter
def bootstrap(element):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        template = get_template("bootstrapform_too/field.html")
        context = Context({'field': element})
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            template = get_template("bootstrapform_too/formset.html")
            context = Context({'formset': element})
        else:
            template = get_template("bootstrapform_too/form.html")
            context = Context({'form': element})

    return template.render(context)


@register.filter
def bootstrap_errorless(element):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        template = get_template("bootstrapform_too/field_errorless.html")
        context = Context({'field': element})
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            template = get_template("bootstrapform_too/formset_errorless.html")
            context = Context({'formset': element})
        else:
            template = get_template("bootstrapform_too/form_errorless.html")
            context = Context({'form': element})

    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"
