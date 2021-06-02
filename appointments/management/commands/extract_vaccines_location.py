from django.core.management import BaseCommand
import pandas as pd
from appointments.models import VaccineLocation


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        locations_array = []

        def populate_locations(row):
            locations_array.append(
                VaccineLocation(cnes=row['cod_cnes'], name=row['nom_estab'], address=row['dsc_endereco'],
                                neighborhood=row['dsc_bairro'], city=row['dsc_cidade']))

        try:
            print("Importando os locais de vacina...")
            locations = pd.read_csv("appointments/inputs/ubs.csv", encoding='utf-8')
            print("Adicionando no banco de dados...")
            locations.apply(populate_locations, axis=1)
            VaccineLocation.objects.bulk_create(locations_array)
            print("O csv foi importado com sucesso.")

        except FileNotFoundError:
            print("O arquivo csv não foi encontrado.")
        except Exception as e:
            print(e)
