## ChatGPT Recommendation Tool with Embeddings using MongoDB
ChatGPT Recommendation Tool API with Flask with MongoDB Integration: Enhance recommendations using ChatGPT and MongoDB for applications and running it as a Flask API.

ChatGPT Recommendation Tool with Embeddings MongoDB Integration

The ChatGPT Recommendation Tool with Embeddings MongoDB Integration is a powerful open-source tool designed to enhance the recommendation capabilities. By leveraging the advanced language model ChatGPT and integrating it with the popular NoSQL database MongoDB, this tool provides developers with a robust solution for building recommendation systems within their applications.

Key Features:

1. ChatGPT Integration: The tool seamlessly incorporates the state-of-the-art language model ChatGPT, enabling it to understand and generate human-like text responses.
2. Recommendation Engine: The tool includes a recommendation engine that utilizes the embeddings technique, which represents textual data in a continuous vector space. 3. MongoDB Integration: This tool integrates with MongoDB, a highly scalable NoSQL database known for its flexibility and performance. By storing and retrieving relevant data in MongoDB, developers can efficiently manage large amounts of user interaction data, historical information, and item embeddings for effective recommendation generation.
4. Scalability and Performance: The MongoDB integration ensures scalability and high-performance capabilities, enabling the tool to handle large datasets and user interactions efficiently. This ensures a smooth user experience even when dealing with vast amounts of data.

# Tutorial: Running ChatGPT Recommendation Tool with MongoDB Integration on Port 80 using Flask

In this tutorial, we will guide you through the steps to run the ChatGPT Recommendation Tool with MongoDB Integration as a Flask application on port 80. We will be using Docker to containerize the application for easy deployment.

Step 1: Fill in .env file
Open the .env file and add the following variables

```
MONGO_CONNECTION_STRING=
OPENAI_API_KEY=
```

Step 2: Build the Docker image
Open your terminal and navigate to the project directory where the Dockerfile is located. Run the following command to build the Docker image:

```
docker build -t chatgpt-recommendation .
```

This command will build the Docker image named "chatgpt-recommendation" based on the instructions defined in the Dockerfile.

Step 3: Run the Docker container
After successfully building the Docker image, you can run the container using the following command:

```
docker run -p 80:80 chatgpt-recommendation
```

This command will start the Docker container and map port 80 of the host machine to port 80 of the container. Adjust the port mapping as per your requirements.

Step 3: Access the application
Once the Docker container is running, you can access the ChatGPT Recommendation Tool with MongoDB Integration by opening a web browser and navigating to `http://localhost:80`. If you're running Docker on a remote machine, replace "localhost" with the IP address or hostname of the machine where the container is running.

Congratulations! You have successfully set up and deployed the ChatGPT Recommendation Tool with MongoDB Integration as a Flask application running on port 80 using Docker.

Note: Make sure you have the necessary code files (`app.py`, `templates`, etc.) in the same directory as your Dockerfile for the application to run correctly. Additionally, ensure that any required environment variables, configuration files, or database connection details are appropriately set within your Flask application.
