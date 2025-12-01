from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from catalog.models import Category, Product
import json, os
from pathlib import Path

class Command(BaseCommand):
    help = "Load mock products and ensure admin user"

    def add_arguments(self, parser):
        parser.add_argument("--mock", default=None, help="Path to mock products.json")

    @transaction.atomic
    def handle(self, *args, **opts):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin")
            self.stdout.write(self.style.SUCCESS("Created admin:admin"))
        mock_path = opts["mock"]
        if not mock_path:
            # default path relative to project
            mock_path = Path(__file__).resolve().parents[5] / "frontend" / "react-trabajo" / "public" / "mock" / "products.json"
        mock_path = Path(mock_path)
        if not mock_path.exists():
            self.stdout.write(self.style.WARNING(f"Mock not found at {mock_path}"))
            return
        data = json.loads(mock_path.read_text())
        # categories
        cat_map = {}
        for p in data:
            cname = p.get("category","General")
            slug = cname.lower().replace(" ","-")
            cat, _ = Category.objects.get_or_create(slug=slug, defaults={"name": cname})
            cat_map[cname] = cat
        # products
        for p in data:
            Product.objects.update_or_create(
                id=p["id"],
                defaults={
                    "name": p["name"],
                    "price": int(p["price"]),
                    "desc": p.get("description",""),
                    "tracks": p.get("tracks"),
                    "category": cat_map.get(p.get("category","General")),
                }
            )
        self.stdout.write(self.style.SUCCESS(f"Loaded {len(data)} products"))