import markovify

# Get raw text as string.
with open("test.txt") as f:
    text = f.read()

print("Generated Toxic Comments: ")
# Build the model.
text_model = markovify.Text(text)
for i in range(5):
    print(text_model.make_sentence())

with open("test2.txt") as f:
    text = f.read()

print("Generated Not Toxic Comments: ")
# Build the model.
text_model = markovify.Text(text)
for i in range(5):
    print(text_model.make_sentence())
