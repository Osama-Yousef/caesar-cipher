from caesar_cipher.caesar_cipher import encrypt_, decrypt_, break_cipher


#### tests for encrypting #####

def test_encrypt_normal():
  assert encrypt_('cat', 5) == "hfy"


def test_encrypt_bigkey27():
  assert encrypt_('cat', 27) == "dbu"



def test_encrypt_bigkey195():  ## test if encrypt handling with small letter
  assert encrypt_('cat', 195) == "png"

def test_encrypt_Capital195(): ## test if encrypt handling with capital letter
  assert encrypt_('Cat', 195) == "png"


def test_encrypt_sentence_text():
  assert encrypt_('In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.', 7) == "pu h ovsl pu aol nyvbuk aolyl spclk h oviipa. uva h uhzaf, kpyaf, dla ovsl, mpsslk dpao aol lukz vm dvytz huk hu vvgf ztlss, uvy fla h kyf, ihyl, zhukf ovsl dpao uvaopun pu pa av zpa kvdu vu vy av lha: pa dhz h oviipa-ovsl, huk aoha tlhuz jvtmvya."

##### tests for decrypting ########


def test_decrypt__simple():
  assert decrypt_('hfy', 5) == 'cat'

def test_decrypt__sentence_text():
    assert decrypt_('pu h ovsl pu aol nyvbuk aolyl spclk h oviipa. uva h uhzaf, kpyaf, dla ovsl, mpsslk dpao aol lukz vm dvytz huk hu vvgf ztlss, uvy fla h kyf, ihyl, zhukf ovsl dpao uvaopun pu pa av zpa kvdu vu vy av lha: pa dhz h oviipa-ovsl, huk aoha tlhuz jvtmvya.', 7) == 'in a hole in the ground there lived a hobbit. not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'

def test_decrypt_bigkey195():
  assert decrypt_('png', 195) == 'cat'

######  test if it  allow non-alpha characters but ignore them, including white space     #########
def test_break_cipher_small_word():
  assert break_cipher('h f y') == 'e c v'

  ##################################################
        ########## last required test ##########
''' TEST if decrypting encrypted version of ( It was the best of times, it was the worst of times.)  WITHOUT knowing the shift used.'''         ############################

def test_break_cipher_text():
  text = 'It was the best of times, it was the worst of times'

  cipher = encrypt_(text, 5)

  assert break_cipher(cipher) == text.lower()

######### additional tests using break ##################

def test_break_cipher_small_word():
  assert break_cipher('hfy') == 'cat'

def test_break_cipher_small_sentence():
  assert break_cipher("dcrt ndj zcdl paa iwt tatbtcih, xi'h cdi sxuuxrjai id ejaa idvtiwtg p htcitcrt") == "once you know all the elements, it's not difficult to pull together a sentence"
####################################################

'''         stretch goal       ''' 
''' using the Break  for a message written in language other than English '''

def test_break_cipher_notenglish():
  cipher = encrypt_('russkoeslovo', 145)
  assert break_cipher(cipher) == "Not English"

def test_break_cipher_notenglish2():
  cipher = encrypt_('привет', 145)
  assert break_cipher(cipher) == "Not English"