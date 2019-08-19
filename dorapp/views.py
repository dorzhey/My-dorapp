from django.shortcuts import render, get_object_or_404
from .models import Tool

# Create your views here.
def tool_list(request):
    tools = Tool.objects.all()
    return render(request, 'dorapp/tool_list.html', {'tools':tools})

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    return render(request, 'dorapp/tool_detail.html', {'tool': tool})