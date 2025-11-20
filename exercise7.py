import re

emails = [
    "abc@gmail.com",
    "1234@#xyz.com",
    "address@domain.com",
    "grwcv.teacf12@",
    "rtd@tagline.in",
    "ritudhanani28@tagline.look",
    "ritu.dhanani.ritu12@dhanani34",
    "fake@fake123.fakercom"
]

regex = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'

output = [email for email in emails if re.match(regex, email)]

print(output)
