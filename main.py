from dotenv import load_dotenv
load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print('Hello Gouds')

    res = app.invoke({"question": "what is the capital of France?"})
    
    print(res)
