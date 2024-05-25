import email_sender


def main():
    mail_body = """
    <html>
    <body style="background-color:blue;">
    <hr style="border:1px solid black;"> <!-- Чорний роздільник -->
    <p style="color:yellow; font-style:italic; font-size:24px;">My homework</p> <!-- Слова більшого розміру -->
    <hr style="border:1px solid black;"> <!-- Чорний роздільник -->
    </body>
    </html>
    """
    email_sender.send_email(
        ["kirillchickalenko@ukr.net", "chikalenko.kiriill@gmail.com"],
        mail_body=mail_body,
        mail_subject="Hello! This is my homework!",
        attachment="main.py",
    )


if __name__ == "__main__":
    main()
