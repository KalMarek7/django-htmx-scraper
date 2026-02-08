# Django Scraping PoC (HTMX + MySQL + Docker)

## Project Overview

A Proof of Concept (PoC) project demonstrating the integration of **Django** with **HTMX** and web scraping tools (**BeautifulSoup**). The system allows for asynchronous data fetching from external sources, persisting them in a **MySQL** database, and dynamically updating the UI without full page reloads.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTMX (Dynamic DOM updates)
- **Database:** MySQL
- **Scraping:** BeautifulSoup4, Requests
- **Infrastructure:** Docker, Docker Compose

## Key Features

- **On-demand Scraping:** Data fetching triggered via HTMX-powered buttons.
- **Dynamic UI:** Table updates using HTMX for a seamless user experience.
- **Data Persistence:** Managed via Docker volumes for MySQL data.
- **Containerization:** Fully dockerized environment for easy deployment and testing.

## How to Run

### Prerequisites

- Docker
- Docker Compose

1. Clone the repository:

    ```bash
    git clone [https://github.com/YourUser/repo-name.git](https://github.com/YourUser/repo-name.git)
    cd repo-name

    ```

2. Run `docker compose up`
