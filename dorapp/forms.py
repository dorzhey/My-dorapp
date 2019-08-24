from django import forms

from .models import Tool

class ToolForm(forms.ModelForm):

    class Meta:
        model = Tool
        fields = ('tool_name', 'description',)