# Predict Equipment Failure Risk Application for Factory Equipment - mlops

## Project Overview

This repository contains all the resources and source code for our Predict Equipment Failure Risk Application designed to optimize maintenance activities in a factory setting. This application leverages historical maintenance data and will eventually integrate real-time IoT sensor data to predict potential equipment failures. The goal is to reduce downtime and maintenance costs while improving the longevity and reliability of factory equipment.

### Key Features
- **Real-Time Data Dashboard**: Visualizes the health status of equipment.
- **Predictive Alerts System**: Sends notifications for upcoming maintenance needs.
- **Historical Data Analysis Interface**: Allows for deep dives into historical maintenance data.
- **Maintenance Scheduling Tool**: Assists in planning and optimizing maintenance operations.
- **Performance Monitoring**: Monitors the health and accuracy of deployed models.
- **User Management and Security**: Ensures data security through role-based access controls.

## Project Structure

```plaintext
/
├── data/                   # Dataset and data preparation scripts
├── docs/                   # Project documentation and references
├── models/                 # Machine learning models and training scripts
├── notebooks/              # Jupyter notebooks for exploration and analysis
├── src/                    # Source code for the predictive maintenance application
│   ├── api/                # API for handling requests
│   ├── app/                # Backend logic of the application
│   └── ui/                 # Frontend user interface components
├── tests/                  # Automated tests for the application and data processing
└── README.md               # Project overview and setup instructions

```

## Architecture

The application is structured into three main components:

1. **Data Layer**: Manages all data-related processes, from ingestion and storage to preprocessing. It uses a robust database system to handle both batch and real-time data efficiently.

2. **Application Layer**: Hosts the core logic of the application, including the predictive models, data analysis tools, and maintenance scheduling functionalities. It integrates with the Data Layer to fetch predictive insights and operational data.

3. **Presentation Layer**: Provides a user interface for interacting with the system, visualizing data, and receiving alerts. It is designed to be intuitive and accessible to all stakeholders.

## Getting Started

### Prerequisites
- Python 3.8+
- Docker (for containerization)
- PostgreSQL or another chosen database system
- Node.js (if developing custom UI components)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eetinosa/predictive-maintenance-mlops.git
   cd predictive-maintenance-mlops
   ```
2.  **Set up the environment:**
    ```bash
    # Create a virtual environment
    python -m venv predict_app
    # Activate the environment
    source predict_app/bin/activate
    # Install dependencies
    pip install -r requirements.txt
    ```
3. **Database setup:**
    ```bash
    # Initialize the database schema
    python src/db_initialize.py
     ```

4. **Run the application:**
    ```bash
    python src/app.py
    ```

5.  **Visit the application: Open your web browser and go to http://localhost:5000 to view the application.**
