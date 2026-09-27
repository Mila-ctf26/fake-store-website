import requests

# schaut wofür pass genutzt wird und überlegt, ob ihr das später noch braucht

def load_products(url):
    # Lade und returne die Produktdaten.
    response = requests.get(url)
    products = response.json()
    #print(products[0])
    return products


def build_product_cards(products):
    # Erzeuge und returne alle Produktkarten als einen String.
    cards = ""
    for product in products:
        title = product["title"]
        category = product["category"]
        price = product["price"]
        image = product["image"]
        card = f"""
        <article class="product">
    <img src="{image}" alt="{title}">
    <h2>{title}</h2>
    <p class="category">{category}</p>
    <p class="price">{price:.2f}€</p>
     </article>
    """
        cards += card
    return cards  


def build_shop_html(product_cards):
    # Setze die Karten in ein vollständiges HTML-Dokument ein.
    html = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
    <header>
    <h1>Code & Style Shop</h1>
    <p>Sechs Produkte, live aus einer API geladen.</p>
    </header>

    <main class="products">
        {product_cards}
    </main>    

    </body>
    </html>
    """    
    return html
