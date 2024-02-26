# DukeIDS706_DE Week 02 Assignment [![Python CI](https://github.com/nogibjj/DukeIDS_DE_ds655/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/DukeIDS_DE_ds655/actions/workflows/main.yml)


This repository is cloned from the template created in Week01 (https://github.com/DivyaSharma0795/DukeIDS706_DE_ds655)

Files in this repository include:


## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages, and in addition - Pandas, Seaborn, and Matplotlib


## 3. Codes
  This folder contains all the code files used in this repository - the project for this week is _Pandas Descriptive Statistics Script_ , I will be using the Iris dataset for this analysis
  The code files in this folder are -
   * `Pandas_Description.py` - this is a python function to share the description of a dataframe
   * `Pandas_Plot.py` - this is a python function to plot a chart from the dataframe and save it as a png file
   * `Test_Week2_Pandas.py` - this is a python code to test the functions defined - this function can also be called by the pytest module in the Makefile of the repository.

     ![Make Test Output](https://github.com/nogibjj/DukeIDS706_ds655_Week02/blob/main/Resources/Week2_Successful_Test.png?raw=true)


## 4. Resources
  -  This folder contains any other files relevant to this project. Currently, I have added -
  * `iris_dataset` - this is a copy of the iris dataset, in case the link is not accessible (Original link - https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/Iris_Data.csv)

  
  * `PlotImage.png` - this is the chart plotted using the `pandas_plot.py` script from the Codes folder - this gets automatically saved here every time the code is run, along with the timestamp


    ![Plot Image Output](https://github.com/nogibjj/DukeIDS706_ds655_Week02/blob/main/Resources/PlotImage.png?raw=true)


  * `Summary.md` - This is a markdown file containing the Summary Statistics created using the describe() function in Pandas. This file also contains a timestamp for when it was created, and the image that was generated in the code (PlotImage.png)

    ![Summary Screenshot](https://github.com/nogibjj/DukeIDS706_ds655_Week02/blob/main/Resources/Week2_SummaryMarkdown.png?raw=true)


  *_The PlotImage.png file and the Summary.md file are auto-created every time a workflow is run, using the YML File defined in CI Automation
  * This folder also contains all the images used in the README
    
## 5. CI/CD Automation Files


  ### 5(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 5(b). Github Actions
  Github Actions uses the `main.yml` file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions


  ### 5(c). Devcontainer
  The `.devcontainer` folder mainly contains two files - 
    * `Dockerfile` defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
    * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
