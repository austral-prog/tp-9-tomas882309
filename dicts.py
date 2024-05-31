
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    set1 = set (items)
    tupla = tuple (items)
    mapa = {}
    for elemento in set1:
        num = tupla.count (elemento)
        mapa[elemento] = num
    return (mapa)


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    set1 = set (items)
    tupla = tuple (items)
    mapa = inventory
    for elemento in set1:
        num = tupla.count (elemento)
        if elemento in inventory:
            inventory[elemento] = num + mapa[elemento]
        else:
            inventory[elemento] = num
    return (inventory)

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    set1 = set (items)
    tupla = tuple (items)
    mapa = inventory
    for elemento in set1:
        num = tupla.count (elemento)
        if num > mapa[elemento]:
            num = mapa[elemento]
        inventory[elemento] = mapa[elemento] - num
    return (inventory)


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory.keys():
        del inventory [item]
        return (inventory)

    else:
        return (inventory)


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    dic = []
    for elemento, valor in inventory.items():
        if valor != 0:
            tupla = (elemento, valor)
            dic.append (tupla)
    return (dic)



