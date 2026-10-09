-Requirements:
    Python 3.8+
    pip

-Installation on windows:
create a venv in the project folder:
    python -m venv venv
activate venv:
    venv\Scripts\Activate.ps1

-Install requirements.txt
    pip install -r requirements.txt

-Launch server:
    python -m uvicorn main:app --reload
-Shut down:
    Ctrl + C