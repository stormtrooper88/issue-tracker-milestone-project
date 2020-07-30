from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bug
import datetime
from .forms import BugPostForm

# Create your views here.
def all_bugs(request):
    """
    Create a view that will return a list of all Bugs that were published prior to 'now' and give them the 'bugs.html' template
    """
    bugs = Bug.objects.filter()
    form = BugPostForm(instance=None)
    return render(request, "bugs.html", {"bugs": bugs, 'form': form})

def bug_detail(request, pk):
    """
    Create a view that will return a single Bug object based on the bug ID(pk) and render it to the 'bugdetail.html' template.
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.save()
    return render(request, "bugdetail.html", {'bug': bug})


def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows users to create or edit a post depending if the bug ID is null or not
    """
    print(f"pk =  {pk}, all the bugs with filter: {Bug.objects.filter()}")
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    print(f"This is the bug at the beginning: {bug}")
    if request.method == "POST":
        print("we are in POST")
        form = BugPostForm(request.POST, request.FILES, instance=bug)
        print(f"the form is: {form}")
        if form.is_valid():
            print("the form is valid")
            bug = form.save(commit=False)
            print(f"the date stamp: {datetime.datetime.now()}")
            bug.created_date = datetime.datetime.now()
            bug.save()
            print(f"The bug after saving it: {bug}")
            return redirect(bug_detail, bug.pk)
        print("form is not valid")
    else:
        form = BugPostForm(instance=bug)
        print(f"the form in GET mode: {form}")
    return render(request, 'trackerbugform.html', {'form': form})