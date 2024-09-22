# astrological-sign-app
# Find out more about your astrological sign and its signification using this Python web app built with Streamlit.

This project calculates a user's astrological sign based on their birthdate and displays a relevant description of it. It was made for a university project at HEC Paris.

## Installation and Set-up

This section is for users who have Python and pip already installed and who wish to run the app locally.

### 1. Clone the repo to your machine. 

Open your terminal an run the following bash command:

Use ```git clone https://github.com/tesscln/astrological-sign-app.git ```

Then, navigate to the directory: ```cd astrological-sign-app.```

### 2. Create a virtual environment

Depending on what you use locally (conda, venv, virtualenv).

### 3. Install the required dependencies

```pip install -r requirements.txt```

### 4. Run the app.py file.

```streamlit run app.py```

This will open your default browser with a webpage, asking you for your name and birthday. 
Then, by clicking on 'Calculate my sign', you will get information about your astrological sign and its signification.

### 5. Stop the app

To stop the Streamlit app, return to the terminal and press ```Ctrl + C```.

## How to run the app in a Docker container

If you don't want to deal with dependency management, you can use Docker to run the app in an isolated environment.

### 1. Clone the repo to your machine. 

Open your terminal an run the following bash command:

Use ```git clone https://github.com/tesscln/astrological-sign-app.git ```

Then, navigate to the directory: ```cd astrological-sign-app.```

### 2. Make sure that Docker is installed on your machine.

Check if it is installed by running ```docker --version``` in your terminal. 
If it is not installed, you can install it on your desktop [here](https://www.docker.com) and follow the instructions.

### 3. Build the Docker image

```docker build -t astrological-sign-app .```

### 4. Run the Docker container

```docker run -p 8501:8501 astrological-sign-app```

Open your browser and go to **http://localhost:8501**.