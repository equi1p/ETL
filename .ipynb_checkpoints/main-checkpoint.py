from extract import extract
from transform import transform
from load import load

def main():
    data = extract()
    data_transformed = transform(data)
    load(data_transformed)


if __name__ == '__main__':
    main()