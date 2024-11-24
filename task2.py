book_records = []
while True: # The true here mean that the input is valid
    record = input("Enter book record (format: 'Book Title - Days Borrowed') or 'done' to finish: ")
    if record.lower() == 'done': # Here We write this line for check if the first input is done or not
        break
    book_records.append(record) # Append here to add the record to book_records
    book_dict = {}
    unique_titles = set() # We use the built in function named set to eliminate duplications
for record in book_records:
    title, days = record.split(" - ") # Split the title into title and days  Nader - 8 Mohammed - 8
    days = int(days) # To get the days in integer values
    if title in book_dict:
        book_dict[title] += days # This condition checks if the title is already in book_dict or not
    else:
        book_dict[title] = days
        unique_titles.add(title) # this condition to add the title to unique_titles to print It in another step
most_borrowed = max(book_dict , key=book_dict.get)
print (f"The most borrowed book: {most_borrowed}")        
least_borrowed = min(book_dict , key=book_dict.get) 
print (f"The least borrowed book: {least_borrowed}")        
average = sum(book_dict.values()) / len(book_dict)
print (f"The average: {average}")
print(f"The unique book: {unique_titles}")
sorted_books = sorted(book_dict.items(), key=lambda x: x[1], reverse=True) # I'm searching for sorted in this condition
print (f"The books after sorting in descending order: {sorted_books}")