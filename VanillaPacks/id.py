from bs4 import BeautifulSoup

with open("path_to_Addons.html", "r") as f:
    soup = BeautifulSoup(f, 'html.parser')
f = open("block_id.txt", "a")
f.write(soup('table')[2].get_text().replace("\n\n", "").replace(" ", "")[5:])

with open("entity_id.txt", "a") as f:
    test = soup('table')[3]
    result = []
    allrows = test.findAll('tr')
    for row in allrows:
        cols = row.find_all('td')
        cols = [temp.text.strip() for temp in cols]
        result.append(cols)
    for x in range(1, len(result)):
        f.write(result[x][0])
        f.write('\n')

with open("item_id.txt", "a") as f:
    test = soup('table')[9]
    result = []
    allrows = test.findAll('tr')
    for row in allrows:
        cols = row.find_all('td')
        cols = [temp.text.strip() for temp in cols]
        result.append(cols)
    for x in range(1, len(result)):
        f.write(result[x][0])
        f.write('\n')