import os

def walk(path_address):
    files = []
    for r,d,f in os.walk(path_address):
        for file in f:
            print(r)
            print(d)
            print(f)
            files.append(os.path.join(r,file))
    print(files)

if __name__ == "__main__":
    walk('C://Users//hdargaye//Desktop//CodePlayground//PyPlayground')
