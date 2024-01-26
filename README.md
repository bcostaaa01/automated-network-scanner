# 🚀 Network Speed Test API

This is a FastAPI application that measures network speed and provides the results via an API.

## 📚 API Documentation

The API has the following endpoints:

- `GET /speed`: Returns an XML file with the current network speed.
- `GET /speed_log`: Returns the current network speed log.

## 🛠️ Installation & Set Up

1. Clone the repository

```bash
git clone https://github.com/bcostaaa01/network-speed-test-api.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

You can run the application using the following command:

```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

## 📝 API Usage

### Get Network Speed

To get the current network speed, send a GET request to `/speed`. This will return an XML file with the current network speed.

```bash
curl http://localhost:8000/speed
```

### Get Network Speed Log

To get the current network speed log, send a GET request to `/speed_log`. This will return the current network speed log.

```bash
curl http://localhost:8000/speed_log
```

## 📚 API Documentation

You can view the API documentation at `http://localhost:8000/docs` when the application is running.

## 📝 License

This project is licensed under the terms of the MIT license.
```

This README provides a brief description of the project, instructions for installing and running the application, and examples of how to use the API. It also includes a link to the API documentation and information about the project's license.