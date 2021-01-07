from datetime import datetime
import pathlib


if __name__ == "__main__":
    print(pathlib.Path(__file__).parent.absolute())
    with open('artifacts/output.txt','w') as outfile:
        outfile.write("Hello world! GH Action Artifact")
        outfile.write(datetime.now().strftime("%b-%d-%Y-%H:%M:%S"))