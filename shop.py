from pathlib import Path
import shop_tools


base_dir = Path(__file__).parent
output_path = base_dir / "index.html"
url = "https://fakestoreapi.com/products?limit=6"

# Lade die Produkte, erzeuge das HTML und schreibe index.html.

products = shop_tools.load_products(url)

product_cards = shop_tools.build_product_cards(products)

html = shop_tools.build_shop_html(product_cards)

with output_path. open("w", encoding="utf-8") as html_file:
    html_file.write(html)

print(output_path)    

