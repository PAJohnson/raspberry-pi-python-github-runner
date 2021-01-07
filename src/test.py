from datetime import datetime
import os

if __name__ == "__main__":
    print(os.path.abspath(os.path.dirname(__file__)))
    with open(os.path.abspath(os.path.dirname(__file__)) + '/../artifacts/output.txt','w') as outfile:
        outfile.write("Hello world! GH Action Artifact")
        outfile.write(datetime.now().strftime("%b-%d-%Y-%H:%M:%S"))