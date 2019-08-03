from django.shortcuts import render

# Create your views here.
def tool_list(request):
    return render(request, 'dorapp/tool_list.html', {})