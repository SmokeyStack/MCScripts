import requests, zipfile, io, shutil, os
from bs4 import BeautifulSoup

print('start')

headers = {"User-agent": 'YOUR-USER-AGENT'}

URL = "https://www.minecraft.net/en-us/download/server/bedrock"
page = requests.get(URL, headers=headers)
if page.status_code == 200:
    print('Success!')
elif page.status_code == 404:
    print('Not Found.')

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="check-to-proceed px-3")

test = []
for job_element in job_elements:
    title_element = job_element.find("a", class_="btn btn-disabled-outline mt-4 downloadlink")
    test.append(title_element["href"])
testa = test[0]

links = [
    testa,
    'https://aka.ms/behaviorpacktemplate',
    'https://aka.ms/resourcepacktemplate'
]  # Links to downloads
folder = ['BDS', 'behaviour_pack', 'resource_pack']  # Folder names
count = 0
repo = 'vanilla_packs'  # Repo folder

# Checks if there are old packs and deletes them
for x in folder:
    if (os.path.isdir(folder[count])):
        shutil.rmtree('./' + folder[count])
    if (os.path.isdir('./' + repo + '/' + folder[count])):
        shutil.rmtree('./' + repo + '/' + folder[count])
    count += 1
print('Old Packs Deleted!')
count = 0

# Downloads the packs
for x in links:
    r = requests.get(x)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('./' + folder[count])
    count += 1
print('Packs Downloaded!')
count = 0

# Moves the packs into the repo folder
for x in folder:
    src = './' + folder[count]
    if (os.path.isdir('./' + repo)):
        dest = './' + repo
    else:
        os.mkdir('./' + repo)
        dest = './' + repo
    shutil.move(src, dest, copy_function=shutil.copytree)
    count += 1
print('Packs Moved!')