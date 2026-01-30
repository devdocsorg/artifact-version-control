# Acme API Documentation

Welcome to the Acme API. This documentation covers everything you need to integrate with our platform.

## Quick Start

1. [Get your API key](authentication.md)
2. [Make your first request](endpoints.md)

## Table of Contents

- [Authentication](authentication.md) — API keys, OAuth, and token management
- [Endpoints](endpoints.md) — Full API reference with inline error codes
- [Changelog](changelog.md) — Version history and breaking changes

## Base URL

```
https://api.acme.com/v2
```

## Rate Limits

All endpoints are rate-limited to 1000 requests per minute per API key. Exceeding this limit returns a `429 Too Many Requests` response.

## Support

Contact us at api-support@acme.com or visit our [developer forum](https://forum.acme.com).
