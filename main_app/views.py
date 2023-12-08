from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'species': 'Zebra Finch', 'description': 'Vibrant and active', 'age': 1},
  {'name': 'Sachi', 'species': 'Gouldian Finch', 'description': 'Colorful and social', 'age': 2},
  {'name': 'Milo', 'species': 'Bengalese Finch', 'description': 'Playful and curious', 'age': 3},
  {'name': 'Bella', 'species': 'Star Finch', 'description': 'Elegant and serene', 'age': 2},
  {'name': 'Jasper', 'species': 'Cherry Finch', 'description': 'Charming and vocal', 'age': 4}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
    })