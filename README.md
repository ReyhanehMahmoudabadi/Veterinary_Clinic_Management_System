# 🐾 Veterinary Clinic Management System

A desktop application for managing veterinary clinic records, developed with Python, Tkinter, and object-oriented programming (OOP). The system provides separate interfaces for managing pet owners, veterinarians, pets, and veterinary visits.

## 📌 Table of Contents

- [Overview](#overview)
- [Important: Read Before Using](#important-read-before-using)
- [Features](#features)
- [Technologies](#technologies)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Validation Rules](#validation-rules)
- [Data Storage](#data-storage)
- [Tests](#tests)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

## 📖 Overview

The Veterinary Clinic Management System is designed to organize the main records of a veterinary clinic. It manages pet owners and veterinarians, stores pet information linked to registered owners, and records veterinary visits associated with existing pets and veterinarians. The application is organized into separate layers for models, data access, business logic, controllers, and views.

## ⚠️ Important: Read Before Using

> **Important:** Follow the data-entry order below. The application checks whether related records already exist before saving a pet or a visit. If a required record has not been registered, the save operation will be rejected.

### Required data-entry order

1. **Owners** — Register the owner first. Each `Owner ID` must be unique.
2. **Vets** — Register veterinarians. Each `Vet ID` must be unique. Owners and veterinarians can be registered independently, so either of these first two steps may come first.
3. **Pets** — Register a pet only after its owner exists. The entered `Owner ID` must match an existing owner, and each `Pet ID` must be unique.
4. **Visits** — Register a visit only after its pet and veterinarian exist. The entered `Pet ID` and `Vet ID` must match existing records, and each `Visit ID` must be unique.

**Recommended workflow:** `Owners → Vets → Pets → Visits`

The essential dependencies are:

- A pet requires an existing owner.
- A visit requires an existing pet and an existing veterinarian.
- Owners and veterinarians do not depend on each other.

## ✨ Features

- Register and view owner records.
- Register and view veterinarian records.
- Register and view pet records linked to existing owners.
- Register and view veterinary visits linked to existing pets and veterinarians.
- Validate input data before saving records.
- Prevent duplicate Owner IDs, Vet IDs, Pet IDs, and Visit IDs.
- Persist records between application runs using local data files.
- Display records through Tkinter table views.

## 🛠️ Technologies

- **Python** — application logic and data models.
- **Tkinter / ttk** — desktop graphical user interface.
- **Pickle** — serialization of Python objects for local file storage.
- **Regular expressions (`re`)** — format validation.
- **Git and GitHub** — version control and source-code hosting.

PyCharm was used as the development environment. It is not required to run the application.

## 🏗️ Architecture

The project uses a layered structure:

| Layer | Responsibility |
|---|---|
| `model` | Defines the `Person`, `Owner`, `Vet`, `Pet`, and `Visit` classes. |
| `data_access` | Loads and saves records in local `.dat` files. |
| `business_logic` | Applies business rules, checks duplicate IDs, and verifies record relationships. |
| `controller` | Connects the views to the business-logic layer. |
| `view` | Implements the Tkinter windows and user interface. |
| `tools` | Contains shared input-validation methods. |
| `test` | Contains test scripts for the model and business-logic functionality. |


## 🚀 Getting Started

### Requirements

- Python 3
- Tkinter (usually included with standard Python installations; on some Linux distributions it may need to be installed separately)
- The project files and the `data_access/data/` directory

The application uses Python standard-library modules and does not currently require a third-party package installation.

### Download the project

Clone the repository:

```bash
git clone https://github.com/ReyhanehMahmoudabadi/Veterinary_Clinic_Management_System.git
```

Alternatively, download the repository as a ZIP file and extract it.

## ▶️ Running the Application

Open a terminal in the project root directory (the directory containing `main.py`) and run:

```bash
python main.py
```

The main window provides access to the Owners, Pets, Vets, and Visits sections. Before entering records, read the [Important: Read Before Using](#important-read-before-using) section and follow the required data-entry order.

## 📂 Project Structure

The project is organized into the following main directories and files:

- `business_logic/` — business rules and operations.
- `controller/` — connects the interface to the business logic.
- `data_access/` — data access modules and the `data/` folder for local records.
- `model/` — application classes and data models.
- `test/` — test scripts.
- `tools/` — shared validation utilities.
- `view/` — Tkinter interface windows.
- `main.py` — application entry point.
- `README.md` — project documentation.

## 🔍 Validation Rules

Input validation is centralized in `tools/validation.py` in the `Validator` class. The implemented rules include:

| Field | Validation rule |
|---|---|
| Name | 2–30 English letters. |
| Family name | 2–50 English letters. |
| National ID | Exactly 10 digits. |
| Phone number | 10 or 11 digits, matching the configured mobile-number pattern. |
| Email | Optional; if provided, must match the configured email format. |
| Owner ID | Positive integer. |
| Address | 2–300 characters; supports English/Persian letters, digits, spaces, and selected punctuation. |
| Vet ID | Positive integer. |
| Specialization | 2–100 English letters and spaces. |
| License number | 4–20 digits. |
| Pet ID | 1–10 English letters or digits. |
| Pet name | 1–30 English letters, spaces, or hyphens. |
| Species and breed | 1–50 English letters and spaces. |
| Gender | `Male`, `Female`, or `Unknown` (case-insensitive). |
| Birth date | A valid `date` value that is not in the future. |
| Weight | Positive integer or floating-point number. |
| Microchip number | Optional; if provided, exactly 15 digits. |
| Visit ID | `VIS-` followed by one or more digits. |
| Visit date | A `datetime` value that is not earlier than the current date and time. |
| Reason | 1–60 characters matching the configured English/Persian text and punctuation pattern. |
| Status | `Scheduled`, `Completed`, `Cancelled`, or `Rescheduled` (case-insensitive). |
| Diagnosis | 1–255 characters matching the configured letters, digits, spaces, and punctuation pattern. |
| Treatment | 1–255 characters matching the configured letters, digits, spaces, and punctuation pattern. |

In addition to field validation, the business-logic layer checks that record IDs are unique and that referenced owners, pets, and veterinarians exist before saving dependent records.

## 💾 Data Storage

The application uses Python's `pickle` module to serialize records into separate files in `data_access/data/`:

| File | Contents |
|---|---|
| `owner.dat` | Owner records |
| `vet.dat` | Veterinarian records |
| `pet.dat` | Pet records |
| `visit.dat` | Visit records |

Run the application from the project root so the relative data-file paths resolve correctly. Keep the `data_access/data/` directory in place. Back up these files before making changes to the project or its data.

> **Security note:** Pickle files must only be loaded from trusted sources. Loading an untrusted or modified pickle file can execute malicious code. Do not open `.dat` files received from unknown sources.

## 🧪 Tests

The `test/` directory contains the following test scripts:

- `person_test.py`
- `owner_test.py`
- `pet_test.py`
- `vet_test.py`
- `visit_test.py`

Run an individual test script from the project root, for example:

```bash
python -m test.owner_test
```

Replace `owner_test` with the desired test module name to run another test. These are standalone test scripts; the project does not currently include a configured automated test runner or coverage report.

## ⚠️ Known Limitations

- The current data layer uses local Pickle files rather than a database system.
- The current business-logic layer provides record creation and retrieval; update and delete operations are not implemented in these modules.
- The application is designed as a local desktop application and does not provide multi-user or network synchronization.
- Data files should be backed up manually.

## 🔮 Future Improvements

Potential enhancements for future versions include:

- Add update and delete operations for records.
- Add search and filtering functionality.
- Introduce SQLite or another database system.
- Add automated unit tests and test coverage reporting.
- Implement data backup and recovery features.
- Add report generation and CSV/PDF export.
- Improve error logging and exception handling.

## 👩‍💻 Author

**Reyhaneh Mahmoudabadi**

GitHub: [@ReyhanehMahmoudabadi](https://github.com/ReyhanehMahmoudabadi)

## 📄 License

No license has been specified for this repository. Unless a license is added, the project is not explicitly released for reuse, modification, or redistribution under an open-source license.

---

Developed with ❤️ using Python.
