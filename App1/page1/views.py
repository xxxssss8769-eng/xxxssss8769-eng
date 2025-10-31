from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Products, Sign

# Create your views here.

def index1(request):
    return render(request, 'page1temp/page1temp1.html')


def product(request):
    # Require sign-in
    username = request.session.get('username')
    if not username:
        # Redirect to sign_in with next param so user returns here after signing in
        signin_url = reverse('sign_in') + f"?next={request.get_full_path()}"
        return redirect(signin_url)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        ptype = request.POST.get('type', '').strip()
        price = request.POST.get('price', '').strip()
        contact = request.POST.get('contact', '').strip()
        active = request.POST.get('active') == 'on'

        errors = []
        if not name:
            errors.append('Name is required.')
        if not ptype:
            errors.append('Type is required.')
        try:
            price_val = int(price)
            if price_val < 0:
                errors.append('Price must be non-negative.')
        except Exception:
            errors.append('Price must be an integer.')

        if errors:
            return render(request, 'products/product.html', {
                'errors': errors,
                'form': {
                    'name': name,
                    'type': ptype,
                    'price': price,
                    'contact': contact,
                    'active': active,
                }
            })

        prod = Products.objects.create(
            name=name,
            type=ptype,
            price=price_val,
            contact=contact,
            active=active,
        )
        return redirect(reverse('product_detail', args=[prod.pk]))

    # GET -> show empty form
    return render(request, 'products/product.html')


def products(request):
    qs = Products.objects.filter(type__in=['sport','offroad','city','hypird']).order_by('name')
    return render(request, 'products/products.html', {'pros': qs})


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def sign_in(request):
    next_url = request.GET.get('next') or request.POST.get('next') or None
    session_username = request.session.get('username')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request, 'page1temp/sign_in.html', {
                'error': 'Please provide both username and password.',
                'username': username,
                'next': next_url,
                'session_username': session_username,
            })

        person, created = Sign.objects.get_or_create(name=username, defaults={'password': password})
        if not created:
            person.password = password
            person.save()
            message = 'Signed in (existing user) — password updated.'
        else:
            message = 'Account created successfully.'

        # Set session so other views can check login
        request.session['username'] = person.name

        # Redirect back to next if provided
        if next_url:
            return redirect(next_url)

        return render(request, 'page1temp/sign_in.html', {
            'success': message,
            'person': person,
            'session_username': request.session.get('username'),
        })

    return render(request, 'page1temp/sign_in.html', {'next': next_url, 'session_username': session_username})


# New views: show filtered lists for New Cars and Hire Cars

def new_cars(request):
    qs = Products.objects.filter(type__in=['New']).order_by('name')
    return render(request, 'products/new_cars.html', {'pros': qs})


def hire_cars(request):
    qs = Products.objects.filter(type__in=['Hair']).order_by('name')
    return render(request, 'products/hire_cars.html', {'pros': qs})
