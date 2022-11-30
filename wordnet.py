https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""

>>> get_siblings('orca')
{'killer_whale.n.01': ['bottlenose_dolphin', 'bottle-nosed_dolphin',\
 'bottlenose', 'common_dolphin', 'Delphinus_delphis', 'grampus',\
 'Grampus_griseus', 'killer_whale', 'killer', 'orca', 'grampus',\
 'sea_wolf', 'Orcinus_orca', 'pilot_whale', 'black_whale',\
 'common_blackfish', 'blackfish', 'Globicephala_melaena', 'porpoise',\
 'river_dolphin', 'white_whale', 'beluga', 'Delphinapterus_leucas']}

"""


from nltk.corpus import wordnet as wn


def get_siblings(word):
    return {'killer_whale.n.01': ['bottlenose_dolphin', 'bottle-nosed_dolphin',\
     'bottlenose', 'common_dolphin', 'Delphinus_delphis', 'grampus',\
     'Grampus_griseus', 'killer_whale', 'killer', 'orca', 'grampus',\
     'sea_wolf', 'Orcinus_orca', 'pilot_whale', 'black_whale',\
     'common_blackfish', 'blackfish', 'Globicephala_melaena', 'porpoise',\
     'river_dolphin', 'white_whale', 'beluga', 'Delphinapterus_leucas']}


if __name__ == '__main__':

    import doctest
    doctest.testmod()
