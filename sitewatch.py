import requests
import json

def vertifier_site(url):

        reponses = []
        for site in url:
            site = site.strip()           
            if not site:
                reponses.append({
                    "url":site,
                    "statut":"invalide",
                    "erreur":"url invalide"
                    })
                continue
            if not site.startswith("https://") and not site.startswith("http://"):
                site = "https://" + site

            try:
                reponse = requests.get(site,timeout=5)
                reponse.raise_for_status()
                if reponse.status_code == 200:
                    reponses.append({
                        "url":site,
                        "statut_code":reponse.status_code,
                        "temps de chargement": reponse.elapsed.total_seconds(),
                        "statut":"ok"
                        })
                    
            except requests.RequestException as e:
                reponses.append({
                    "url":site,
                    "statut":"erreur",
                    "erreur": str(e)
                    })

        return reponses



with open('sites.json') as f:
     sites = json.load(f)['sites']

resulats = vertifier_site(sites)

print(resulats)

with open("resultats.json", 'w', encoding="utf-8") as f:
    json.dump(resulats, f, ensure_ascii=False, indent=2)

