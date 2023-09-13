
def cero(vector, it):
    for t in range(it):
        vector.append(int(0))


def bul(vector, it):
    for y in range(it):
        vector.append(False)


def search(var, vector):
    for m in range(len(vector)):
        if var == vector[m]:
            return m


list_num_article = []
list_can_stock = []
list_price_unit = []

for z in range(10):
    list_num_article.append(input("Enter article's number:"))
    list_can_stock.append(input("Enter stock' amount:"))
    list_price_unit.append(int(input("Enter the unit price")))


# Accumulator of the clients
total_sells_client = []
cero(total_sells_client, 10)

# Booleano (Sells of the articles)
sells = []
bul(sells, 10)

print("DATA CHARGE")
# Data Charge
num_client = int(input("The CLIENT:"))
article_number = input("The article's number:")
units_sells = int(input("The amount of unit sells:"))

while num_client != 0:

    i = search(article_number, list_num_article)

    total = units_sells * list_price_unit[i]
    # Instruction A
    print("N. Client", "N. Article", "Unit sells", "Total")
    print(num_client, "    ", article_number, "      ", units_sells, "     ", total)
    # B
    total_sells_client[num_client-1] += total
    # C
    sells[i] = True

    num_client = int(input("The CLIENT:"))
    if num_client != 0:
        article_number = input("The article's number:")
        units_sells = int(input("The amount of unit sells:"))

# Instruction B
client = 0
high_cliente = 0
for d in range(len(total_sells_client)):
    if total_sells_client[d] > high_cliente:
        high_cliente = total_sells_client[d]
        client = d + 1


print("The client with most sells is the number:", client,)

# Instruction C
print("The article's numbers with no sells are:")
for s in range(len(sells)):
    if not sells[s]:
        print(list_num_article[s])

