Optical Character Recognition API

In your terminal goes to the folder where you want to deploy the project.

Run in the terminal:
- git clone https://github.com/JulienGha/ocr_webapp.git if you have access, otherwise unzip the folder.
- cd ocr_webapp in terminal

Run the OCR API & Server:
- Make sure that Docker is installed and can run.
- Check if there is an app running on port 5000 (lsof -i :5000)
- docker-compose up --build in terminal

Run the front:
- Go to the front directory.
- Open your IDE.
- Verify that Node is installed by executing the command "node -v" in the terminal.
- If Node is not installed, install it.
- In the terminal, run the command "npm install".
- Still in the terminal, execute the command "npm start".
- Once the React starts, choose a tif or png who weights less than 3MB.

The application is composed by two main components: the server and the user interface (front).
- Server & OCR Initialization: Both the server and the OCR are initialize using Docker, ensuring a reproducible environment for deployment.
- The server is divided into three parts:
  - server.py: This script sets up the server, listens for incoming requests, and delegates tasks as necessary.
  - tasks.py: This script handles image processing by giving the function to the workers.
  - worker.py: This script sets up a system to queue jobs and process them in the background using workers. This ensures that the server can continue to handle incoming requests even if the image processing takes time. We installed tesseract directly on the workers (when building them with their Dockerfile) to ensure an easier use.
- User Interface:
  - The front-end of the application is built using React. I opted for React because of its ease of use, especially for building user interfaces and adding functionalities.
  - My previous work experiences with React, particularly in Web 3.0 technologies, have made me comfortable with tasks such as image upload.
  - The front-end is initialized using Node.js, providing the necessary environment to run and test the React application.
