from django.core.management.base import BaseCommand, CommandError
from homepage import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponseRedirect, HttpResponse
import datetime

templater = get_renderer('retail')

class Command(BaseCommand):
    help = 'Check for overdue rentals'

    def handle(self, *args, **options):
        rentals = hmod.RentalLineItem.objects.all()
        params = {}
        overdues = {}

        now = datetime.datetime.now().date()

        for rental in rentals:
            if rental.date_due < now:
                overdue = {rental.id: rental}
                overdues[rental.id] = overdue
            else:
                pass

        params['overdues'] = overdues
        return templater.render_to_response(args, '/retail/check_rentals.html', params)
        # return HttpResponseRedirect('/retail/check_rentals.html/')