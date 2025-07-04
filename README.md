# Action Repository

This repository is part of the GitHub Webhook Assessment Task. It serves as the source repository that will trigger webhook events when actions like push, pull requests, and merges occur.

## Purpose

This repository demonstrates:
- **Push events**: When code is pushed to any branch
- **Pull Request events**: When pull requests are created
- **Merge events**: When pull requests are merged

## Webhook Configuration

The webhook endpoint is configured to send events to the webhook-repo Flask application, which processes and stores the events in MongoDB.

## Test Branches

- `main`: Main branch for production-ready code
- `staging`: Staging branch for testing
- `dev`: Development branch for ongoing work

## Sample Files

- `app.py`: Sample Python application
- `config.json`: Configuration file
- `docs/`: Documentation directory

