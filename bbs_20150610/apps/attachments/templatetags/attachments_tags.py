# # -*- coding: utf-8 -*-
import os
import re
from django.conf import settings
from django.template import Library, Node, Variable
from apps.attachments.forms import AttachmentForm
from apps.attachments.views import add_url_for_obj
from django.core.urlresolvers import reverse
from apps.attachments.models import Attachment

register = Library()

@register.inclusion_tag('attachments/add_form.html', takes_context=True)
def attachment_form(context, obj):
    """
    Renders a "upload attachment" form.

    The user must own ``attachments.add_attachment permission`` to add
    attachments.
    """
    if context['user'].has_perm('attachments.add_attachment'):
        return {
            'form': AttachmentForm(),
            'form_url': add_url_for_obj(obj),
            'next': context['request'].build_absolute_uri(),
        }
    else:
        return {
            'form': None,
        }

@register.inclusion_tag('attachments/delete_link.html', takes_context=True)
def attachment_delete_link(context, attachment):
    """
    Renders a html link to the delete view of the given attachment. Returns
    no content if the request-user has no permission to delete attachments.

    The user must own either the ``attachments.delete_attachment`` permission
    and is the creator of the attachment, that he can delete it or he has
    ``attachments.delete_foreign_attachments`` which allows him to delete all
    attachments.
    """
    if context['user'].has_perm('delete_foreign_attachments') \
       or (context['user'] == attachment.creator and \
           context['user'].has_perm('attachments.delete_attachment')):
        return {
            'next': context['request'].build_absolute_uri(),
            'delete_url': reverse('delete_attachment', kwargs={'attachment_pk': attachment.pk})
        }
    return {'delete_url': None,}



class AttachmentsForObjectNode(Node):
    def __init__(self, obj, var_name):
        self.obj = obj
        self.var_name = var_name

    def resolve(self, var, context):
        """Resolves a variable out of context if it's not in quotes"""
        if var[0] in ('"', "'") and var[-1] == var[0]:
            return var[1:-1]
        else:
            return Variable(var).resolve(context)

    def render(self, context):
        obj = self.resolve(self.obj, context)
        var_name = self.resolve(self.var_name, context)
        context[var_name] = Attachment.objects.attachments_for_object(obj)
        return ''

@register.tag
def get_attachments_for(parser, token):
    """
    Resolves attachments that are attached to a given object. You can specify
    the variable name in the context the attachments are stored using the `as`
    argument. Default context variable name is `attachments`.

    Syntax::

        {% get_attachments_for obj %}
        {% for att in attachments %}
            {{ att }}
        {% endfor %}

        {% get_attachments_for obj as "my_attachments" %}

    """
    def next_bit_for(bits, key, if_none=None):
        try:
            return bits[bits.index(key)+1]
        except ValueError:
            return if_none

    bits = token.contents.split()
    args = {
        'obj': next_bit_for(bits, 'get_attachments_for'),
        'var_name': next_bit_for(bits, 'as', '"attachments"'),
    }
    return AttachmentsForObjectNode(**args)


class AttachmentsForFilterObjectNode(Node):
    def __init__(self, obj, body):
        self.obj = obj
        self.body = body

    def resolve(self, var, context):
        """Resolves a variable out of context if it's not in quotes"""
        if var[0] in ('"', "'") and var[-1] == var[0]:
            return var[1:-1]
        else:
            return Variable(var).resolve(context)

    def render(self, context):
        obj = self.resolve(self.obj, context)
        body = self.resolve(self.body, context)
        attrs = Attachment.objects.attachments_for_object(obj)
        # print attrs, body
        att_sre = re.compile('\[attachment\](\d+)\[\/attachment\]').findall(body)
        attrs = attrs.exclude(id__in=att_sre)
        context['attachments'] = attrs
        return ''


@register.tag
def get_attachments_for_filte(parser, token):
    bits = token.contents.split()
    obj, body = bits[1:]
    return AttachmentsForFilterObjectNode(obj, body)


@register.filter
def attachment_sequence(content):
    # [attachment]30[/attachment]

    def sub_att(m):
        try:
            attr = Attachment.objects.get(id=m.group(1))
            filename = os.path.basename(attr.attachment_file.name)
            if re.search(r'.*\.(png|jpg|jpeg|gif)$', filename):
                # 图片
                return "<img src='{scr}' class='img-body-auto'>".format(scr=str(settings.MEDIA_URL+attr.attachment_file.name))
            else:
                return "<a href='{href}'><i class='fa fa-paperclip'></i>{filename}</a>".format(href=str(settings.MEDIA_URL+attr.attachment_file.name), filename=filename)
        except Exception as e:
            return ''
        return ''
    return re.compile('\[attachment\](\d+)\[\/attachment\]').sub(sub_att, content)


@register.filter
def attachment_a_preview(attr):
    filename = os.path.basename(attr.attachment_file.name)
    if re.search(r'.*\.(png|jpg|jpeg|gif)$', filename):
        # 图片
        return "<img src='{scr}'>".format(scr=str(settings.MEDIA_URL+attr.attachment_file.name))
    else:
        return "<a href='{href}'><i class='fa fa-paperclip'></i>{filename}</a>".format(href=str(settings.MEDIA_URL+attr.attachment_file.name), filename=filename)

@register.filter
def attachment_preview(attr):
    filename = os.path.basename(attr.attachment_file.name)
    if re.search(r'.*\.(png|jpg|jpeg|gif)$', filename):
        # 图片
        return "<img src='{scr}'>".format(scr=str(settings.MEDIA_URL+attr.attachment_file.name))
    else:
        return '<i class="fa fa-file-o"></i>'
    return filename
