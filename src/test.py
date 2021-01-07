from datetime import datetime

if __name__ == "__main__":
    with open('output'+datetime.now().strftime("%b-%d-%Y-%H:%M:%S")+'.txt','w') as outfile:
        outfile.write("Hello world! GH Action Artifact")
        outfile.write(datetime.now().strftime("%b-%d-%Y-%H:%M:%S"))