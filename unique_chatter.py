import csv
import os

streamer = "fuslie"
suffix = 1

if suffix == 1:
    base_filename = f"data/{streamer}.csv"
    filename = base_filename
else:
    filename = f"data/{streamer}_{suffix}.csv"

# Dictionary to store author and message count
author_message_count = {}  

total_messages = 0

with open(filename, 'r', newline='') as file:
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

# Write the results to a CSV file
result_filename = "results.csv"
result_csv_file = open(result_filename, "a", newline="")
writer = csv.writer(result_csv_file, delimiter =";")

# header = ['Streamer', 'Total messages', 'Total chatters', 'Average messages per chatter']
# writer.writerow(header)

num_unique_authors = len(author_message_count)
print(f"The number of unique chatters is: {num_unique_authors}")

print(f"The total number of messages is: {total_messages}")

messages_per_author = format(total_messages / num_unique_authors, ".2f")
print(f"The average number of messages per chatter is: {messages_per_author}")

writer.writerow([streamer, total_messages, num_unique_authors, messages_per_author])