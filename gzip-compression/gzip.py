import gzip
import shutil

def compress(input_file, output_file):
  with open(input_file, 'rb') as file_in:
    with gzip.open(output_file, 'rb') as file_out:
      shutil.copyfileobj(file_in, file_out)

# Exemplo de utilização

file_input = 'example.txt'
file_output = 'example.gz'

compress(file_input, file_output)