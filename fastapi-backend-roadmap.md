# FastAPI & Backend Mastery — Roadmap

**Learner profile:** Comfortable with Python basics (functions, classes, loops, modules). New to type hints, async, and web frameworks. Goal: become a competent backend developer with FastAPI + Pydantic as the core.

**Version assumptions:** FastAPI and Pydantic v2 era. Confirm current versions when starting, as both move fast.

---

## Progress tracker

- [ ] Phase 0 — Python foundations
- [ ] Phase 1 — Pydantic
- [ ] Phase 2 — FastAPI core
- [ ] Phase 3 — Data layer
- [ ] Phase 4 — Auth & security
- [ ] Phase 5 — Testing
- [ ] Phase 6 — Production

> Don't move to the next phase until the build milestone for the current phase is complete.

---

## Phase 0 — Python foundations

Most "FastAPI confusion" is actually missing Python. Lock these first.

| Topic | What to understand |
|---|---|
| **Virtual environments & pip** | `python -m venv`, `requirements.txt`, installing packages cleanly — set this up before anything else |
| **Type hints & `typing`** | `list[int]`, `dict[str, X]`, `Optional`, `Union`/`\|`, `Literal` — FastAPI and Pydantic *are* type hints in action |
| **`async` / `await` & the event loop** | What "async" actually means, when it helps (I/O-bound) vs when it doesn't (CPU-bound). ASGI vs WSGI. |
| **Decorators** | Enough to understand what `@app.get(...)` is actually doing |
| **Context managers** | `with`, `__enter__`/`__exit__` — used for DB sessions and lifespan events |
| **HTTP & REST fundamentals** | Methods (GET/POST/PUT/DELETE), status codes, headers, request/response lifecycle |
| **Reading errors** | Pydantic and FastAPI produce structured validation errors — learn to read them early, saves significant debugging pain later |

**Phase 0 build milestone:** No build yet — solidify your Python before writing a single FastAPI line.

---

## Phase 1 — Pydantic

Pydantic is the foundation under FastAPI. FastAPI's request bodies, response models, and all validation are Pydantic. Learn it first, independently.

| Topic | What to understand |
|---|---|
| **`BaseModel`, fields, defaults** | Required vs optional fields, default values, `Field()` for metadata |
| **Validation** | Types, constraints (`gt`, `lt`, `min_length`), `field_validator`, `model_validator` |
| **Serialization** | `model_dump`, `model_dump_json`, aliases, `exclude`/`include` |
| **Nested models and lists of models** | A `Task` with a list of `Tag` models — nesting is central to real APIs |
| **`pydantic-settings`** | `BaseSettings`, `.env` files, managing secrets safely |

**Phase 1 build milestone:** Define `Task` and `User` Pydantic models with full validation. No routes yet — just models and tests in plain Python.

---

## Phase 2 — FastAPI core

| Topic | What to understand |
|---|---|
| **First app, `uvicorn`, `/docs` & `/redoc`** | `uvicorn main:app --reload`, exploring the auto-generated OpenAPI UI |
| **Path params, query params, request bodies** | `GET /tasks/{id}`, `?status=done`, `POST` body with a Pydantic model |
| **`response_model`, status codes & `HTTPException`** | Returning typed responses, 404s, 422 validation errors |
| **Dependency injection with `Depends()`** | FastAPI's signature feature — shared logic, DB sessions, current user |
| **Routers & project structure** | `APIRouter`, splitting routes into modules as the app grows |
| **Middleware & lifespan events** | Request logging, startup/shutdown hooks for DB connections |
| **pytest basics (intro)** | `pytest` fundamentals, writing your first test, `assert` statements — start the habit early before the app grows complex |

**Phase 2 build milestone:** Full CRUD API for Tasks using in-memory storage. Auto-docs at `/docs` working. Basic pytest tests for at least two endpoints.

---

## Phase 3 — Data layer

| Topic | What to understand |
|---|---|
| **Relational basics & SQL** | Tables, primary/foreign keys, `SELECT`/`INSERT`/`UPDATE`/`DELETE`, JOINs |
| **SQLAlchemy 2.0 ORM** | `DeclarativeBase`, mapped columns, relationships, async sessions |
| **Session management via `Depends()`** | One DB session per request, auto-closed — the standard pattern |
| **Alembic migrations** | `alembic init`, autogenerate, `upgrade`/`downgrade` — schema version control |
| **Repository pattern** | Separate data-access logic from route handlers for clean, testable architecture |

**Phase 3 build milestone:** Replace in-memory storage with a real PostgreSQL database. Add Alembic migrations.

---

## Phase 4 — Auth & security

| Topic | What to understand |
|---|---|
| **Password hashing** | `bcrypt` / `passlib` — never store plain passwords; hash on write, verify on login |
| **OAuth2 password flow & JWT tokens** | Token endpoint, creating/verifying JWTs with `PyJWT` — note: `python-jose` is largely unmaintained, use `PyJWT` instead |
| **Protecting routes** | `Depends(get_current_user)` — the standard pattern for authenticated endpoints |
| **Scopes & role-based access** | Admin vs regular user, restricting endpoints by role |
| **Common pitfalls** | `CORSMiddleware`, secrets in `.env`, never trust client-sent IDs |

**Phase 4 build milestone:** Add user registration, a `/login` endpoint returning a JWT, and protect all Task routes with authentication.

---

## Phase 5 — Testing

> pytest basics were introduced at the end of Phase 2. This phase goes deeper — focus here is on testing a real database, auth flows, and dependency overrides.

| Topic | What to understand |
|---|---|
| **`pytest` fixtures & `conftest.py`** | Fixture scope, `parametrize`, setup/teardown — building on the basics from Phase 2 |
| **`TestClient` & `httpx`** | Synchronous `TestClient` for simple tests, `AsyncClient` for async routes |
| **Test database setup** | SQLite in-memory or a separate Postgres test DB, rolled back after each test |
| **Mocking dependencies** | `app.dependency_overrides` — swap real DB for a test DB without changing routes |
| **Coverage & CI basics** | `pytest-cov`, aiming for 80%+, running tests in GitHub Actions |

**Phase 5 build milestone:** A test suite covering all CRUD endpoints and auth flows, with a passing CI run.

---

## Phase 6 — Production

| Topic | What to understand |
|---|---|
| **Project layout** | `src/` layout, settings per environment (dev / staging / prod) |
| **`uvicorn` + `gunicorn`** | Worker count, graceful shutdown, health check endpoint |
| **Dockerizing the app** | Multi-stage `Dockerfile`, `.dockerignore`, `docker-compose` with Postgres |
| **Logging & error monitoring** | Structured JSON logs, Sentry integration, request ID middleware |
| **Background tasks** | `FastAPI BackgroundTasks` for lightweight jobs; intro to Celery + Redis for heavier work |
| **CI/CD pipeline** | Lint (`ruff`), type check (`mypy`), test, build Docker image on push |

**Phase 6 build milestone:** Fully Dockerized app with `docker-compose` (app + Postgres), structured logging, and a complete CI pipeline.

---

## The build project — Task/Notes API

A single project that grows across every phase.

| After phase | State of the project |
|---|---|
| Phase 1 | Pydantic models for `Task` and `User` with validation |
| Phase 2 | Working CRUD API with in-memory storage and dependency injection |
| Phase 3 | Real PostgreSQL database with Alembic migrations |
| Phase 4 | User registration, login, and JWT-protected routes |
| Phase 5 | Test suite covering all endpoints and auth flows |
| Phase 6 | Dockerized, configured for multiple environments, deploy-ready |
