from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        has_name = False

        for form in self.forms:

            if form.cleaned_data.get('is_main'):
                if has_name is not True:
                    has_name = True
                else:
                    raise ValidationError('Основным может быть только один раздел!')

        if has_name is not True:
            raise ValidationError('Укажите основной раздел!')

        return super().clean()


class ScopeInline(admin.TabularInline):
    formset = RelationshipInlineFormset
    model = ArticleScope
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ScopeInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
