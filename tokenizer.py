# This script tokenizes the text from a file into integers and decodes integers back to text.

file = input("Enter the path to the text file : ")

# opening the file and reading its content.
with open (file, "r") as f:
    raw_text = f.read()

# using regular expressions to preprocess the text
import re
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# sorting the unique tokens to create a vocabulary
all_tokens = sorted(list(set(preprocessed)))
# adding special tokens to the vocabulary
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

# creating a vocabulary mapping each unique token to an integer
vocab = {token:integer for integer,token in enumerate(all_tokens)}



# class to tokenize text into integers and decode integers back to text
class SimpleTokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = { i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text


# main execution
# This part will take input from the user to tokenize and decode text  
tokenizer = SimpleTokenizer(vocab)

text1 = input("Enter the first text to tokenize: ")
text2 = input("Enter the second text to tokenize: ")

text = " <|endoftext|> ".join((text1, text2))

result_encode = tokenizer.encode(text)
result_decode = tokenizer.decode(tokenizer.encode(text))
print("Encoded:", result_encode)
print("Decoded:", result_decode)