# Authentication

All API requests require authentication. We support two methods:

## API Key Authentication

Include your API key in the request header:

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  https://api.acme.com/v2/users
```

> **Note:** API keys use the `X-API-Key` header, not `Authorization: Bearer`. The Bearer scheme is reserved for OAuth access tokens.

### Getting Your API Key

1. Log into the [Acme Dashboard](https://dashboard.acme.com)
2. Navigate to Settings > API Keys
3. Click "Generate New Key"
4. Copy the key — it won't be shown again

> **Security tip:** Store your API key in an environment variable, never in source code.

### Key Rotation

API keys expire after 90 days. To rotate:

```bash
curl -X POST https://api.acme.com/v2/auth/rotate \
  -H "X-API-Key: OLD_API_KEY" \
  -H "Content-Type: application/json"
```

Response:
```json
{
  "api_key": "acme_live_newkey123",
  "expires_at": "2025-04-30T00:00:00Z",
  "previous_key_valid_until": "2025-02-07T00:00:00Z"
}
```

The old key remains valid for 7 days after rotation to allow migration.

## OAuth 2.0

For user-facing applications, use OAuth 2.0 authorization code flow.

### Step 1: Redirect to Authorization

```
GET https://auth.acme.com/authorize
  ?client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &response_type=code
  &scope=users:read+projects:write
```

> **Changed in v2.1:** Scopes now use resource-based format (`users:read`, `projects:write`) instead of the old `read write` format.

### Step 2: Exchange Code for Token

```bash
curl -X POST https://auth.acme.com/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=AUTH_CODE" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "redirect_uri=https://yourapp.com/callback"
```

> **Important:** The `redirect_uri` must exactly match the one used in Step 1.

### Step 3: Use the Access Token

```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" \
  https://api.acme.com/v2/users/me
```

## Token Expiry

Access tokens expire after 1 hour. Use the refresh token to get a new one:

```bash
curl -X POST https://auth.acme.com/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=YOUR_REFRESH_TOKEN" \
  -d "client_id=YOUR_CLIENT_ID"
```

If the refresh token is also expired (30 days), the user must re-authorize through Step 1.
