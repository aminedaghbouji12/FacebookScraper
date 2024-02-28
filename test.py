import requests
from fastapi.testclient import TestClient
import main2

BASE_URL = "http://localhost:8000"

ROOT_ENDPOINT = "/"
SCRAP_ENDPOINT = "/scrap/{page_name}"

test_client = TestClient(main2.app)


def test_root_endpoint():
    response = test_client.get(ROOT_ENDPOINT)
    expected_text = "Welcome to my Facebook scraping service"
    
    assert response.status_code == 200
    assert expected_text in response.text


def test_scrap_endpoint():
    page_name = "Golden cars"
    response = test_client.get(SCRAP_ENDPOINT.format(page_name=page_name))
    assert response.status_code == 200

    expected_scraped_posts = [{
  "_id": { "$oid": "62098594a574744959073812"
    },
  "post_id": {
    "$numberLong": "2429859013931223"
  },
  "text": "☛Vous souhaitez effectuer la vente de votre #véhicule 🚗🚙 avec le meilleur #Prix ⁉️\nNous rachetons de suite.\n☛#Contactez nous pour profiter des #services offerts par notre showroom : #Vente / #Achat / #Echange.\n📲 Contact : 20 385 000 / 24 385 000\n✉ E mail : goldencars.tn@gmail.com\n📌 Route de Marsa Cité Taieb Mhiri Elaouina Tunis Tunisie. ( En face de l'ambassade des États-Unis )",
  "post_text": "☛Vous souhaitez effectuer la vente de votre #véhicule 🚗🚙 avec le meilleur #Prix ⁉️\nNous rachetons de suite.\n☛#Contactez nous pour profiter des #services offerts par notre showroom : #Vente / #Achat / #Echange.\n📲 Contact : 20 385 000 / 24 385 000\n✉ E mail : goldencars.tn@gmail.com\n📌 Route de Marsa Cité Taieb Mhiri Elaouina Tunis Tunisie. ( En face de l'ambassade des États-Unis )",
  "shared_text": {
    "$numberDouble": "NaN"
  },
  "time": "2024-01-24 13:24:50",
  "timestamp": 1579868690,
  "image": "https://scontent.ftun15-1.fna.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/83083103_2429866977263760_1290413187392339968_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=8024bb&_nc_ohc=dLWUrJfla6EAX-uC-F0&_nc_oc=AQn5zE4BnaZQpjcUZBdOHUwvIMd3DQ34z3Sj8PfZsH7_UlYjKJ2VzueybTIcj5F8oNk&_nc_ht=scontent.ftun15-1.fna&oh=00_AT_ncqMmf7QqVElaT0gfn5Kl8fap0Nsj-el2NtxC_Z2Tmg&oe=622D31A7",
  "image_lowquality": "https://scontent.ftun15-1.fna.fbcdn.net/v/t1.6435-9/cp0/e15/q65/s320x320/83083103_2429866977263760_1290413187392339968_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=8024bb&_nc_ohc=dLWUrJfla6EAX-uC-F0&_nc_oc=AQn5zE4BnaZQpjcUZBdOHUwvIMd3DQ34z3Sj8PfZsH7_UlYjKJ2VzueybTIcj5F8oNk&_nc_ht=scontent.ftun15-1.fna&oh=00_AT8Ko8R05pd8vfzChTYK_8i6PxSghFdXVpWVt-az6rJalg&oe=6230CEA5",
  "images": "['https://scontent.ftun15-1.fna.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/83083103_2429866977263760_1290413187392339968_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=8024bb&_nc_ohc=dLWUrJfla6EAX-uC-F0&_nc_oc=AQn5zE4BnaZQpjcUZBdOHUwvIMd3DQ34z3Sj8PfZsH7_UlYjKJ2VzueybTIcj5F8oNk&_nc_ht=scontent.ftun15-1.fna&oh=00_AT_ncqMmf7QqVElaT0gfn5Kl8fap0Nsj-el2NtxC_Z2Tmg&oe=622D31A7']",
  "images_description": "[\"May be an image of text that says 'GOLDEN CARS Vente Achat Echange Showroom Golden Cars, Route de Marsa Cité Taïeb Mhiri Elaouina Tunis Tunisie. (En face de l'ambassade des Etats Unis) NOUS RACHETONS VOTRE VÉHICULE RAPIDEMENT Paiments de Suite TEL: 24 385 O00 Nous offrons les meitleurs prix'\"]",
  "images_lowquality": "['https://scontent.ftun15-1.fna.fbcdn.net/v/t1.6435-9/cp0/e15/q65/s320x320/83083103_2429866977263760_1290413187392339968_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=8024bb&_nc_ohc=dLWUrJfla6EAX-uC-F0&_nc_oc=AQn5zE4BnaZQpjcUZBdOHUwvIMd3DQ34z3Sj8PfZsH7_UlYjKJ2VzueybTIcj5F8oNk&_nc_ht=scontent.ftun15-1.fna&oh=00_AT8Ko8R05pd8vfzChTYK_8i6PxSghFdXVpWVt-az6rJalg&oe=6230CEA5']",
  "images_lowquality_description": "[\"May be an image of text that says 'GOLDEN CARS Vente Achat Echange Showroom Golden Cars, Route de Marsa Cité Taïeb Mhiri Elaouina Tunis Tunisie. (En face de l'ambassade des Etats Unis) NOUS RACHETONS VOTRE VÉHICULE RAPIDEMENT Paiments de Suite TEL: 24 385 O00 Nous offrons les meitleurs prix'\"]",
}]
    assert response.json() == {"scrapedPosts": expected_scraped_posts}


if __name__ == "__main__":
    test_root_endpoint()
    test_scrap_endpoint()
    print("All tests passed successfully!")
