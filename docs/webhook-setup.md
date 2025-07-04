# GitHub Webhook Setup Guide

This document explains how to configure GitHub webhooks for the assessment task.

## Webhook Configuration

1. **Navigate to Repository Settings**
   - Go to your GitHub repository
   - Click on "Settings" tab
   - Select "Webhooks" from the left sidebar

2. **Add New Webhook**
   - Click "Add webhook"
   - Enter the payload URL: `https://your-domain.com/api/webhook`
   - Set Content type to: `application/json`
   - Select events to trigger:
     - Push events
     - Pull requests
     - Pull request reviews (for merge detection)

3. **Webhook Events**

### Push Events
Triggered when code is pushed to any branch.

**Payload includes:**
- Repository information
- Commit details
- Branch reference
- Author information

### Pull Request Events
Triggered when pull requests are opened, closed, or updated.

**Payload includes:**
- Pull request details
- Source and target branches
- Author information
- Action type (opened, closed, etc.)

### Merge Events
Triggered when pull requests are merged (subset of pull request events).

**Detection:**
- Pull request event with `action: "closed"`
- `pull_request.merged: true`

## Testing

1. Make a commit and push to test push events
2. Create a pull request to test PR events
3. Merge a pull request to test merge events

## Troubleshooting

- Check webhook delivery status in GitHub settings
- Verify endpoint is accessible and returns 200 status
- Check server logs for processing errors

