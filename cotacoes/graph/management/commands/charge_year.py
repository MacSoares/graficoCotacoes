import requests
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext as _
from graph.models import Currency


class Command(BaseCommand):
    help = 'Charge database from currency API'

    def add_arguments(self, parser):
        parser.add_argument(
            "--year",
            type=int,
            help=_("Define the year to run charge"),
        )

    def handle(self, *args, **options):
        ini = datetime.now()
        today = datetime.today()
        year_start = datetime(options["year"], 1, 1)
        date_control = year_start

        while date_control <= today:
            url = f"https://api.vatcomply.com/rates?base=USD&date={date_control.date()}"
            response = requests.get(
                url, data={}
            )

            if response.status_code == 200:
                response = response.json()
                rates = response["rates"]
                base_date = response["date"]
            else:
                raise Exception("Vatcomply endpoint not reachable")

            usd = rates["USD"]
            eur = rates["EUR"]
            jpy = rates["JPY"]

            Currency.objects.update_or_create(
                usd=usd, eur=eur, jpy=jpy, base_date=base_date)
            date_control = date_control + timedelta(days=1)

        self.stdout.write(
            self.style.SUCCESS(
                _("Runtime was: {}".format((datetime.now() - ini))))
        )
