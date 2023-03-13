from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Created to Calculate Subtotal in Shopping Cart
    Credit : Code Institutes Boutique Ado project
    """
    return price * quantity
