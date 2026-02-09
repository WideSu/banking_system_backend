# In-Memory Banking System

![Build Status](https://img.shields.io/github/actions/workflow/status/WideSu/banking_system_backend/python-ci.yml?branch=main)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

A high-performance, in-memory banking system backend built with **Python** and **FastAPI**. Designed for demonstration, it showcases best practices in concurrent programming (Asyncio), RESTful API design, and containerization (Docker).

## Features

- ** High Performance**: Pure in-memory operations with **O(1)** lookup times.
- ** Concurrency Safe**: Uses Python's `asyncio` single-threaded event loop to handle concurrent requests safely without locks.
- ** Docker Ready**: Containerized for easy deployment to any cloud platform (Render, AWS, GCP).
- ** Robust Error Handling**: Custom exceptions for domain-specific errors (Insufficient Funds, Account Not Found, etc.).
- ** Comprehensive Testing**: 100% test coverage with **PyTest** and **GitHub Actions** CI/CD.

## Architecture

The system follows a clean architecture separating the domain model from the API layer.

```mermaid
graph TD
    subgraph Python_Banking_System["Python Banking System"]
        A[Bank] -->|manages| B[Account]
        B -->|records| C[Transactions]
    end

    subgraph Core_Operations["Core Operations"]
        B --> D[Account Operations]
        D --> D1[Deposit]
        D --> D2[Withdraw]
        D --> D3[Transfer]
        D --> D4[Get Balance]
        C --> E[Transaction Record]
    end

    subgraph Error_Handling["Error Handling"]
        F[Custom Exceptions]
        F --> F1[InsufficientFundsError]
        F --> F2[AccountNotFoundError]
        F --> F3[NegativeAmountError]
    end

    %% Styling
    style A fill:#1565C0,stroke:#0D47A1,color:#ffffff
    style B fill:#00897B,stroke:#00695C,color:#ffffff
    style C fill:#6A1B9A,stroke:#4A148C,color:#ffffff
    style D fill:#D32F2F,stroke:#B71C1C,color:#ffffff
    style F fill:#FF8F00,stroke:#E65100,color:#000000
    
    class Python_Banking_System,Core_Operations,Error_Handling fill:#f5f5f5,stroke:#bdbdbd,stroke-width:2px
```

## Tech Stack

- **Language**: Python 3.9+
- **Framework**: FastAPI
- **Concurrency**: Asyncio
- **Containerization**: Docker & Docker Compose
- **Testing**: PyTest, HTTPX
- **CI/CD**: GitHub Actions

---

## Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional, for containerized execution)

### 1. Clone the repository

```bash
git clone https://github.com/WideSu/banking_system_backend.git
cd banking_system_backend
```

### 2. Run with Docker (Recommended)

The easiest way to run the application is using Docker Compose.

```bash
docker-compose up --build
```

The API Docs will be available at:
- **Interactive Docs**: https://banking-system-backend-klt3.onrender.com/docs

### 3. Run Locally (Manual)

Set up a virtual environment and install dependencies.

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m banking.main
```

## Testing

We maintain **100% code coverage**. You can run the test suite using PyTest.

```bash
# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=banking --cov-report=term-missing
```

## Project Structure

```
banking_system_backend/
├── banking/              # Core Application Code
│   ├── models.py         # Domain Logic (Bank, Account)
│   ├── main.py           # FastAPI Application & Routes
│   └── errors.py         # Custom Exception Classes
├── tests/                # Test Suite
│   ├── performance/      # Load & Stress Tests
│   ├── test_main.py      # API Integration Tests
│   └── test_models.py    # Unit Tests
├── docs/                 # Documentation
├── Dockerfile            # Docker Configuration
├── docker-compose.yml    # Docker Compose Configuration
└── requirements.txt      # Project Dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
