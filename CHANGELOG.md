# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [0.2.2] - 2022-03-28

### Changed
- Use classes to perform template generation instead of relying on template files

---

## [0.2.1] - 2022-03-23

### Changed
- `setup.py` now includes requirements for installing this project

---

## [0.2.0] - 2022-03-23

### Added
- Support not mounting requirements.txt file for Airflow services
- Support not mounting requirements-dev.txt file for the test runner service
- Support creation of a MongoDB service in Docker Compose cluster

---

## [0.1.1] - 2022-03-21

### Changed
- Changelog link to github markdown file instead of local relative reference

---

## [0.1.0] - 2022-03-21

### Added
- Generation of basic E2E test scripts for Airflow DAGs
