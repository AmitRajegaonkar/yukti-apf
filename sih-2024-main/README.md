# SIH 2024 Project - Real-Time Face Recognition Surveillance

This project is a real-time face recognition system designed for surveillance. It integrates with a Directus CMS backend to identify known individuals (criminals) from a database and trigger alerts with location data.

## Prerequisites

- **Python 3.12** is required.
  - Download from [python.org](https://www.python.org/downloads/).
  - **Important:** Check "Add Python to PATH" during installation.
- **Docker Desktop** (for running the Directus backend).

## Installation Setup

1.  update the path of dlib in requirements.txt

2.  **Create a virtual environment**:
    ```bash
    python -m venv myenv312
    ```

3.  **Activate the virtual environment**:
    - Windows:
      ```bash
      .\myenv312\Scripts\activate
      ```
    - Mac/Linux:
      ```bash
      source myenv312/bin/activate
      ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Backend Setup (Directus)

The project uses Directus as a backend database.

1.  Navigate to the `directus` folder:
    ```bash
    cd directus
    ```
2.  Start the Directus server using Docker:
    ```bash
    docker-compose up -d
    ```
3.  Access the admin panel at `http://localhost:8055`.
    - **Email:** `admin@mppolice.gov.in`
    - **Password:** `1234`

if it works then copy the DB file from database_ to directus\database
## Directus Schema Setup

For the application to function, you need to create the following Collections in Directus:

### 1. `criminal_db`
This collection stores the list of suspects to watch for.
- **Primary Key**: `id` (Auto-increment or UUID)
- **Field**: `suspect_aadhaar_no` (Type: String) - The Aadhaar number of the suspect.

### 2. `aadhaar_db`
This collection acts as the central citizen database containing face embeddings.
- **Primary Key**: `aadhaar_no` (Type: String) - Matches `suspect_aadhaar_no`.
- **Field**: `face_embeddings` (Type: JSON) - Stores the vector embedding of the face.
  - *Format*: `{"data": [-0.123, 0.456, ...]}`

### 3. `alert_db`
This collection stores the alerts generated when a face matches.
- **Primary Key**: `id` (Auto-increment or UUID)
- **Field**: `frame` (Type: Image/File) - The captured image of the suspect.
- **Field**: `camera_location` (Type: String) - Location of the camera that detected the face.
- **Field**: `aadhaar_found` (Type: String) - The Aadhaar number of the identified person.

> **Note:** Ensure you give **Public** read/write access (or configure a specific Role) for these collections in **Settings > Roles & Permissions** if you are not using the Admin token.

## Configuration (.env)

Create a `.env` file in the root directory (`sih-2024-main/`) and add the following variables. You can get these values from your Directus admin panel.

```env
# Your Directus User Token (User Profile -> Token)
DIRECT_US_ACCESS_TOKEN=your_access_token_here

# The ID of the folder in Directus where alert images should be uploaded
ALERT_FACES_FOLDER_ID=your_folder_id_here

# Camera Location Mappings (Format: CAMERA_{ID}_LOCATION)
CAMERA_0_LOCATION="Swami Rd, opp. Cooper Hospital, Navpada, JVPD Scheme, Vile Parle, Mumbai"
# CAMERA_1_LOCATION="Another Location..."
```

## Usage

### 1. Main Surveillance System (`project.py`)
This is the main script that runs the camera feed, detects faces, and matches them against the database.

```bash
python project.py
```
- **Functionality**:
    - Captures video from the default camera (ID 0).
    - Detects faces in real-time.
    - Compares detected faces with embeddings in `aadhaar_db`.
    - If a match is found, it uploads the capture to Directus and logs an alert in `alert_db` with the camera's location.
- **Controls**: Press `q` to quit the application.

### 2. Generate Embeddings (`get_embeddings.py`)
A utility script to generate face embeddings from an image file.

```bash
python get_embeddings.py
```
- Opens a file dialog to select an image.
- Generates a face embedding vector.
- Saves the embedding to `user.json` (useful for manually updating the database).

## Project Structure

- **`project.py`**: Main application logic (Multiprocessing for capture, detection, and API communication).
- **`get_embeddings.py`**: Tool to extract face embeddings from images.
- **`directus/`**: Contains `docker-compose.yml` for the backend.
- **`requirements.txt`**: Python dependencies.
- **`.env`**: Configuration file for secrets and settings.