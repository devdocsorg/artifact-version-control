# API Endpoints

All endpoints use the base URL `https://api.acme.com/v2`.

## Projects

### List Projects

```
GET /projects
```

Returns all projects accessible to the authenticated user.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter by status: `active`, `archived` |
| `limit` | integer | No | Max results (default: 20) |

**Example:**

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.acme.com/v2/projects?status=active"
```

**Response:**

```json
{
  "data": [
    {
      "id": "proj_456",
      "name": "Website Redesign",
      "status": "active",
      "created_at": "2025-01-15T10:00:00Z"
    }
  ],
  "total": 5
}
```

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 400 | `invalid_field` | Invalid `status` value. Must be `active` or `archived` |
| 401 | `missing_auth` | No authorization header provided |

### Create Project

```
POST /projects
```

**Body:**

```json
{
  "name": "New Project",
  "description": "Project description"
}
```

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 400 | `missing_field` | `name` is required |
| 403 | `role_required` | Only admins can create projects |

### Delete Project

```
DELETE /projects/:id
```

Permanently deletes a project and all associated data. This action cannot be undone.

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 404 | `not_found` | Project does not exist |
| 403 | `role_required` | Only admins can delete projects |

## Users

### List Users

```
GET /users
```

Returns a list of users in your organization.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | integer | No | Max results (default: 20, max: 100) |
| `offset` | integer | No | Pagination offset |

**Example:**

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.acme.com/v2/users?limit=10"
```

**Response:**

```json
{
  "data": [
    {
      "id": "usr_123",
      "name": "Jane Doe",
      "email": "jane@example.com",
      "role": "admin"
    }
  ],
  "total": 42
}
```

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 401 | `missing_auth` | No authorization header provided |
| 401 | `invalid_token` | Token is invalid or expired |

### Get User

```
GET /users/:id
```

Returns a single user by ID.

**Example:**

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://api.acme.com/v2/users/usr_123"
```

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 404 | `not_found` | User does not exist |

### Create User

```
POST /users
```

Creates a new user.

**Body:**

```json
{
  "name": "John Smith",
  "email": "john@example.com",
  "role": "member"
}
```

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 400 | `missing_field` | `name` and `email` are required |
| 400 | `invalid_field` | `role` must be `admin`, `member`, or `viewer` |
| 409 | `duplicate` | A user with this email already exists |

## Common Errors

All endpoints may return these errors:

| Status | Code | Description |
|--------|------|-------------|
| 429 | `rate_limited` | Rate limit exceeded. Check `Retry-After` header |
| 500 | `internal_error` | Server error. Contact support with `X-Request-ID` |
