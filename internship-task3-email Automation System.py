import re
import time
from datetime import datetime


# =========================
# EMAIL AUTOMATION ENGINE
# =========================

class EmailAutomationSystem:

    def __init__(self, sender_name="Automation System"):
        self.sender_name = sender_name
        self.success = []
        self.failed = []

    # -------------------------
    # Email validation
    # -------------------------
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    # -------------------------
    # Simulated email sending
    # -------------------------
    def send_email(self, email, message):
        if not self.validate_email(email):
            self.failed.append(email)
            print(f"[INVALID] {email}")
            return False

        # simulate sending delay
        time.sleep(0.2)

        print(f"[SENT] To: {email}")
        self.success.append(email)
        return True

    # -------------------------
    # Batch processing (important for scalability)
    # -------------------------
    def send_bulk_emails(self, email_list, message, batch_size=5):
        print("\n==============================")
        print("   EMAIL AUTOMATION SYSTEM")
        print("==============================\n")

        total = len(email_list)

        for i in range(0, total, batch_size):
            batch = email_list[i:i + batch_size]

            print(f"\n--- Processing Batch {i // batch_size + 1} ---")

            for email in batch:
                self.send_email(email, message)

            print("Batch completed.\n")
            time.sleep(0.5)

        self.generate_report()

    # -------------------------
    # Final report generation
    # -------------------------
    def generate_report(self):
        print("\n==============================")
        print("        DELIVERY REPORT")
        print("==============================")

        print(f"Total Emails: {len(self.success) + len(self.failed)}")
        print(f"Successfully Sent: {len(self.success)}")
        print(f"Failed: {len(self.failed)}")

        print("\nTimestamp:", datetime.now())

        # Save report file
        with open("email_report.txt", "w") as file:
            file.write("EMAIL AUTOMATION REPORT\n")
            file.write(f"Time: {datetime.now()}\n\n")
            file.write(f"Success Count: {len(self.success)}\n")
            file.write(f"Failed Count: {len(self.failed)}\n\n")
            file.write("Successful Emails:\n")
            file.writelines(email + "\n" for email in self.success)

            file.write("\nFailed Emails:\n")
            file.writelines(email + "\n" for email in self.failed)

        print("\nReport saved as 'email_report.txt'")
        print("==============================\n")


# =========================
# MAIN EXECUTION
# =========================

if __name__ == "__main__":
    emails = [
        "user1@example.com", "user2@example.com", "invalid-email",
        "user4@example.com", "user5@example.com", "user6@example.com",
        "user7@example.com", "user8@example.com", "user9@example.com",
        "user10@example.com"
    ]

    message = """
Hello,

This is an automated email sent via the Email Automation System.
This system supports bulk processing, validation, and reporting.

Regards,
Internship Project
"""

    system = EmailAutomationSystem()
    system.send_bulk_emails(emails, message, batch_size=3)