#Adding this to install all the packages in requirements.txt - I have not included versions of the individual packages in the requirements file
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

#Adding this to format code using black
format:	
	black \Codes/*.py 

test:
	python -m pytest \Codes/Test_*.py
	git push -u origin main

lint:
	pylint --disable=R,C --ignore-patterns=\Codes/Check_.*?py \Codes/*.py

git:	
	git config --global user.name 'github-actions'
	git config --local user.email "action@github.com"
	python \Codes/main.py
	git add \Resources/*
	git commit -m "Updated these files Automatically" || echo "ignore commit failure"
	git push
    env:
	GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

all: install format lint test git
