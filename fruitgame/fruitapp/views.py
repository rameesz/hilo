from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import FruitSet
from django.db.models import Q

# View to add a new fruit set with only 1 fruit
def add_fruit_set(request):
    if request.method == 'POST':
        fruit1 = request.POST.get('fruit1')
        result = request.POST.get('result')

        # Save the fruit and result to the database
        if fruit1 and result:
            FruitSet.objects.create(fruit1=fruit1, fruit2='', result=result)
            
            # Redirect to the same page after successful submission
            return redirect('add_fruit_set')
        else:
            # Show an error if fields are missing
            error_message = "Please fill both the fruit and result fields."
            return render(request, 'add_fruit_set.html', {'error_message': error_message})

    return render(request, 'add_fruit_set.html')

# View to search for fruit sets by fruit name
def search_fruit_set(request):
    query = request.GET.get('search_query')
    search_results = None
    if query:
        search_results = FruitSet.objects.filter(
            Q(fruit1__icontains=query)
        )
    return render(request, 'search_fruit_set.html', {'search_results': search_results})

# View to display the details of a specific fruit set
def view_fruit_set(request, id):
    fruit_set = get_object_or_404(FruitSet, id=id)
    return render(request, 'view_fruit_set.html', {'fruit_set': fruit_set})

# View to edit an existing fruit set
def edit_fruit_set(request, id):
    fruit_set = get_object_or_404(FruitSet, id=id)
    
    if request.method == 'POST':
        fruit_set.fruit1 = request.POST['fruit1']
        fruit_set.result = request.POST['result']
        fruit_set.save()
        return redirect('view_fruit_set', id=id)
    
    return render(request, 'edit_fruit_set.html', {'fruit_set': fruit_set})


def list_fruit_sets(request):
    fruit_sets = FruitSet.objects.all().order_by('id')  # Fetch all records from the model
    return render(request, 'list_fruit_sets.html', {'fruit_sets': fruit_sets})