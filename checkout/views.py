from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import orderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = orderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KEGsHKU8JxANin5v2WhyRXbGPwz2A1ixi5DQFCTx7Ozt1sXvLD3UTyJzRGLJZ3vEljku6CirnsrEYeeqlSUiLHx00T80ZwKbi',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
