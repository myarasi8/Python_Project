def clean_text(txt):
    """Takes the txt and removes all the punctuation"""
    s = txt.lower()
    for ch in s:
        if ch in ['.', '!', '?', ',', ':', ';']:
            s = s. replace(ch, '')
    return s

def sample_file_write(filename):
    """A function that demonstrates how to write a
         Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.

        
def sample_file_read(filename):
    """A function that demonstrates how to read a
         Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)


def stem(word):
    """Function that removes the suffixes and prefixes of a word"""
    if word[-3:] == 'ing':
        stem = word[:-3]
        return stem
    elif word [-2:] == 'er':
        stem = word[:-3]
        return stem
    elif word [-2:] == 'es':
        stem = word[:-3]
        return stem
    elif word[:4] == 'anti':
        stem = word[4:]
        return stem
    elif word[:2] == 're':
        stem = word[2:]
        return stem
    elif word[:3] == 'mis':
        stem = word[3:]
        return stem
    elif word[:2] == 'ex':
        stem = word[2:]
        return stem
    elif word[:2] == 'un':
        stem = word[2:]
        return stem
    elif word[:3] == 'non':
        stem = word[3:]
        return stem
    elif word[:3] == 'dis':
        stem = word[3:]
        return stem
    elif word[-2:] == 'ed':
        stem = word[:-2]
        return stem
    elif word[:3] == 'pre':
        stem = word[3:]
        return stem
    else:
        stem = word
        return stem

from math import log
def compare_dictionaries(d1, d2):
    """Takes two dictionaries, computes, and returns the log similarity score"""
    score = 0
    total = 0
    for w in d1:
        total += d1[w]
    for w in (d2):
        if w in d1:
            score = log(d1[w]/total)*(d2[w])
        else:
            score = log(0.5/total)*(d2[w])
    return score

    
#Part I
class TextModel:

    def __init__(self, model_name):
        self.name = str(model_name)
        self.words = {}                           #dictionary that records number of times each word appears in a text
        self.word_lengths = {}                 #dictionary that records number of times each word length appears
        self.stems = {}                           #dictionary that records number of times each word stem appears in a text
        self.sentence_lengths = {}          #dictionary that records number of times each sentence_length appears
        self.punctuation_frequency = {}  #dictionary that records number of times a '.?!' appear in the text
        
    def __str__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += ' number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += ' number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += ' number of stems: ' + str(len(self.stems)) + '\n'
        s += ' punctuation frequence: ' + str(len(self.punctuation_frequency)) + '\n'
        return s

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces to all of the dictionaries in this text model."""
    #Code for updating sentence_lengths dictionary # must do this before clean_text
        words = s.split()
        for w in words:
            ch = ['.', '!', '?']
            if w[-1] in ch:
                pos = words.index(w)
                sentence_length = len(words[0:(pos+1)])
                if sentence_length not in self.sentence_lengths:
                    self.sentence_lengths[sentence_length] = 1
                    words = words[(pos+1):]
                else:
                    self.sentence_lengths[sentence_length] += 1
                    words = words[(pos+1):]

    #Code for updating punctuation_frequency dictionary
        words = s.split()
        ch = ['.', '!', '?']
        x = ''
        for w in words:
            if w[-1] in ch:
                x = w[-1]
                if x not in self.punctuation_frequency:
                    self.punctuation_frequency[x] = 1
                else:
                    self.punctuation_frequency[x] += 1

    # Add code to clean the text and split it into a list of words.
    # *Hint:* Call one of your other methods!
        words = clean_text(s).split()

        # Code for updating the words dictionary.
        for w in words:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1

        # Add code to update other feature dictionaries.
        #Code for updating the word_lengths dictionary
        for w in words:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1

        #Code for stem dictionary
        for w in words:
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
        

    def add_file(self, filename):
        """Adds all of the text in the file identified by filename to the model"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        x = f.read()
        #print(x)
        f.close()
        return self.add_string(x)
        
    def save_model(self):
        """Saves the features of the Textmodel to the file
        """
        #words = {'test':1, 'foo': 42}
        #word_lengths = {8:1, 4:8}
       
        filename_1 = self.name + '_' + 'words'
        f = open(filename_1, 'w')
        f.write(str(self.words))
        f.close()

        filename_2 = self.name + '_' + 'word_lengths'
        f = open(filename_2, 'w')
        f.write(str(self.word_lengths))
        f.close()

        filename_3 = self.name + '_' + 'sentence_lengths'
        f = open(filename_3, 'w')
        f.write(str(self.sentence_lengths))
        f.close()

        filename_4 = self.name + '_' + 'stems'
        f = open(filename_4, 'w')
        f.write(str(self.stems))
        f.close()

        filename_5 = self.name + '_' + 'punctuation_frequency'
        f = open(filename_5, 'w')
        f.write(str(self.punctuation_frequency))
        f.close()

    def read_model(self):
        """Reads the stored dictionaries for the called TextModel object from their files
             and assigns them to the attributes of the called TextModel
        """
        f = open(filename_1, 'r')
        d_str_1 = f.read()
        f.close()
        self.words = dict(eval(d_str_1))

        f = open(filename_2, 'r')
        d_str_2 = f.read()
        f.close()
        self.word_lengths = dict(eval(d_str_2))

        f = open(filename_3, 'r')
        d_str_3 = f.read()
        f.close()
        self.sentence_lengths = dict(eval(d_str_3))

        f = open(filename_4, 'r')
        d_str_4 = f.read()
        f.close()
        self.stems = dict(eval(d_str_4))

        f = open(filename_5, 'r')
        d_str_5 = f.read()
        f.close()
        self.punctuation_frequency = dict(eval(d_str5))

    def similarity_scores(self, other):
        """Takes the log similarity score of all the dictionaries and puts them in a list"""
        word_score = compare_dictionaries(other.words, self.words)
        word_score2 = compare_dictionaries(other.word_lengths, self.word_lengths)
        word_score3 = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        word_score4 = compare_dictionaries(other.stems, self.stems)
        word_score5 = compare_dictionaries(other.punctuation_frequency, self.punctuation_frequency)
        dictList = [word_score, word_score2, word_score3, word_score4, word_score5]
        return dictList

    def classify(self, source1, source2):
        """Returns which source is more similar to mystery, source 1 or source 2"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', source1.name, ':', scores1)
        print('scores for', source2.name, ':', scores2)
        weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] + 2*scores1[3] + 4*scores1[4]
        weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2] + 2*scores2[3] + 4*scores2[4]
        if weighted_sum1 > weighted_sum2:
            print('mystery is more likely to have come from', source1.name)
        elif weighted_sum1 < weighted_sum2:
            print('mystery is more likely to have come from', source2.name)
        else:
            return
# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def test():
    """ The test function."""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
        
        

    
        

    






















    
        
        
