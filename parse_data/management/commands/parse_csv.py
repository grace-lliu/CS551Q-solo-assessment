import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from parse_data.models import Product, ProductDetail

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # delete existing data
        Product.objects.all().delete()
        print("Table Product dropped successfully")
        ProductDetail.objects.all().delete()
        print("Table ProductDetail dropped successfully")

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/parse_data/data/AppleStore.csv', newline='', encoding='utf-8') as f:

            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                # extract data from csv row
                product_id = int(row[0])
                size_bytes = int(row[1])
                currency = row[3]
                price_str = row[4].strip()
                rating_count_tot = row[5]
                rating_count_ver = row[6].strip()
                user_rating = row[7].strip()
                user_rating_ver = row[8].strip()
                ver = row[9]
                cont_rating = row[10]
                prime_genre = row[11]
                sup_devices_num = int(row[12])
                ipadSc_urls_num = int(row[13])
                lang_num = int(row[14]) if row[14] else 0
                vpp_lic = bool(int(row[15])) if row[15] else bool(0)

                # create Product object and save to database
                product = Product(id=product_id, currency=currency, price=price_str,
                                  rating_count_tot=rating_count_tot, user_rating=user_rating)
                product.save()

                # create ProductDetail object and save to database
                product_detail = ProductDetail(product_id=product, size_bytes=size_bytes,
                                                rating_count_ver=rating_count_ver, user_rating_ver=user_rating_ver,
                                                ver=ver, cont_rating=cont_rating, prime_genre=prime_genre,
                                                sup_devices_num=sup_devices_num, ipadSc_urls_num=ipadSc_urls_num,
                                                lang_num=lang_num, vpp_lic=vpp_lic)
                product_detail.save()
