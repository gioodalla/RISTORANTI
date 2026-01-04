import os
import subprocess

# --- Configurazione repository ---
repo_path = r'C:\Users\Lorenzo\OneDrive\Documenti\GitHub\RISTORANTI\RISTORANTI'  # METTI QUI il percorso del tuo repo clonato
file_name = 'Ristoranti_Gio_Marty.txt'

# --- Funzione per aggiornare GitHub ---
def aggiorna_github(commit_msg):
    os.chdir(repo_path)
    subprocess.run(['git', 'add', file_name])
    subprocess.run(['git', 'commit', '-m', commit_msg])
    subprocess.run(['git', 'push'])

# --- Inserimento dati ---
nome_ristorante = input('Nome Ristorante:  ')

prv = input('Scrivi la provincia, es PD: ')
provincia = '(' + prv + ')' 
location =  float(input('Location: '))
servizio = float(input('Servizio: '))
conto = float(input('Conto: '))

lista_voti_cibo = []
while True:
    voto = input('Inserisci Voti, per terminare lascia vuoto: ')
    if voto == '':
        break
    lista_voti_cibo.append(float(voto))

if len(lista_voti_cibo) == 0:
    avg = (location + servizio + conto) / 3
else:
    avg = (sum(lista_voti_cibo) + location + servizio + conto) / (len(lista_voti_cibo) + 3)

extra = input('Aggiungi Extra? (Si, No): ')
if extra.lower() == 'si':
    avg += 0.5

# --- Scrittura su file ---
with open(os.path.join(repo_path, file_name), 'a', encoding='utf-8') as f:
    f.write(f'{nome_ristorante} {provincia} {avg:.2f}\n')
    f.write(f'   - Location: {location}\n')
    f.write(f'   - Servizio: {servizio}\n')
    f.write(f'   - Voti Menu\': {lista_voti_cibo}\n')
    f.write(f'   - Conto: {conto}\n')

print("Ristorante aggiunto!")

# --- Aggiorna automaticamente GitHub ---
aggiorna_github(f"Aggiunto ristorante: {nome_ristorante}")
print("File aggiornato anche su GitHub!")
