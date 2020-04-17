# Coronavirus-Prediction
ML-Model-Flask-Deployment
This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API
Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.
Project Structure
This project has four major parts :
1.	model.py - This contains code that our Machine Learning model to predict Corona Patient absed on training data in 'dataset.csv' file.
2.	app.py - This contains Flask APIs that receives Corona Patient details through GUI or API calls, computes the precited value based on our model and returns it.
3.	request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4.	templates - This folder contains the HTML template to allow user to enter  Patient detail and displays the predicted that is Corona Patient or not .
Running the project
1.	Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a file covid.pkl
2.	Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.
3.	Navigate to URL http://localhost:5000
 
Enter valid numerical values in all 5 input boxes and hit Predict.
If everything goes well, you should be able to see the predcited Corona Patient is positive or not on the HTML page!  
