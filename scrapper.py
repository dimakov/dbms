import datefinder
import nltk
import operator
from nltk.tag.stanford import StanfordNERTagger
from geotext import GeoText

nltk.internals.config_java("C:/Program Files/Java/jdk1.8.0_74/bin/java.exe")
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

counts = dict()
filename = '6Times.txt'

with open(filename, 'r') as f:
    raw_data = f.read()
    date = datefinder.find_dates(raw_data, source=True)
    for match in date:
        print match
    document = nltk.sent_tokenize(raw_data)
    for sentence in document:
        places = GeoText(sentence)
        if places.cities:
            for city in places.cities:
                counts[city] = counts.get(city, 0) + 1
    print "Probable cities:"
    print max(counts.iteritems(), key=operator.itemgetter(1))[0]
    print "Probable streets:"
    for sentence in document:
        if "Street" not in sentence and "street" not in sentence:
            continue
        tagged =  st.tag(sentence.split())
        for tup in tagged:
            if tup[1] == "LOCATION" and tup[0] not in counts:
                print tup[0]