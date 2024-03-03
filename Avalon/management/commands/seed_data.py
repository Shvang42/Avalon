from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Seed the database with test data"
    
    def handle(self, *args, **options):
        # create any test data
        
        
        self.stdout.write(self.style.SUCCESS("Successfully seeded test data."))