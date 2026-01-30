# Error Codes

The API uses standard HTTP status codes. Error responses include a JSON body with details.

## Error Response Format

```json
{
  "error": {
    "code": "invalid_request",
    "message": "The request body is missing required field 'name'",
    "details": {
      "field": "name",
      "reason": "required"
    }
  }
}
```

## Common Error Codes

### 400 Bad Request

The request was malformed or missing required parameters.

| Code | Message | Fix |
|------|---------|-----|
| `invalid_request` | Request body is invalid | Check JSON syntax |
| `missing_field` | Required field missing | Include all required fields |
| `invalid_field` | Field value is invalid | Check field type and constraints |

### 401 Unauthorized

Authentication failed or was not provided.

| Code | Message | Fix |
|------|---------|-----|
| `missing_auth` | No authorization header | Include `Authorization: Bearer <token>` |
| `invalid_token` | Token is invalid or expired | Refresh your token or generate a new API key |

### 403 Forbidden

You don't have permission for this action.

| Code | Message | Fix |
|------|---------|-----|
| `insufficient_scope` | Token lacks required scope | Request additional OAuth scopes |
| `role_required` | Your role can't perform this action | Contact your admin for elevated access |

### 404 Not Found

The requested resource doesn't exist.

### 429 Too Many Requests

Rate limit exceeded. Check the `Retry-After` header for when you can retry.

### 500 Internal Server Error

Something went wrong on our end. If this persists, contact support with the `X-Request-ID` header value from the response.
