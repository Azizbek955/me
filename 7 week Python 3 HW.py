Mbox_file = 'your_mbox_file'
try:
    with open(Mbox_file, 'r', encoding='utf-8') as file:
        sender = None

        for line in file:
            if line.startswith('From '):

                words = line.split()
                if len(words) > 1 and words[1] != 'From:':
                    sender = words[1]
                    print(f'Sender: {sender}')
except FileNotFoundError:
    print(f"File '{Mbox_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
