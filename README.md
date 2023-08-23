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
