from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bug
from .forms import BugPostForm

# Create your views here.
def all_bugs(request):
    """
    Create a view that will return a list of all Bugs that were published prior to 'now' and give them the 'bugs.html' template
    """
    bugs = Bug.objects.filter(created_date)()).order_by('-created_date')
    return render(request, "bugs.html", {"bugs": bugs})

def bug_detail(request, pk):
    """
    Create a view that will return a single Bug object based on the bug ID(pk) and render it to the 'bugdetail.html' template.
    """
    bug = get_object_or_404(Bug)
    bug.views += 1
    bug.save()
    return render(request, "bugdetail.html", {'bug': bug})


def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows users to create or edit a post depending if the bug ID is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugPostForm(request.POST, request.FILES, instance=bug)
        if form.is.valid():
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugPostForm(instance=bug)
    return render(request, 'bugs.html', {'form': form})