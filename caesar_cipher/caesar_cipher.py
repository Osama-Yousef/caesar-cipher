from nltk.corpus import words

from collections import Counter

# english words collection
words_list= words.words()

def encrypt_(plain, key):
  """Function that takes in a plain text phrase and a numeric key and encrypts it using
   ceasar cipher with the shift equals to key. The plain text can be anything in english letters, 
   function will return encrypted lowercased text with the original punctuation marks and spaces"""

  # this line because the input may have capital letters
  plain = plain.lower()

  encrypted_plain = ''

  # when key is more than 26
  key = key % 26

  for char in plain:
    # I decided to use Ascii codes as a base for my solution

    ''' Any not english letters  will be skipped and returned in their original code '''
    if ord(char) not in range(97, 123): ## it means from a to z in Ascii code
      shifted_ascii = ord(char) ### NOTES : For example ord('B') returns 66 which is a unicode code point value of character 'B'.
      encrypted_plain += chr(shifted_ascii)
      continue
    
    # if Ascii code of the char + key value is more than 122 which means we can't just add key to the char code we need to go to the start of the alphabet again

    elif (ord(char)+key) > 122:
      # 122 = "z"  this line  BELOW TO find how far our current letter from the last letter in the alphabet
      steps_from_z = (122 - ord(char)) 

      # find how many steps from 'a' we need to do to encode our letter
      steps_from_a = key  - steps_from_z - 1
      # find the ascii code for the letter we need to display instead of current letter
      shifted_ascii = 97 + steps_from_a

    else:
      # in case if char code + key not bigger than 122
      shifted_ascii = (ord(char)+ key) 
      
    # add encrypted letters to the string after each loop iteration
    encrypted_plain += chr(shifted_ascii)
  
  return encrypted_plain


def decrypt_(cipher, key):
  """Function that takes in encrypted text and numeric key which will restore the encrypted 
  text back to its original form as long as correct key is supplied"""

  return encrypt_(cipher, -key)


def break_cipher(cipher):
  """Function to transform cipher into its original state without access to the key."""

  #Create a dictionary where all letters counted 
  letters_count = Counter(cipher)

  # delete all common punctuation elements that can affect our results
  del letters_count[',']
  del letters_count[' ']
  del letters_count['.']
  del letters_count[':']

  #list of all english letters 
  en_fingerprint = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p','g','w', 'y','b','v','k','x','j','q','z']

  # the most common letter in our text
  possible_e = letters_count.most_common(1)[0][0]

  ''' check each letter from en_fingerprint until our text doesn't look like english text'''
  for letter in en_fingerprint:
    # find difference between ascii code for most common letter in our text and current letter from en_fingerprint
    key = ord(possible_e) - ord(letter)
    # decrypt text using our generated key
    decrypted_text = decrypt_(cipher, key)
   
    # if decrypted text is recognised as english text >> return decrypted text else: continue checking whike have letters in en_fingerptint
    if is_english(decrypted_text):
      return decrypted_text
  
  # if the text considered as non english text
  return "Not English"
      
''' stretch goal '''
def is_english(text):
  """Helper function to find out if the given text 
   is english text or not"""
  words = text.split()
  
  word_count = 0

  for word in words:
    if word in words_list:
      word_count += 1
  ## our logic is like this
  # if more than half of the words in text recognized as english words consider text as english text
  if (word_count/len(words)) > 0.5:
    return True
  else: 
    return False

### exection and testing ###
if __name__ == "__main__":
    assert encrypt_('abc', 1) == 'bcd'
    assert encrypt_('acb', 10) == 'kml'
    assert encrypt_('abc',27) == 'bcd'
    assert decrypt_('bcd',1) == 'abc'

    print('All tests passed!!!!')