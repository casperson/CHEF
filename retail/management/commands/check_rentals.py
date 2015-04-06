from django.core.management.base import BaseCommand, CommandError
from homepage import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from homepage import dmp_render
import datetime
import os

templater = get_renderer('retail')

class Command(BaseCommand):
    help = 'Check for overdue rentals'

    def handle(self, *args, **options):
        rentals = hmod.RentalLineItem.objects.all()
        params = {}
        overdues = []

        now = datetime.datetime.now().date()

        for rental in rentals:
            if rental.date_due < now:
                overdues.append(rental)
            else:
                pass

        for overdue in overdues:
            fee = None
            if overdue.rentable_item is not None:
                fee = hmod.RentableItem.objects.get(id=overdue.rentable_item.id)
            elif overdue.wardrobe_item is not None:
                fee = hmod.RentableItem.objects.get(id=overdue.wardrobe_item.id)

            item = hmod.LineItem.objects.get(rental_line_item=overdue)
            print(item.shopping_cart)
            user = hmod.User.objects.get(id=item.shopping_cart.user_id)
            dayslatecalc = now - overdue.date_due
            dayslate = dayslatecalc.days.numerator

            overdueItem = {
                'id': item.id,
                'name': item.rental_item_name,
                'datedue': overdue.date_due,
                'price': fee.price_per_day,
                'dayslate': dayslate,
                'latefee': fee.price_per_day * dayslate,
                'today': now
            }

            params['item'] = item
            params['user'] = user
            params['overdueItem'] = overdueItem
            params['overdues'] = overdues

            emailsubject = "Overdue Rental Items"
            emailbody = dmp_render('check_rentals.html', params)

            send_mail(emailsubject,emailbody,'sterling@thecolonialheritage.me', user.email,
                      html_message=emailbody, fail_silently=False)