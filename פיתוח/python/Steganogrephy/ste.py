# פונקציה לחיפוש תווים קריאים מתוך קובץ בינארי
def extract_readable_strings(file_path, min_length=4):
    with open(file_path, 'rb') as file:
        content = file.read()  # קרא את כל הקובץ בתור תכולה בינארית
        current_string = ""

        for byte in content:
            # המרת כל בית לתו תו ASCII
            if 32 <= byte <= 126:  # תו קריא ב־ASCII (כולל תו רווח)
                current_string += chr(byte)
            else:
                # אם מצאנו תו שלא קריא, בודקים אם יש מחרוזת ארוכה מספיק
                if len(current_string) >= min_length:
                    print(current_string)  # הצגת המחרוזת הקריאה
                current_string = ""  # לאתחל את המחרוזת

        # הדפסת המחרוזת הקריאה אם היא ארוכה מספיק
        if len(current_string) >= min_length:
            print(current_string)

# דוגמת שימוש
file_path = 'path_to_your_image.jpg'  # החלף בנתיב לקובץ שלך
extract_readable_strings(file_path)

