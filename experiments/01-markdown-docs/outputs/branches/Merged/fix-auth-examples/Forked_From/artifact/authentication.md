# Authentication

All API requests require authentication. We support two methods:

## API Key Authentication

Include your API key in the request header:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.acme.com/v2/users
```

### Getting Your API Key

1. Log into the [Acme Dashboard](https://dashboard.acme.com)
2. Navigate to Settings > API Keys
3. Click "Generate New Key"
4. Copy the key — it won't be shown again

### Key Rotation

API keys expire after 90 days. To rotate:

```bash
curl -X POST https://api.acme.com/v2/auth/rotate \
  -H "Authorization: Bearer OLD_API_KEY"
```

Response:
```json
{
  "new_key": "acme_live_newkey123",
  "expires_at": "2025-04-30T00:00:00Z"
}
```

## OAuth 2.0

For user-facing applications, use OAuth 2.0 authorization code flow.

### Step 1: Redirect to Authorization

```
GET https://auth.acme.com/authorize
  ?client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &response_type=code
  &scope=read write
```

### Step 2: Exchange Code for Token

```bash
curl -X POST https://auth.acme.com/token \
  -d "grant_type=authorization_code" \
  -d "code=AUTH_CODE" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET"
```

### Step 3: Use the Access Token

```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" \
  https://api.acme.com/v2/users/me
```

## Token Expiry

Access tokens expire after 1 hour. Use the refresh token to get a new one:

```bash
curl -X POST https://auth.acme.com/token \
  -d "grant_type=refresh_token" \
  -d "refresh_token=YOUR_REFRESH_TOKEN"
```
