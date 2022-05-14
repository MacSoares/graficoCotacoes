from decimal import Decimal
from django.test import TestCase
from django.core.management import call_command, get_commands
from graph.management.commands.charge_since_year import Command
from graph.models import Currency


class ImportCurrencyTest(TestCase):
    def setUp(self):
        call_command("charge_since_year", "--year", "2022")
        # pass

    def test_command_exists(self):
        commands = get_commands()
        command_name = "charge_since_year"
        self.assertIn(command_name, commands)

    def test_get_saved_value(self):
        obj = Currency.objects.get(base_date='2022-05-12')
        self.assertIsNotNone(obj)
        self.assertEqual(obj.brl, Decimal("5.2038"))

    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
