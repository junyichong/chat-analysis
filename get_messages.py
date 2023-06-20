from chat_downloader import ChatDownloader
import csv

url = 'https://www.youtube.com/watch?v=ZuuyTZ-9gDs&ab_channel=Valkyrae'

csv_file = open('test.csv', 'w', newline='')
writer = csv.writer(csv_file, delimiter =';')

header = ['Time Stamp', 'Name', 'Message']
writer.writerow(header)

chat = ChatDownloader().get_chat(url) 

for message in chat:  
    # chat.print_formatted(message)         
    time_stamp = message["time_text"]
    author_name = message["author"]["name"]
    message_content = message["message"]

    try:
        writer.writerow([time_stamp, author_name, message_content])

    except UnicodeEncodeError:
        # Handle encoding error by replacing or ignoring unsupported characters
        cleaned_author_name = author_name.encode("ascii", "ignore").decode("utf-8")
        cleaned_message_content = message_content.encode("ascii", "ignore").decode("utf-8")
        writer.writerow([time_stamp, cleaned_author_name, cleaned_message_content])

csv_file.close()