🚀 Azure DevOps CI/CD Machine Learning API



📌 Project Overview



This project demonstrates a complete DevOps workflow for deploying a Machine Learning prediction API using:



Azure Cloud Shell



GitHub Actions (CI)



Azure Pipelines (CD)



Azure App Service



Azure CLI



Python (Flask)



Makefile automation



The application exposes a REST API endpoint that returns a JSON-based prediction.



🏗 Architecture Diagram

4

Workflow



Developer pushes code to GitHub



GitHub Actions runs lint + tests (CI)



Azure Pipelines builds and deploys (CD)



Azure App Service hosts the Flask ML API



User sends POST request → receives JSON prediction



🔁 Continuous Integration

Azure Cloud Shell

git clone https://github.com/YOUR-USERNAME/YOUR-REPO

cd YOUR-REPO

make all





This runs:



Dependency install



Linting



Unit tests



GitHub Actions



Workflow file:



.github/workflows/main.yml





Runs automatically on push to main.



🚀 Continuous Delivery



Deployment handled by:



azure-pipelines.yml





Azure Pipeline:



Installs dependencies



Runs tests



Deploys to Azure App Service



🧪 Testing the Live App



After deployment:



./make\_prediction.sh https://your-app-name.azurewebsites.net





Example Output:



{

&nbsp; "prediction": 3.9

}



📊 Project Management

🔗 Trello Board



https://trello.com/b/YOUR-BOARD-ID



🔗 Project Plan Spreadsheet



https://docs.google.com/spreadsheets/d/YOUR-SHEET-ID



Includes:



Quarterly plan



Weekly deliverables



Task estimations



🎥 Screencast Demo



YouTube Demo:

[https://youtube.com/YOUR-VIDEO-LINK](https://www.youtube.com/watch?v=YmLPBLMCxRQ&t=811s)


