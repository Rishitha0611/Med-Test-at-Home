# Med-Test-at-Home

#Project Overview:
The main goal of the project is to decrease the medical related issues faced by the public. As there are different kind of diseases a person can suffer from, we predict their best possible outcome with the symptoms they are facing. In this project, we used various data sets for training the machine learning models and we used Flask for model deployment. We used variety of tools like Python, Flask, NumPy, Pandas, HTML, CSS for project deployment.

We used three different endpoints to perform three different operations: 
1. “/”
This endpoint calls the HTML page which is our webpage where user enters the symptoms

2. “/predict”
When user enters the symptoms and clicks on predict button this endpoint is invoked. This is responsible in sending the symptoms entered to prediction function and showing the predicted disease in the output. Also, Precautions are displayed by calling the precaution function using then disease predicted from prediction function

3. “/symptomsList”
This endpoint comes into picture when the symptomsList button is clicked. This helps the user to choose the symptom from the variety of symptoms.

#Results:
In this project we used two machine learning algorithms namely Logistic Regression and Random Forest Classifier. We managed to achieve an accuracy rate of 98.21% using Random Forest Classifier.

#Conclusion:
Training this model with the patients’ data from various medical organizations makes this application a real time solution for the people who cannot afford expensive hospital visits. This application has an accuracy rate of more than 98% which makes the margin of error negligible. One can access this application and make use of it by going through the Source code for the Application.
