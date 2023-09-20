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
	run: |
		python \Codes/main.py
		git config user.name "Divya"
		git config user.email "divya.sharma@duke.edu"
		git add .
		git commit -m "Updated files"
		git push -u origin main
	env:
	        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

all: install format lint test git
