mkdir ./installed
pip3 install -r requirements.txt --target installed --implementation cp --python-version 37 --no-deps
cp src/* installed/