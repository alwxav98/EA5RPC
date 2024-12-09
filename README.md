# RPC project in Python

This project implements a basic RPC (Remote Procedure Call) server in Python using Flask and Flask-JSON-RPC. The server exposes several methods that can be called remotely over HTTP using JSON-RPC protocol.

## Instructions to run the project
### Prerequisites
1. Make sure you have Docker installed on your machine.
2. Clone this repository to your local machine:

   ```bash
   git clone  https://github.com/alwxav98/EA5RPC.git
   cd  EA5RPC
   ```

### Using Docker
1. Clone this repository to your local machine.
2. Build the Docker image with the following command:

   ```bash
   docker build -t python-rpc .
   ```

3. Run the container with:

   ```bash
   docker run -d -p 5000:5000 --name rpc-container python-rpc
   ```
4. Access the application in your browser:
- Home page: http://localhost:5000
- API endpoint: http://localhost:5000/api

## Testing the Webhoop Endpoint
The RPC accepts POST requests and cannot be accessed directly from the browser. You can test it using tools like Postman or cURL. Here's an example:

### Using Postman
1. Open Postman and create a new request.
2. Set the method to POST.
3. Enter the URL: http://localhost:5000/api.
4. In the Postman Headers section, add the following header:
  - Key: Content-Type
  - Value: application/json
5. Go to the Body tab, select raw, and choose JSON as the format.
6. Enter the following sample JSON:

   ```json
      {
        "jsonrpc": "2.0",
        "method": "App.hello_world",
        "params": [],
        "id": 1
      }
      ```
7. Submit the request
   Click Send to submit the request.
   
   This should return:
   
   ```json
      {
          "id": 1,
          "jsonrpc": "2.0",
          "result": "Hola, mundo desde RPC"
      }
      ```
   
