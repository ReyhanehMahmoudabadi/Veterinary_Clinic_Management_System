# 🐾 Veterinary Clinic Management System

A desktop-based Veterinary Clinic Management System developed using Python and Object-Oriented Programming (OOP). The application provides a graphical interface for managing pet owners, veterinarians, pets, and veterinary visits.

---

## 📌 Table of Contents

- [Introduction](#-introduction)
- [Important Notice](#️-important-notice)
- [Features](#-features)
- [Technologies](#️-technologies)
- [Project Architecture](#️-project-architecture)
- [Installation](#️-installation)
- [How to Run](#️-how-to-run)
- [Project Structure](#-project-structure)
- [Validation Rules](#-validation-rules)
- [Data Storage](#-data-storage)
- [Testing](#-testing)
- [License](#-license)

---

## 📖 Introduction

The Veterinary Clinic Management System is designed to organize and manage essential veterinary clinic information.

The application provides four main management sections:

- **Owners:** Stores pet owner information.
- **Vets:** Stores veterinarian information.
- **Pets:** Manages pet information and owner relationships.
- **Visits:** Manages veterinary appointments and their related information.

The project is developed using an object-oriented approach and a layered architecture to keep the code organized, reusable, and maintainable.

---

## ⚠️ Important Notice

**PLEASE READ THIS SECTION CAREFULLY BEFORE USING THE APPLICATION.**

This application implements specific business rules and data dependencies. To ensure successful registration and prevent validation errors, users must follow the required data entry order.

### Required Form Submission Order

**1. Owners**

Register pet owners first.

- Each Owner ID must be unique.
- Owner information must be registered before adding pets.

**2. Vets**

Register veterinarians.

- Each Vet ID must be unique.
- Vets can be registered independently of Owners.

**3. Pets**

Register pets after their owners have been registered.

- Each Pet ID must be unique.
- The entered Owner ID must belong to an existing owner.
- The application rejects pets associated with non-existing owners.

**4. Visits**

Register visits after the required pets and veterinarians have been registered.

- Each Visit ID must be unique.
- The entered Pet ID must belong to an existing pet.
- The entered Vet ID must belong to an existing veterinarian.
- The application rejects visits referencing non-existing pets or veterinarians.

### Recommended Workflow

`Owners → Vets → Pets → Visits`

**Important:** Following this order is essential because the application checks relationships between records before saving dependent information.

---

## ✨ Features

- Register and manage pet owners.
- Register and manage veterinarians.
- Register and manage pets.
- Schedule and manage veterinary visits.
- Validate user input through dedicated validation methods.
- Prevent duplicate record IDs.
- Verify relationships between owners, pets, and veterinarians.
- Display registered records in table views.
- Support optional fields such as email, microchip number, diagnosis, and treatment.
- Save and retrieve application data using file-based storage.

---

## 🛠️ Technologies

- **Python** – Main programming language.
- **Tkinter** – Graphical User Interface.
- **Object-Oriented Programming (OOP)** – Application design.
- **Pickle** – Object serialization and data persistence.
- **Regular Expressions (Regex)** – Input validation.
- **PyCharm** – Development environment.
- **Git & GitHub** – Version control.

---

## 🏗️ Project Architecture

The application follows a layered architecture:

| Layer          | Responsibility                                            |
| -------------- | --------------------------------------------------------- |
| Model          | Defines data classes and their attributes.                |
| Data Access    | Handles saving and retrieving records.                    |
| Business Logic | Implements business rules and data relationship checks.   |
| Controller     | Connects the GUI with the business logic layer.           |
| View           | Provides the graphical user interface.                    |
| Tools          | Contains shared validation methods.                       |
| Test           | Contains tests for application classes and functionality. |

---

### Architecture Overview

The project follows a layered architecture based on Object-Oriented Programming (OOP), with each layer responsible for a specific part of the application.

The **View** layer provides the graphical interface, while the **Controller** layer manages communication between the interface and the application's core logic. The **Business Logic** layer handles application rules, validations, and relationships between records. The **Data Access** layer manages data storage and retrieval, while the **Model** layer defines the application's main entities and their attributes.

The **Tools** layer provides reusable validation methods, and the **Test** layer contains test modules for verifying application functionality.

This separation of responsibilities makes the application more organized, maintainable, and easier to extend.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ReyhanehMahmoudabadi/Veterinary_Clinic_Management_System.git
```

### 2. Open the Project

Open the downloaded project folder in PyCharm or another Python IDE.

### 3. Configure Python

Make sure Python is installed and configured in your IDE.

No additional third-party packages are required. The project uses Python's built-in modules.

---

## ▶️ How to Run

Run the application from the project root directory using:

```bash
python main.py
```

The main window will appear, providing access to four sections:

- Owners
- Pets
- Vets
- Visits

**Reminder:** Read the Important Notice section and follow the required form submission order before entering records.

---

## 📂 Project Structure

```text
Veterinary_Clinic_Management_System/
│
├── business_logic/
│   ├── __init__.py
│   ├── owner_bl.py
│   ├── pet_bl.py
│   ├── vet_bl.py
│   └── visit_bl.py
│
├── controller/
│   ├── __init__.py
│   ├── owner_controller.py
│   ├── pet_controller.py
│   ├── vet_controller.py
│   └── visit_controller.py
│
├── data_access/
│   ├── __init__.py
│   ├── owner_da.py
│   ├── pet_da.py
│   ├── vet_da.py
│   ├── visit_da.py
│   │
│   └── data/
│       ├── owner.dat
│       ├── pet.dat
│       ├── vet.dat
│       └── visit.dat
│
├── model/
│   ├── __init__.py
│   ├── person.py
│   ├── owner.py
│   ├── pet.py
│   ├── vet.py
│   └── visit.py
│
├── test/
│   ├── __init__.py
│   ├── person_test.py
│   ├── owner_test.py
│   ├── pet_test.py
│   ├── vet_test.py
│   └── visit_test.py
│
├── tools/
│   ├── __init__.py
│   └── validation.py
│
├── view/
│   ├── __init__.py
│   ├── owner_view.py
│   ├── panel_view.py
│   ├── pet_view.py
│   ├── vet_view.py
│   └── visit_view.py
│
├── main.py
│
└── README.md
```

---

## 🔍 Validation Rules

The application uses a centralized `Validator` class located in `tools/validation.py`.

Some of the implemented validation rules include:

- **Names:** Must contain valid English letters and follow the defined length limits.
- **National ID:** Must contain exactly 10 digits.
- **Phone Number:** Must follow the defined mobile phone number format.
- **Email:** Must follow a valid email address format. This field is optional.
- **Owner ID / Vet ID:** Must be positive integers.
- **Pet ID:** Must contain 1–10 English letters or digits.
- **Gender:** Must be `Male`, `Female`, or `Unknown`.
- **Birth Date:** Must be a valid date and cannot be in the future.
- **Weight:** Must be a positive number.
- **Microchip Number:** Must contain exactly 15 digits when provided.
- **Visit ID:** Must follow the `VIS-` prefix format, followed by digits.
- **Visit Date:** Must be a valid datetime and cannot be in the past.
- **Visit Status:** Must be one of the following values:
  - `Scheduled`
  - `Completed`
  - `Cancelled`
  - `Rescheduled`

Additional validation rules are implemented for addresses, specialization, license numbers, species, breed, reason, diagnosis, and treatment.

---

## 💾 Data Storage

The application uses Python's `pickle` module to store and retrieve objects.

Data is saved in separate binary files inside:

```text
data_access/data/
```

| File        | Stored Information   |
| ----------- | -------------------- |
| `owner.dat` | Owner records        |
| `vet.dat`   | Veterinarian records |
| `pet.dat`   | Pet records          |
| `visit.dat` | Visit records        |

The records are loaded when the application accesses the corresponding data management sections.

**Note:** Keep the `.dat` files in their original directory to preserve access to previously saved records.

---

## 🧪 Testing

The `test/` directory contains individual test modules for the application's classes and functionality.

Available test files:

- `person_test.py`
- `owner_test.py`
- `pet_test.py`
- `vet_test.py`
- `visit_test.py`

These modules can be executed separately to test different parts of the application.

---

## 📄 License

No license has been specified for this project.

---

Developed with ❤️ using Python.
