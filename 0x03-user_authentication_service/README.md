# User Authentication Service with Flask

This project focuses on building a user authentication service using Flask, covering essential concepts such as API route declaration, cookie handling, request form data retrieval, and HTTP status code handling.

## Learning Objectives

1. **Declare API Routes in Flask:**
   - Understand the process of declaring API routes in a Flask application.
   - Utilize route decorators, such as `@app.route()`.

2. **Get and Set Cookies:**
   - Learn how to retrieve and set cookies in the context of user authentication.

3. **Retrieve Request Form Data:**
   - Understand how to retrieve and process form data from HTTP requests.

4. **Return Various HTTP Status Codes:**
   - Gain knowledge on returning appropriate HTTP status codes in Flask responses.

## Requirements

### Editors
- Allowed editors: vi, vim, emacs.

### Environment and Execution
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.

### Coding Style
- Code should adhere to the pycodestyle style (version 2.5).

### Dependency
- Install the bcrypt library using `pip3 install bcrypt`.

### Database
- Use SQLAlchemy 1.3.x for database interactions.

### File Execution
- All files must be executable.

### Code Length
- The length of your files will be tested using the `wc` command.

### Documentation
- All modules, classes, and functions should have meaningful documentation.
- Documentation should be in the form of real sentences, explaining the purpose of the module, class, or method.
- The length of documentation will be verified.

### Type Annotations
- All functions should be type-annotated for clarity.

### Flask Interaction
- Ensure that the Flask app interacts only with Auth and never with the DB directly.
- Use only public methods of Auth and DB outside these classes.

## Setup

1. Install required dependencies:
   ```bash
   pip3 install -r requirements.txt

