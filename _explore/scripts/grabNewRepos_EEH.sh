export PATH_TO_CONFIG="../../_config.yml"

# Basic script run procedure
function runScript() {
    echo "Run - $1"
    python -u $1
    ret=$?
    # errorCheck "$1"
}

# RUN THIS FIRST
echo about to run python script import_code_json.py
runScript import_code_json.py
echo ran script import_code_json.py
