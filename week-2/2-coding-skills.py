import json


print(json.load(open('data.json', 'r'))['people'][0]['skills'][2]['name'])



def main():
    pass

if __name__ == '__main__':
    main()