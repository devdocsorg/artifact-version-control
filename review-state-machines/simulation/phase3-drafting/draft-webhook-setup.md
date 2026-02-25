# Webhook Setup Guide

Learn how to create and manage webhooks to receive real-time event notifications
from the platform.

## Overview

Webhooks let your application receive automatic HTTP POST notifications when events
occur in your account — new orders, payment updates, user changes, and more. Instead
of polling the API, your server gets notified instantly.

**When to use webhooks:**
- You need real-time notifications (not batch/polling)
- Your integration reacts to events (Slack alerts, database syncs, workflow triggers)
- You want to reduce API calls and stay within rate limits

## Prerequisites

Before creating a webhook, you need:

- An API key with `webhooks:write` scope ([create one here](/settings/api-keys))
- A publicly accessible HTTPS endpoint that can receive POST requests
- Your endpoint must respond with a `2xx` status code within 30 seconds

> **Note:** HTTP (non-TLS) endpoints are not supported. Your endpoint must use HTTPS.

## Creating a Webhook

### Via API

```bash
curl -X POST https://api.company.com/v1/webhooks \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://your-server.com/webhooks",
    "events": ["order.created", "payment.completed"],
    "description": "Production order notifications"
  }'
```

**Response (201 Created):**

```json
{
  "id": "wh_abc123def456",
  "url": "https://your-server.com/webhooks",
  "events": ["order.created", "payment.completed"],
  "description": "Production order notifications",
  "secret": "whsec_k7j2m9x4p1q8...",
  "status": "active",
  "created_at": "2026-02-10T14:30:00Z"
}
```

> **Important:** The `secret` is only returned once, at creation time. Store it
> securely — you'll need it for signature verification.

### Via UI

1. Navigate to **Settings → Integrations → Webhooks**
2. Click **Create Webhook**
3. Enter your endpoint URL
4. Select the event types you want to receive
5. (Optional) Add a description
6. Click **Save**

Your webhook secret will be displayed once. Copy it and store it securely.

## Event Types

| Event | Description | Payload Key |
|-------|------------|-------------|
| `order.created` | New order placed | `order` |
| `order.updated` | Order details changed | `order` |
| `order.completed` | Order fulfilled | `order` |
| `order.cancelled` | Order cancelled | `order` |
| `payment.completed` | Payment succeeded | `payment` |
| `payment.failed` | Payment attempt failed | `payment` |
| `payment.refunded` | Refund issued | `payment` |
| `user.created` | New user registered | `user` |
| `user.updated` | User profile changed | `user` |
| `user.deleted` | User account removed | `user` |
| `invoice.created` | Invoice generated | `invoice` |
| `invoice.paid` | Invoice payment received | `invoice` |
| `subscription.created` | New subscription started | `subscription` |
| `subscription.cancelled` | Subscription cancelled | `subscription` |
| `subscription.renewed` | Subscription auto-renewed | `subscription` |

## Payload Format

Every webhook delivery sends a JSON POST request:

```json
{
  "id": "evt_789xyz",
  "type": "order.created",
  "created_at": "2026-02-10T14:35:22Z",
  "data": {
    "order": {
      "id": "ord_456",
      "total": 99.99,
      "currency": "USD",
      "status": "pending"
    }
  }
}
```

The `data` object contains the full resource under the key listed in the Event Types
table above.

**Payload size limit:** 256 KB. Events with payloads exceeding this limit are
truncated — the `data` object will contain a `truncated: true` flag and a `full_url`
link to retrieve the complete payload via API.

## Signature Verification

Every webhook delivery includes an HMAC-SHA256 signature in the
`X-Webhook-Signature-256` header. **Always verify this signature** to confirm the
request came from us and wasn't tampered with.

### How It Works

1. We compute `HMAC-SHA256(webhook_secret, raw_request_body)`
2. We send the hex digest in the `X-Webhook-Signature-256` header
3. Your server computes the same HMAC and compares

### Python

```python
import hmac
import hashlib

def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)

# In your request handler:
raw_body = request.get_data()  # raw bytes, NOT parsed JSON
signature = request.headers.get('X-Webhook-Signature-256')
if not verify_webhook(raw_body, signature, WEBHOOK_SECRET):
    return Response(status=401)
```

### Node.js

```javascript
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload, 'utf8')
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(`sha256=${expected}`),
    Buffer.from(signature)
  );
}
```

## Retry Behavior

If your endpoint returns a non-2xx status code or doesn't respond within 30 seconds,
we automatically retry delivery:

| Attempt | Delay After Failure |
|---------|-------------------|
| 1st retry | 1 minute |
| 2nd retry | 5 minutes |
| 3rd retry | 30 minutes |
| 4th retry | 30 minutes |
| 5th retry | 30 minutes |

After 5 failed retries, the delivery is marked as `failed` in your delivery log. The
webhook remains active — future events will still be delivered.

> **Note:** If 95% of deliveries fail over a 24-hour period, the webhook is
> automatically disabled and you'll receive an email notification.

## Delivery Logs

View delivery history for any webhook:

### Via API

```bash
curl https://api.company.com/v1/webhooks/wh_abc123def456/deliveries \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Via UI

Navigate to **Settings → Integrations → Webhooks → [your webhook] → Delivery Log**

Each delivery entry shows:
- **Event type** and event ID
- **HTTP status code** returned by your endpoint
- **Response time** (ms)
- **Delivery status:** `delivered`, `retrying`, `failed`
- **Timestamp** of each delivery attempt

## Troubleshooting

### Webhook not receiving events

1. **Check webhook status:** Navigate to Settings → Webhooks and confirm status is "Active"
2. **Verify endpoint URL:** Ensure your URL is publicly accessible (not localhost)
3. **Check event types:** Confirm you're subscribed to the event type you expect
4. **Test connectivity:** 
   ```bash
   curl -X POST https://your-server.com/webhooks \
     -H "Content-Type: application/json" \
     -d '{"test": true}'
   ```
5. **Check delivery log:** Look for failed deliveries with specific error codes

### Signature verification failing

1. **Use raw body:** You must verify against the raw request body, not parsed JSON.
   Parsing and re-serializing changes whitespace and field order.
2. **Check secret:** Ensure you're using the correct webhook secret (from creation time)
3. **Check header name:** The header is `X-Webhook-Signature-256` (not `X-Signature`)
4. **Encoding:** The signature is a hex-encoded SHA256 HMAC prefixed with `sha256=`

### Deliveries failing with timeout

1. **Respond quickly:** Your endpoint must return `2xx` within 30 seconds
2. **Process async:** Accept the webhook immediately, process the payload in a background job
3. **Check server logs:** Look for exceptions in your webhook handler

## Limits and Quotas

| Limit | Value |
|-------|-------|
| Webhooks per account | 25 |
| Events per webhook | Unlimited |
| Payload size | 256 KB |
| Response timeout | 30 seconds |
| Retry attempts | 5 |
| Auto-disable threshold | 95% failure over 24h |
