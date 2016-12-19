
# coding: utf-8

# In[ ]:

import sys, locale
sys.stdin.encoding

#Determines block of text to search for and decodes the ascii characters
stringToSearch = u'The undersigned counterparty instructs INTL FCStone Markets, LLC that this Swap Transaction will not be submitted for clearing to a derivatives clearing organization on the basis that the Transaction qualifies for the “End-User Exception” from clearing under section 2h(7) of the CEA. The undersigned counterparty is not a financial entity as defined in CEA section 2h(7)(C), is entering into the Swap Transaction to hedge or mitigate a commercial risk and has notified the CFTC, through the DTCC, the manner in which the undersigned generally meets its financial obligations associated with non-cleared swaps'
stringToSearch = stringToSearch.replace(u"\u201C",'"').replace(u"\u201D", '"')

#asks for input and decodes ascii characters if user happens to enter any
inputText = raw_input("Enter entire text to search: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
#encoding = 'utf-8' if sys.stdin.encoding in (None, 'ascii') else sys.stdin.encoding
#print inputText.decode(encoding)
inputText = inputText.replace(u"\u201C",'"').replace(u"\u201D", '"')
#print inputText


# In[ ]:

#checks if user input contains the desired string
value = inputText.find(stringToSearch)
if value != -1:
    print "Exists"
else:
    print "Doesn't Exist"

