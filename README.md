#  Email Automation System

##  Project Overview

The Email Automation System is a Python-based application that simulates the process of sending emails in bulk. It validates email addresses, processes emails in batches, keeps track of successful and failed deliveries, and generates a detailed delivery report.

The project demonstrates the core concepts of email automation, input validation, batch processing, and report generation without requiring an actual email server.

---

##  Features

- Bulk email processing
- Email address validation using Regular Expressions (Regex)
- Batch-based email sending for scalability
- Simulated email delivery
- Tracks successful and failed emails
- Generates a delivery report
- Saves report to a text file
- Displays processing progress and summary

---

##  Technologies Used

- Python 3.x
- Regular Expressions (re)
- Time Module
- Datetime Module
- File Handling
- Object-Oriented Programming (OOP)

---

##  Project Structure

```
Email-Automation-System/
│── email_automation.py
│── README.md
│── email_report.txt      # Generated after execution
```

---

##  Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/Email-Automation-System.git
```

2. Navigate to the project directory.

```bash
cd Email-Automation-System
```

3. Run the program.

```bash
python email_automation.py
```

---

##  How It Works

1. A list of email addresses is provided to the system.
2. Each email address is validated using a regular expression.
3. Valid emails are processed and marked as successfully sent.
4. Invalid email addresses are recorded as failed deliveries.
5. Emails are processed in configurable batches to improve scalability.
6. After all batches are completed, a delivery report is displayed and saved to a text file.

---

##  Key Components

### Email Validation

- Uses Regular Expressions (Regex) to verify email format.
- Invalid email addresses are skipped and logged.

### Bulk Processing

- Processes emails in user-defined batch sizes.
- Simulates delays between email batches.

### Delivery Report

The system generates:

- Total emails processed
- Successfully sent emails
- Failed emails
- Timestamp of execution
- Lists of successful and failed email addresses

---

##  Sample Output

```
==============================
   EMAIL AUTOMATION SYSTEM
==============================

--- Processing Batch 1 ---

[SENT] To: user1@example.com
[SENT] To: user2@example.com
[INVALID] invalid-email

Batch completed.

--- Processing Batch 2 ---

[SENT] To: user4@example.com
[SENT] To: user5@example.com
[SENT] To: user6@example.com

Batch completed.

==============================
        DELIVERY REPORT
==============================

Total Emails: 10
Successfully Sent: 9
Failed: 1

Report saved as 'email_report.txt'
```

---

##  Generated Report

After execution, the application creates an **email_report.txt** file containing:

- Execution timestamp
- Number of successful emails
- Number of failed emails
- List of successful email addresses
- List of failed email addresses

---

##  Future Improvements

- Real email sending using SMTP
- HTML email support
- Email attachments
- Personalized email templates
- Email scheduling
- Multi-threaded batch processing
- Database integration
- GUI using Tkinter or PyQt
- Logging system for advanced monitoring

---

## Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- Email validation using Regular Expressions
- Batch processing techniques
- Python file handling
- Exception-free workflow design
- Report generation
- Modular programming practices

---

##  Author

**Fabiha Ashraf**

BS Artificial Intelligence

---

## 📄 License

This project is developed for educational purposes and is free to use, modify, and distribute.
