import requests

BASE_URL = "http://127.0.0.1:8000/"

RETRIEVER_ROUTE_MAP = {
    "lli": "advice_lli",
    "chr": "advice_chroma_db"
}


def get_advice(query, retriever):
    data = {
        "query": query,
    }
    assistant_url = RETRIEVER_ROUTE_MAP[retriever]
    response = requests.post(BASE_URL+assistant_url, json=data).json()
    advice = response["advice"]
    print(advice)


def main():
    while True:

        query_input = input("Enter a query: ")

        retriever_input = input("Enter the retriever identifier: ")

        if query_input is not None and retriever_input is not None:
            print("One sec...")
            get_advice(query_input, retriever_input)

        else:
            break

if __name__ == "__main__":
    main()