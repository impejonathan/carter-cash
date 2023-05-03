# carter-cash
projet personnel scraping + analyse + créeation du app streamlite 


# Choix de pneus

Ce projet personnel vous permet de choisir des pneus selon leur largeur, hauteur, diamètre et autres informations. Il utilise des données provenant du site web de Carter-Cash.

## Analyse du site web de Carter-Cash

J'ai analysé la structure du site web de Carter-Cash pour récupérer les informations nécessaires à mon projet. J'ai utilisé les xpath pour récupérer les informations des pneus à l'URL https://www.carter-cash.com/pneus/205-55-r16.

## Spider

J'ai créé une spider simple pour analyser les résultats et les nettoyer pour éviter de devoir les nettoyer à nouveau avec pandas plus tard. Ensuite, j'ai créé une spider qui récupère toutes les dimensions de pneus en une seule fois, soit 490 URL pour le crawl spider. Le crawl spider des 490 URL m'a permis de récupérer plus de 7300 pneus disponibles sur le site de Carter-Cash en environ deux heures.

## Analyse de données

J'ai ensuite effectué une analyse générale des informations sur les pneus en faisant des histogrammes sur toutes les informations et des boxplots en prenant en cible le prix.

## Application Streamlite

J'ai créé une application Streamlite qui permet de choisir des pneus en fonction des informations souhaitées et j'ai inclus également l'analyse sur le site.

## Mise en ligne

Enfin, j'ai mis en ligne l'application gratuitement grâce à https://share.streamlit.io/.

## Dépendances

Les dépendances requises pour ce projet sont :

- Scrapy
- Pandas
- Streamlit
- ploty

## Comment installer les dépendances

Pour installer les dépendances, vous pouvez utiliser pip. Voici les commandes pour installer les dépendances :

pip install scrapy
pip install pandas
pip install streamlit

rust
Copy code

## Comment utiliser l'application

Pour utiliser l'application, vous pouvez exécuter la commande suivante :

streamlit run app.py

vbnet
Copy code

Cela ouvrira l'application dans votre navigateur par défaut. Vous pourrez alors choisir les informations de pneus que vous recherchez et obtenir les résultats correspondants.

J'espère que vous apprécierez ce projet et n'hésitez pas à me contacter si vous avez des questions ou des commentaires ! 