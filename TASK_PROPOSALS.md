# Codebase Task Proposals

## 1) Typo fix task
**Task:** Correct repeated typo `plateform` -> `platform` in the project README.

- **Why:** Misspellings reduce professionalism and clarity.
- **Where:** `file storage using hybrid Cryptography/README.md`.
- **Acceptance criteria:** No occurrence of `plateform` remains in the README.

## 2) Bug fix task
**Task:** Fix `NameError` risk in Flask routes by importing `flash` (or removing its usage) in `app.py`.

- **Why:** `flash(...)` is called but never imported from `flask`, which will crash error-handling branches in `/data` and `/download_data`.
- **Where:** `file storage using hybrid Cryptography/app.py`.
- **Acceptance criteria:** Submitting requests without a file no longer raises `NameError`, and the route returns/redirects as intended.

## 3) Comment/documentation discrepancy task
**Task:** Correct inaccurate size comment in `divider.py` where `MAX = 1024*32` is labeled as `1 MB`.

- **Why:** `1024*32` equals **32 KiB**, not 1 MB; this can mislead maintainers about chunking behavior.
- **Where:** `file storage using hybrid Cryptography/divider.py`.
- **Acceptance criteria:** Comment/doc matches actual value, or constant is updated to match intended 1 MB chunk size.

## 4) Test improvement task
**Task:** Add pytest coverage for upload error paths and extension validation.

- **Why:** Core request validation is currently untested, and a small regression (e.g., missing `flash` import) can break runtime behavior.
- **Suggested scope:**
  - `allowed_file` accepts `.pem` (case-insensitive) and rejects other extensions.
  - POST `/data` without `file` part returns expected failure response path.
  - POST `/download_data` rejects non-`.pem` uploads with `Invalid File Format !`.
- **Acceptance criteria:** New tests run under `pytest` and fail before the bug fix / pass afterward.
