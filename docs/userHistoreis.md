# ActionHub - UserHistories

## 1. User Stories
- As a user, I want to register an account so that I can securely access my tasks.
- As a user, I want to log in with my credentials so that I can manage my personal to-do list.
- As an authenticated user, I want to create tasks so that I can organize my daily activities.
- As an authenticated user, I want to edit tasks so that I can update their details.
- As an authenticated user, I want to delete tasks so that I can remove unnecessary items.
- As an authenticated user, I want to mark tasks as completed so that I can track my progress.
- As a user, I want my tasks to be saved in a database so that they persist after logging out.

---

## 2. Functional Requirements
- User registration with username and password.
- Secure login and logout functionality.
- CRUD operations for tasks (Create, Read, Update, Delete).
- Validation for user input (e.g., minimum password length, non-empty task description).
- Association of tasks with the logged-in user.
- Display of tasks in a user-friendly interface.

---

## 3. Non-Functional Requirements
- Security: Passwords must be hashed using a secure algorithm (bcrypt).
- Usability: The interface should be simple and intuitive.
- Reliability: Tasks must persist in the database across sessions.
- Maintainability: Code should follow consistent style guidelines (PEP8, linting).
- Scalability: The system should be able to migrate from SQLite to PostgreSQL if needed.
- Testability: Unit and integration tests must cover core functionalities.

---

## 4. Acceptance Criteria
- A user can successfully register and log in.
- A logged-in user can create, edit, delete, and mark tasks as completed.
- Invalid inputs (e.g., empty task description, weak password) are rejected with clear error messages.
- All tasks are stored in the database and retrieved correctly after login.
