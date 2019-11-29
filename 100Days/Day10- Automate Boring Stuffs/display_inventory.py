def displayInventory():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    for k, v in stuff.items():
        print(f'{k}  : {v}')


if __name__ == "__main__":
    displayInventory()