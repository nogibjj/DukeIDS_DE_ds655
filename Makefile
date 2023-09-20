#Adding this to install all the packages in requirements.txt - I have not included versions of the individual packages in the requirements file
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

#Adding this to format code using black
format:	
	black \Codes/*.py 

test:
	python -m pytest \Codes/Test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=\Codes/Check_.*?py \Codes/*.py

git:
	git add .
	git -c user.name="Divya" -c user.email="<divya.sharma@duke.edu>" commit
	git push -u origin master

all: install format lint test git
