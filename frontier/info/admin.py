from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import format_html
from redactor.fields import RedactorField
from modeltranslation.admin import TabbedTranslationAdmin
from .translation import InfoTranslationOptions, MenuLinksTranslationOptions
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Info, Contact, ParthnerLogo, MenuLinks

def get_admin_thumbnail(self):
    return get_cloudinary_thumb(self.image, width=100, crop="fill", q=7)

def admin_thumbnail_img(obj):
    return format_html('<img src=%s >' % obj.get_admin_thumbnail())

# Register your models here.
class InfoAdmin(TabbedTranslationAdmin):

    def has_add_permission(self, request, obj=None):
        info = Info.objects.all()
        if len(info) == 1:
            return False
        else:
            return True


    formfield_overrides = {
        RedactorField : {'widget': SummernoteWidget},
    }

class ContactAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (

        (('Contact'), {
           'fields': ('image', 'name','position', 'phone_number', 'email', 'in_link',),
       }),

    )
    sortable = 'order'

class ParthnerLogoAdmin(admin.ModelAdmin):
    pass

class MenuLinksAdmin(TabbedTranslationAdmin):

    def has_add_permission(self, request, obj=None):
        info = MenuLinks.objects.all()
        if len(info) == 1:
            return False
        else:
            return True


admin.site.register(Info, InfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ParthnerLogo, ParthnerLogoAdmin)
admin.site.register(MenuLinks, MenuLinksAdmin)
