from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Si vous modifiez ces étendues, supprimez le fichier token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# L'ID de votre fichier Google Sheet.
SPREADSHEET_ID = '1HulF6Yk96EBaTtVyMVvcVayHZruyTu-Ck_5Myfu7VB4'

# Le nom de la plage de données à lire (par exemple, 'Feuille1!A:A' pour la colonne A).
RANGE_NAME = 'Pierre!B:B'

def main():
    """Lit et affiche les valeurs d'une colonne d'un fichier Google Sheet."""
    creds = None
    # Le fichier token.json enregistre les jetons d'accès et d'actualisation de l'utilisateur,
    # et est créé automatiquement lors de la première exécution réussie du flux d'autorisation.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Si aucune information d'identification (credentials) n'est disponible, lancez le flux d'autorisation.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Enregistrez les informations d'identification pour la prochaine exécution
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Appelez l'API Sheets
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                    range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('Aucune donnée trouvée dans la plage spécifiée.')
        else:
            print(f"Contenu de la colonne {RANGE_NAME}:")
            for row in values:
                # Notez que chaque 'row' est une liste, même si nous avons demandé une seule colonne.
                # Nous prenons donc le premier élément de chaque ligne.
                print(row[0])

    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

if __name__ == '__main__':
    main()