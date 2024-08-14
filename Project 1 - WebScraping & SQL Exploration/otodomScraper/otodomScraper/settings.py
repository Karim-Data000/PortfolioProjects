# Scrapy settings for otodomScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "otodomScraper"

SPIDER_MODULES = ["otodomScraper.spiders"]
NEWSPIDER_MODULE = "otodomScraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "otodomScraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 3
# AUTOTHROTTLE_MAX_DELAY = 4

# FEEDS = {
#     'sale - apartment - tryOtodomdata.json': {
#         'format': 'json',
#         'encoding': 'utf8',
#         'store_empty': False,
#       #   'fields': None,  # Or specify fields if you want a specific order
#       #   'indent': 3,     # For pretty-printing JSON
#         'overwrite': False
#     },
#     'sale - apartment - tryOtodomdata.csv': {
#         'format': 'csv',
#         'encoding': 'utf8',
#         'store_empty': False,
#       #   'fields': None,  # Or specify fields if you want a specific order
#       #   'indent': 3,     # For pretty-printing JSON
#         'overwrite': False
#     },
# }
# settings.py

# Splash Server Endpoint
# SPLASH_URL = 'http://localhost:8050'


# Enable Splash downloader middleware and change HttpCompressionMiddleware priority
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }

# # Enable Splash Deduplicate Args Filter
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# Define the Splash DupeFilter
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


# SCRAPEOPS_API_KEY = 'c27266b3-dbaf-4d20-a992-d3ab02b34ce9'
# SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
# SCRAPEOPS_NUM_RESULTS = 150

DEFAULT_REQUEST_HEADERS = {
    "authority" : 'www.otodom.pl',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Windows; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    "sec-ch-ua-mobile": "?0",
    'sec-ch-ua-platform': '"macOS"',
    "sec-fetch-site": "none",
    "sec-fetch-mod": "",
    "sec-fetch-user": "?1",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "bg-BG,bg;q=0.9,en-US;q=0.8,en;q=0.7"
}

# ROTATING_PROXY_LIST_PATH = 'F:\Library\Engineering\computer science\Data Science\portfolio projects\Project 2 - SQL Data Analytics\Free_Proxy_List.txt'
# ROTATING_PROXY_LIST = [
# '130.193.123.34:5678',
# '45.112.125.51:4145',
# '192.252.216.81:4145',
# '104.16.108.42:80',
# '162.144.83.73:60468',
# '36.255.104.1:13623',
# '204.44.192.104:55070',
# '128.199.104.190:41354',
# '188.138.139.216:4145',
# '8.39.228.161:39593',
# '51.89.3.130:30444',
# '92.222.237.74:8888',
# '113.160.58.230:4145',
# '160.16.125.237:3030',
# '45.224.164.128:5678',
# '115.240.101.49:5678',
# '41.242.66.74:5678',
# '201.158.10.64:5678',
# '190.186.1.126:999',
# '175.29.174.242:10800',
# '195.16.78.236:1080',
# '45.112.125.58:4145',
# '132.148.165.102:22311',
# '124.6.225.124:1088',
# '122.146.95.183:4145',
# '178.79.165.164:5422',
# '103.66.233.177:4145',
# '80.240.254.145:4145',
# '202.6.225.92:1080',
# '116.99.231.154:24178',
# '194.44.166.65:1080',
# '185.169.181.25:4145',
# '172.67.38.96:80',
# '190.95.132.190:999',
# '45.174.79.101:999',
# '104.236.36.177:80',
# '96.36.50.99:39593',
# '202.159.35.25:443',
# '177.131.29.213:4153',
# '103.117.109.5:4153',
# '149.20.253.47:12551',
# '152.32.78.24:4145',
# '190.104.219.149:4153',
# '185.189.102.178:4153',
# '197.234.13.63:4145',
# '38.127.172.198:11537',
# '203.142.68.210:5678',
# '164.132.88.120:33089',
# '162.240.10.35:55018',
# '66.42.63.207:13802',
# '113.109.25.160:44844',
# '104.129.205.123:10792',
# '162.255.108.5:5678',
# '162.214.113.208:63389',
# '36.83.78.197:8080',
# '138.36.171.244:7497',

# ]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   "otodomScraper.middlewares.OtodomscraperSpiderMiddleware": 543,
    # 'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,

}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "otodomScraper.middlewares.OtodomscraperDownloaderMiddleware": 543,
   "otodomScraper.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400,
   # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
   # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,


}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "otodomScraper.pipelines.OtodomscraperPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
