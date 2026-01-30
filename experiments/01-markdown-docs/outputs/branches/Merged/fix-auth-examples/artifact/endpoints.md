# API Endpoints

All endpoints use the base URL `https://api.acme.com/v2`.

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
curl -H "X-API-Key: YOUR_API_KEY" \
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

### Get User

```
GET /users/:id
```

Returns a single user by ID.

**Example:**

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
  "https://api.acme.com/v2/users/usr_123"
```

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
curl -H "X-API-Key: YOUR_API_KEY" \
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

### Delete Project

```
DELETE /projects/:id
```

Permanently deletes a project and all associated data. This action cannot be undone.
