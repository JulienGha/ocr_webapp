Optical Character Recognition API

In your terminal goes to the folder where you want to deploy the project.

Run in the terminal:
- git clone https://github.com/JulienGha/ocr_webapp.git if you have access, otherwise unzip the folder.
- cd ocr_webapp

Run the OCR API:
- Make sure that DOcker is installed and can run.
- Check if there is an app running on port 5000 (lsof -i :5000)
- docker-compose up --build

Run the front:
- Go to the front directory.
- Open your IDE.
- Verify that Node is installed by executing the command "node -v" in the terminal.
- If Node is not installed, install it.
- In the terminal, run the command "npm install".
- Still in the terminal, execute the command "npm start".
- Once the React starts, choose a tiff or png who weights less than 3MB.

The application comprises three main components: the server, the user interface (UI), and the Optical Character Recognition (OCR) system.
- Server & OCR Initialization: Both the server and the OCR are set up using Docker, ensuring a consistent and reproducible environment for deployment.
- User Interface:
  - The front-end of the application is built using React. I opted for React because of its ease of use, especially for building user interfaces and adding functionalities.
  - My previous work experiences with React, particularly in Web 3.0 technologies, have made me comfortable with tasks such as image upload.
  - The front-end is initialized using Node.js, providing the necessary environment to run and test the React application.
- OCR System:
  - For the OCR functionality, we leverage Tesseract, as proposed in the challenge.
  - We encountered an issue where Tesseract was unexpectedly shutting down. To address this, we added the line CMD ["tail", "-f", "/dev/null"] to its Dockerfile, ensuring that it remains running.
- Server: The server component is divided into three parts:
  - server.py: This script sets up the server, listens for incoming requests, and delegates tasks as necessary.
  - tasks.py: This script handles image processing. It receives an image, verify its compatibility and then sends it to Tesseract for OCR.
  - worker.py: This script sets up a system to queue jobs and process them in the background using workers. This ensures that the server can continue to handle incoming requests even if the image processing takes time.
