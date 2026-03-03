Detta projekt är en fullstack-labb för att prediktera taxipriser med hjälp av datasetet taxi_trip_pricing.csv. 

Task 0 
Skapade repo, mappstruktur, uv init, venv, installerade paket. Det var jobbigt med venv i Git Bash, fick skriva source .venv/Scripts/activate massa gånger för att det skulle funka.

Task 1   
Laddade CSV, kollade info och describe, plottade grejer med seaborn. Rensade NaN och duplicates, sparade clean fil. Hade massa fel med path till CSV, fick ändra flera gånger.

Task 2   
Laddade datan, delade upp i features och Trip_Price. Definierade numeric_features och categorical_features. Gjorde ColumnTransformer med StandardScaler och OneHotEncoder. Splitade data med train_test_split (test_size=0.2). Skapade två pipelines: en med LinearRegression och en med RandomForestRegressor. Tränade båda och jämförde MSE och R². RandomForest var bäst. Sparade den modellen som taxi_price_model.pkl med joblib

Task 3 - API  
Gjorde FastAPI med GET för data och POST för prediktion. Massor av problem med import (taxipred.backend osv), venv som inte aktiverades, path till CSV som inte hittades (FileNotFoundError). Fick byta från relativa paths till hårdkodade ett tag. Nu funkar det i Swagger, får data på /taxi/ och pris på /predict.

Task 4 - Frontend  
Streamlit dashboard med tabell från API och formulär för prediktion. Först krånglade httpx (ModuleNotFoundError), sen ConnectError för att backend inte var igång. Tog evigheter att ladda tabell för att det var för många rader, så begränsade till head(10). Priserna kom ut låga (typ 17 kr för lång resa) för att datan verkar vara i dollar, inte kronor. Nu visar jag USD istället.


## Screenshots
![Swagger](screenshots/swagger.png)  
![Data från /taxi/](screenshots/get-taxi.png)  
![Prediktion](screenshots/predict.png)  
![Streamlit](screenshots/streamlit.png)

## Video
https://youtu.be/XXXXXXXX (ladda upp sen)

Klar med labben nu, var jobbigt men kul tillslut!