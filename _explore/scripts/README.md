# Updating the visualizer

These are a set of scripts for updating the local github data in this repository, used as the source for displaying the content.

## Overview of the nmfs-opensci changes

- Made a script _explore/scripts/import_code_json.py to get the json from data exported from calles to GithHub API and put it in the _data folder
- Changed BUILD.sh to use that
- edited _config.yml
- created code.json in nmfs-opensci/NMFS_repos
- made a reqular (classic) personal GitHub token and saved to my .zsh file

#### high level overview
- Developer clicks on green "Use This Template" button on the <a href="https://github.com/JustinGOSSES/awesome-list-visual-explorer-template">awesome-list-visual-explorer-template repository page</a>. 
- They change information in the _config.yml file
- They install ruby and jekyl 
- They change directory into `_explore/scripts` and follow the README there to install the python dependencies in an virtualenv. 
- They run the bash script in the `_explore/scripts` directory called `grabNewRepos.sh`. This grabs github URLs from the README whose address was added to the `_config.yml` file and puts them in the `_explore/input_lists.json` file. 
- They run the bash script in the `_explore/scripts` directory called `BUILD.sh`. This is the main build script for the repository and runs a bunch of python files in the scripts folder and also calls the GitHub API to get information like stars and contributors from each GitHub code repository listed in `input_lists.json`. It also replaces the name of the repository used in the template with the name of the new repository listed in `_config.yml`.
- Run `bundle exec jekyll serve` to start up a server that will show a local version of the webpage at http://127.0.0.1:4000/nmfs-repos-visual-explorer
- Push up to GitHub and turn on GitHub Pages for the repository and the visual explorer page will appear.

## Get set up

* This workflow needs Python. So install that if needed.
* Open a Terminal
* Cd to nmfs-repos-visual-explorer
* `bundle install`

Running this will install everything in your Gemfile (including Jekyll). Note, probably won't work. So Google 'install jekyll' for your OS for updated instructions.

* Set up the environment variable for your token. Use a personal access token. I don't think it needs any permissions.
```
echo 'export GITHUB_API_TOKEN=xyz' >> ~/.zshenv
```

## Now start building!

This is all from a zsh Terminal. If your not using that, then you'll need to store your GitHub API token in a different place, i.e. wherever bash needs it.

```
# Create a Python virtual environment
virtualenv -p python3 venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script to get details from json file
bash grabNewRepos_EEH.sh

# Run the collection script
# This takes a while as it uses the GitHub API to get info
bash BUILD.sh

# Serve the Jekyl Page
bundle exec jekyll serve
```

It should show up. If not go here, <http://127.0.0.1:4000/nmfs-repos-visual-explorer/> in a web browser.

Then push everything to GitHub. If you have Pages on, it should magically appear.
