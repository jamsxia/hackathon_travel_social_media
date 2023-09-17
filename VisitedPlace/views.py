from django.shortcuts import render, redirect
from .models import VisitedPlace
from django.contrib.auth.decorators import login_required
from .forms import VisitedPlaceForm
import logging
from django.views.generic.edit import FormView

logger = logging.getLogger(__name__)

@login_required
def add_visited_place(request):
    if request.method == 'POST':
        form = VisitedPlaceForm(request.POST, request.FILES)
        if form.is_valid():
            visited_place = form.save(commit=False)
            visited_place.user = request.user
            visited_place.save()
            return redirect('profile')
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = VisitedPlaceForm()

    return render(request, 'VisitedPlace/add_visited_place.html', {'form': form})