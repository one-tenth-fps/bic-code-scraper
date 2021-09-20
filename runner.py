import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'runspider',
            'bic-code-scraper.py',
            '-o',
            'bic.csv',
        ]
    )
except SystemExit:
    pass