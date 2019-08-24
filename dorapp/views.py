from django.shortcuts import render, get_object_or_404
from .models import Tool
from .forms import ToolForm
from django.shortcuts import redirect
from django.utils import timezone
from django import forms

# Create your views here.
def tool_list(request):
    tools = Tool.objects.all()
    return render(request, 'dorapp/tool_list.html', {'tools':tools})

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    return render(request, 'dorapp/tool_detail.html', {'tool': tool})

def tool_new(request):
    if request.method == "POST":
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.author = request.user
            tool.stock_date = timezone.now()
            tool.save()
            return redirect('tool_detail', pk=tool.pk)
    else:
        form = ToolForm()
    return render(request, 'dorapp/tool_edit.html', {'form': form})