---
title: Meat Freshness
emoji: 🥩
colorFrom: red
colorTo: pink
sdk: docker
pinned: false
---
Meat Freshness Detection
========================

A **FastAPI application** designed to detect meat freshness using a pre-trained **Keras .h5 model**. This project is deployed efficiently via **Docker on Hugging Face Spaces**, providing an accessible and scalable solution for freshness prediction.

Overview
--------

This application leverages a Convolutional Neural Network (CNN) model (presumably "pi-cnn-model" based on your Hugging Face Space) to analyze images of meat and determine its freshness status. The backend is powered by FastAPI, offering a robust and performant API for predictions.

Deployment
----------

The application is containerized with Docker, ensuring consistent environments and easy deployment. It's hosted on Hugging Face Spaces, making it publicly available and easy to interact with. You can access the running space at [https://huggingface.co/spaces/bxntang/pi-cnn-model.](https://huggingface.co/docs/hub/spaces-config-reference)

How to Use
----------

To get a freshness prediction, send an **image file** via a **POST request** to the /predict endpoint of the deployed application. The API will process the image and return the predicted freshness status.

**Example using curl:**

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   curl -X POST -H "Content-Type: multipart/form-data" \    -F "file=@/path/to/your/image.jpg" \    https://bxntang-pi-cnn-model.hf.space/predict   `

**Note:** Replace /path/to/your/image.jpg with the actual path to the image file you want to analyze.

Project Structure
-----------------

While the full file structure is not shown here, key components for deployment and functionality include:

*   .gitattributes
    
*   .gitignore
    
*   Dockerfile: Defines the Docker image for the application.
    
*   README.md: This documentation file.
    
*   aerich.ini (Potentially for database migrations if a database is used)
    
*   pyproject.toml (For project dependencies and metadata)
    
*   requirements.txt: Lists Python dependencies required by the FastAPI application.
    
*   The Keras .h5 model file (e.g., model.h5 or similar, which is loaded by the FastAPI app).
    

Contribution
------------

For information on contributing to this project or understanding the backend code, please refer to the project's files on Hugging Face Spaces.

Configuration Reference
-----------------------

For more details on configuring Hugging Face Spaces, you can check out the official documentation:

*   [Hugging Face Spaces Configuration Reference](https://huggingface.co/docs/hub/spaces-config-reference)