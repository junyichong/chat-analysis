import csv

csv_file = 'data/fuslie.csv'  

# Dictionary to store author and message count
author_message_count = {}  

total_messages = 0

with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=';')

    # Skip the header row if it exists
    next(reader) 

    # Iterate through each row in the CSV
    for row in reader:

        # Get the author from the second row
        author = row[1] 
        
        # Update the count for the author
        if author in author_message_count:
            author_message_count[author] += 1
        else:
            author_message_count[author] = 1

        total_messages += 1

# Print the message count for each author
# for author, message_count in author_message_count.items():
#     print(f"{author}: {message_count} messages")

num_unique_authors = len(author_message_count)
print(f"The number of unique chatters is: {num_unique_authors}")

print(f"The total number of messages is: {total_messages}")

messages_per_author = format(total_messages / num_unique_authors, ".2f")
print(f"The average number of messages per chatter is: {messages_per_author}")
