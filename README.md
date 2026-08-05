Calorie Predictor

Calorie Predictor is a machine learning project that uses a Decision Tree Regressor to estimate the number of calories burned during a workout.

The model takes the following input features:

duration_s – workout duration (seconds),
hr_avg – average heart rate (BPM),
training_load – training load,
cardio_load – cardiovascular load,
recovery_time_s – estimated recovery time (seconds),
age – user's age.

After providing the required parameters, the model returns an estimated number of calories burned during the workout.

Technologies : 
-Python
-FastAPI
-Scikit-learn
-Pandas
-Numpy
-Docker
-Pydantic
-Joblib

Running the application : 
1. Clone the repository - git clone [<repo_url>](https://github.com/ob3x/calorie-predictor)
2. Build the Docker image - docker build -t mlproject .
3. Run the container - docker run -p 8000:8000 mlproject
4. Open the API documentation - http://localhost:8000/docs
