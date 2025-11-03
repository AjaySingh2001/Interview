
# Square Payment API Documentation

## 🧾 Overview
This API handles **secure payment processing** for nanny bookings using the **Square Payment Gateway**.  
It allows authenticated parents to make payments for confirmed nanny sessions.

---

## **Endpoint**
**POST** `/api/payments/square/`

---

## **Required Fields**
| Field | Type | Description |
|--------|------|-------------|
| `nonce` | string | Unique token from Square frontend (represents card/payment source). |
| `booking_id` | int | ID of the booking being paid for. |
| `total_amount` | decimal | Total payment amount (in GBP). |
| `platform_commission` | decimal | Commission retained by the platform. |

---

## **Workflow Explanation**
1. **Validation**
   Ensures all required fields (`nonce`, `booking_id`, `total_amount`, `platform_commission`) are provided.

2. **Fetch Booking**
   Retrieves the booking along with related `nanny` and `parent` details.

3. **Initialize Square Client**
   Uses `SQUARE_ACCESS_TOKEN` and `SQUARE_LOCATION_ID` from environment variables.  
   Operates in **Sandbox** mode for testing.

4. **Payment Request to Square**
   ```python
   client.payments.create(
       source_id=nonce,
       idempotency_key=str(uuid.uuid4()),
       amount_money={
           "amount": int(Decimal(total_amount) * 100),  # GBP → pence
           "currency": "GBP"
       },
       location_id=os.getenv("SQUARE_LOCATION_ID")
   )
   ```
   > 💡 Amount is multiplied by 100 because Square expects the smallest currency unit (pence, not pounds).

5. **Handle Response**
   - If payment is successful (`status == "COMPLETED"`), mark it as `"successful"`.
   - Otherwise, mark it as `"failed"`.

6. **Record Transaction**
   Saves payment details in the `Payment` table, including:
   - Parent, Nanny, Booking
   - Amount, Commission
   - Transaction ID, Status, First-time payment flag

7. **Booking Update**
   If successful, updates booking status → `"confirmed"`.

8. **Notification**
   Sends push notification to the nanny using:
   ```python
   send_payment_notification_to_nanny(booking)
   ```

9. **Error Handling**
   - `Booking.DoesNotExist` → 404  
   - `ApiError` from Square → 400  
   - Any other exception → 500

---

## **Key Talking Points**
✅ Implemented **Square Payment Gateway** using official SDK.  
✅ Handled **currency conversion** (GBP → pence) before sending to Square.  
✅ Used **idempotency key** to prevent duplicate charges.  
✅ Stored full payment details for audit and reporting.  
✅ Sent **real-time notifications** to nannies on successful payment.  
✅ Included **proper exception handling** and response codes.

---

## **Future Improvements**
- Wrap payment + booking update in a **`transaction.atomic()`** block for data consistency.  
- Implement **webhook verification** for asynchronous payment confirmation.  
- Log payment response for debugging and auditing.
