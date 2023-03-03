import os
import openai
import docker 
import git 
import shutil
import subprocess
import json
import pydriller
import re
# from guesslang import Guess

print("Setting api key...")
openai.organization = ""
openai.api_key = "" #os.getenv("OPENAI_API_KEY")
#print(openai.Model.list())
model_engine = "text-davinci-003" 

print("Done. Creating prompt...")

# prompt = "Hey, Access this repo https://github.com/kliakos/sparkjava-war-example. Go through Readme file and check build commands for this repo. Create a Dockerfile by interpreting commands in ReadMe.md file. Do not print any other code except Dockerfile. Don't print empty lines in response."
user_repo=input("Enter name of repo: ")
folder_name = user_repo.split("/")[-1]



dirpath = os.path.join('./', folder_name)
if os.path.exists(dirpath) and os.path.isdir(dirpath):
    shutil.rmtree(dirpath)

###
try:
    repo = git.Repo.clone_from(user_repo, to_path=folder_name ,branch="main")
except git.exc.GitCommandError:
    repo = git.Repo.clone_from(user_repo, to_path=folder_name ,branch="master")
###


os.chdir(folder_name)
repo_path = os.getcwd()
result = subprocess.run(['github-linguist', '--json'], capture_output=True, text=True)
print(result.stdout)
y = json.loads(result.stdout)
lang_name = list(y.keys())[0]
os.chdir("../")


#https://github.com/kliakos/sparkjava-war-example
prompt = (f"Check README.md file of repo {user_repo} which is written in {lang_name}. What will be appropriate docker base image to run this code? While creating a Dockerfile by interpreting commands in README.md. Use docker base image which is most popular official images & build-worthy. Copy code to workdir in docker and command to run the executable. Do not print any other code except Dockerfile. Don't print empty lines in response.")

print("\n") 
print(prompt)
print("\n")
print("Sending prompt...")
response = openai.Completion.create(engine=model_engine, prompt=prompt, temperature=0.3,max_tokens=100) 
print("Prompt sent. Waiting for response for chatgpt...")
text = response.choices[0].text 
print(text)
text = text.strip()

print("\n")
print(text)
print("\n")
print("Got response...")


with open(f"{folder_name}/Dockerfile", "w") as f:
    print(text, file=f)
print("Dockerfile created...")

client = docker.from_env()
try:
    print("Logging in docker registry...")
    client.login(username="jawanjalaniruddha", password="#Temp1234")
except docker.errors.APIError as api_err:
    print("\nAPIError:", api_err)
except Exception as err:
    print(f"\nUnexpected {err=}, {type(err)=}")
    raise 

print("Building docker image...")
# client = docker.DockerClient(base_url='unix://var/run/docker.sock')
try:
    image = client.images.build(path=folder_name, quiet="True")
    print(image)
except docker.errors.BuildError as build_err:
    print("\nBuildError:", build_err)
    prompt = "Got this error while building the Dockerfile from previous response. "+ str(build_err) + "  update dockerfile which will solve this error. If dockerfile is already present in the repo, optimise the dockerfile. Do not print any other code except Dockerfile. Don't print empty lines in response. "
    print(prompt)
    print("Sending prompt...")
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=100) 
    with open(f'{folder_name}/Dockerfile2', 'w') as f:
        print(text, file=f)
    print("Dockerfile created...")
    image = client.images.build(path=f"{folder_name}/Dockerfile2", quiet="True", fileobj=f"{folder_name}",custom_context=True, tag=folder_name)
    print(image)
except docker.errors.APIError as api_err:
    print("\nAPIError:", api_err)
except TypeError as type_err:
    print("\nTypeError:", type_err)
except Exception as err:
    print(f"\nUnexpected {err=}, {type(err)=}")
    raise


clear = client.images.prune(image)
# os.system('clear')
