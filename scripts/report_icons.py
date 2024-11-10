# Icon Mappings Dictionary
# The icon_mappings dictionary is organized by category and is used to map categories and artifacts to icons.
# Please maintain the list in alphabetical order by category for ease of navigation and updating.
#
# To specify an icon for a particular artifact within a category, use the structure:
# 'CATEGORY': {'ARTIFACT': 'icon-name', ...}
# Example:
# 'CHROMIUM': {'BOOKMARKS': 'bookmark', 'DOWNLOADS': 'download', ...}
#
# To specify a default icon for all artifacts within a category or a single icon for the entire category, use:
# 'CATEGORY': 'icon-name' or 'CATEGORY': {'default': 'icon-name', ...}
# Example:
# 'ADDRESS BOOK': 'book-open'
#
# If a category or artifact does not have a specified icon, the 'alert-triangle' icon will be used as a fallback.
#
# Icons are sourced from Feather Icons (feathericons.com). When adding a new icon, ensure that the icon name
# matches the name listed on the Feather Icons website.
#
# The optional '_mode' key can be used to specify a search mode for finding matching artifacts within a category:
# 'CATEGORY': {'_mode': 'search', ...}
# In search mode, the function will attempt to find a partial match for the artifact name within the specified category.

icon_mappings = \
{
    'ACCESSORY DATA HYUNDAI': 'settings',
    'ACCOUNT': {
        'AUTH': 'key',
        'default': 'user',
        '_mode': 'search',
    },
    'ADB HOSTS': 'terminal',
    'ADDRESS BOOK': 'book-open',
    'ADIDAS-RUNNING': {
        'ACTIVITIES': 'activity',
        'GOALS': 'target',
        'USER': 'user',
        'default': 'user'
    },
    'AGGREGATE DICTIONARY': 'book',
    'AIRDROP DISCOVERABLE': 'search',
    'AIRDROP EMAILS': 'send',
    'AIRDROP NUMBERS': 'smartphone',
    'AIRDROP REAL NAMES': 'user',
    'AIRTAG DETECTION': 'alert-circle',
    'AIRTAGS': 'map-pin',
    'ALARMS': 'clock',
    'ALFA ROMEO CONTACTS': 'users',  # TODO: adjust artifact to share a category
    'ALFA ROMEO BLUETOOTH': 'bluetooth',
    'ALFA ROMEO SIRIUS DATA': 'settings',
    'ANDROID SYSTEM INTELLIGENCE': {
        'SIMPLESTORAGE': 'loader',
        'default': 'user'
    },
    'APP CONDUIT': 'activity',
    'APP INTERACTION': 'bar-chart-2',
    'APP PERMISSIONS': 'key',
    'APP ROLES': 'tool',
    'APP UPDATES': 'codepen',
    'APPLE MAIL': 'mail',
    'APPLE NOTES': 'book-open',
    'APPLE PODCASTS': 'play-circle',
    'APPLE WALLET': {
        'CARDS': 'credit-card',
        'PASSES': 'send',
        'TRANSACTIONS': 'dollar-sign',
        'default': 'credit-card',
    },
    'APPLICATIONS': 'grid',
    'AUDI TRIP': 'truck',
    'AUDIO UUIDS': 'smartphone',
    'BADOO': {
        'CHAT': 'message-circle',
        'CONNECTIONS': 'heart',
        'default': 'user'
    },
    'BASH HISTORY': 'terminal',
    'BIOME': 'eye',
    'BIOME AIRPLANE MODE': 'wifi-off',
    'BIOME APP INSTALL': 'eye',
    'BIOME BACKLIGHT': 'eye',
    'BIOME BATTERY PERC': 'eye',
    'BIOME BLUETOOTH': 'eye',
    'BIOME CARPLAY CONN': 'eye',
    'BIOME DEVICE PLUG': 'eye',
    'BIOME DEVICE WIFI': 'wifi',
    'BIOME HARDWARE': 'eye',
    'BIOME IN FOCUS': 'eye',
    'BIOME INTENTS': 'eye',
    'BIOME LOCATION ACT': 'eye',
    'BIOME NOTES': 'eye',
    'BIOME NOTIFICATIONS PUB': 'eye',
    'BIOME NOW PLAYING': 'eye',
    'BIOME SAFARI': 'eye',
    'BIOME SYNC': 'smartphone',
    'BIOME TEXT INPUT': 'eye',
    'BIOME USER ACT META': 'eye',
    'BIOME WIFI': 'eye',
    'BITTORRENT': 'share',
    'BLUETOOTH': 'bluetooth',
    'BLUETOOTH CONNECTIONS': 'bluetooth',
    'BLUETOOTH_DEVICES': 'bluetooth',  # TODO: can this be combined?
    'BOOKING.COM': {
            'ACCOUNT': 'user',
            'ACCOUNT SETTINGS': 'user',
            'PAYMENT METHODS': 'credit-card',
            'PAYMENT METHODS SETTINGS': 'credit-card',
            'VIEWED': 'eye',
            'RECENTLY SEARCHED': 'search',
            'WISH LISTS': 'star',
            'RECENTLY BOOKED': 'shopping-bag',
            'BOOKED': 'shopping-bag',
            'STORED DESTINATIONS': 'map',
            'NOTIFICATIONS': 'bell',
            'FLIGHTS SEARCHED': 'search',
            '_mode': 'search',
    },
    'BROWSER CACHE': {
        'CHROME BROWSER CACHE': 'chrome',
        'default': 'globe'
    },
    'BT REPORT': {
        'GPS DETAIL': 'map-pin',
        'BT CALL REPORT': 'bluetooth',
        'default': 'bluetooth',
    },
    'BUMBLE': {
        'BUMBLE - ACCOUNT DETAILS': 'user',
        'BUMBLE - MESSAGES': 'message-circle',
        'USER SETTINGS': 'user',
        'CHAT MESSAGES': 'message-circle',
        'MATCHES': 'smile',
    },
    'BURNER': {
        'ACCOUNTS': 'user',
        'CONTACTS': 'users',
        'NUMBERS': 'phone',
        'MESSAGES': 'message-circle',
        'default': 'user',
        '_mode': 'search',
    },
    'CACHE DATA': 'box',
    'CALCULATOR LOCKER': 'lock',
    'CALENDAR': {
        'CALENDAR BIRTHDAYS': 'gift',
        'default': 'calendar',
    },
    'CALL HISTORY': {
        'CALL HISTORY': 'phone-call',
        'DELETED VOICEMAIL': 'mic-off',
        'VOICEMAIL': 'mic',
        'default': 'phone',
    },
    'CALL LOGS': 'phone',
    'CAST': 'cast',
    'CARPLAY': 'package',
    'CASH APP': 'credit-card',
    'CELLULAR WIRELESS': 'bar-chart',
    'CHASE RETURNS': 'paperclip',
    'CHATS': 'message-circle',
    'CHATGPT': {
        'CONVERSATIONS METADATA': 'info',
        'CONVERSATIONS': 'message-circle',
        'ACCOUNT': 'user',
        'PREFERENCES' : 'sliders',
        'MEDIA UPLOADS' : 'image',
        'VOICE PROMPTS':'mic',
        '_mode': 'search',
    },
    'CHROMIUM': {
        'AUTOFILL': 'edit-3',
        'BOOKMARKS': 'bookmark',
        'DETECT INCIDENTAL PARTY STATE': 'skip-forward',
        'DOWNLOADS': 'download',
        'LOGIN': 'log-in',
        'MEDIA HISTORY': 'video',
        'NETWORK ACTION PREDICTOR': 'type',
        'OFFLINE PAGES': 'cloud-off',
        'SEARCH TERMS': 'search',
        'TOP SITES': 'list',
        'WEB VISITS': 'globe',
        'default': 'chrome',
        '_mode': 'search',
    },
    'CLIPBOARD': 'clipboard',
    'CLOUDKIT': {
        'NOTE SHARING': 'share-2',
        'PARTICIPANTS': 'user',
    },
    'COINBASE ARCHIVE': {
        '3RD': 'log-in',
        'CARD': 'credit-card',
        'PERSONAL': 'user',
        'SITE': 'activity',
        'TRANS': 'archive',
        'default': 'monitor',
    },
    'CONNECTED DEVICES': 'smartphone',
    'CONNECTED TO': 'zap',
    'CONTACTS': {
        'BLOCKED CONTACTS': 'user-x',
        'default': 'user',
    },
    'CONTACT_LIST': 'users',  # TODO: can this use another category?
    'CONTROL CENTER': {
        'CONTROL CENTER - ACTIVE CONTROLS': 'sliders',
        'CONTROL CENTER - DISABLED CONTROLS': 'x-square',
        'CONTROL CENTER - USER TOGGLED CONTROLS': 'check-square',
    },
    'CORE ACCESSORIES': {
        'ACCESSORYD': 'zap',
        'USER EVENT AGENT': 'activity',
    },
    'COREDUET': {
        'AIRPLANE MODE': 'pause',
        'LOCK STATE': 'lock',
        'PLUGGED IN': 'battery-charging',
    },
    'DAHUA TECHNOLOGY (DMSS)': {
        'CHANNELS': 'film',
        'DEVICES': 'tablet',
        'INFO': 'settings',
        'NOTIFICATIONS': 'bell',
        'PIN': 'unlock',
        'SENSORS': 'smartphone',
        'USER CREATED MEDIA': 'video',
        '_mode': 'search',
    },
    'DATA USAGE': 'wifi',
    'DEVICE DATA': 'file',
    'DEVICE HEALTH SERVICES': {
        'BLUETOOTH': 'bluetooth',
        'BATTERY': 'battery-charging',
        'default': 'bar-chart-2',
        '_mode': 'search'
    },
    'DEVICE INFO': {
        'BUILD INFO': 'terminal',
        'IOS SYSTEM VERSION': 'git-commit',
        'PARTNER SETTINGS': 'settings',
        'SETTINGS_SECURE_': 'settings',
        'default': 'info',
        '_mode': 'search',
    },
    'DHCP': 'settings',
    'DIAGNOSTIC_DATA': 'thermometer',
    'DIGITAL WELLBEING': {
        'ACCOUNT DATA': 'user',
        'default': 'layers',
        '_mode': 'search',
    },
    'DIGITAL WELLBEING ACCOUNT': {
        'ACCOUNT DATA': 'user',
        'default': 'layers',
        '_mode': 'search',
    },
    'DISCORD': {
        'DISCORD ACCOUNT': 'user',
        'DISCORD MANIFEST': 'file-text',
        'DISCORD MESSAGES': 'message-square',
    },
    'DISCORD CHATS': 'message-square',
    'DISCORD RETURNS': 'message-square',
    'DOWNLOADS': 'download',
    'DRAFT NATIVE MESSAGES': 'message-circle',
    'DUCKDUCKGO': {
        'DUCKDUCKGO TAB THUMBNAILS': 'image',
        'default': 'layers'
    },
    'EMULATED STORAGE METADATA': 'database',
    'ENCRYPTING MEDIA APPS': 'lock',
    'ETC HOSTS': 'globe',
    'FACEBOOK MESSENGER': {
        'CALLS': 'phone-call',
        'CHAT': 'message-circle',
        'CONTACTS': 'users',
        'default': 'facebook',
        '_mode': 'search',
    },
    'FACEBOOK - INSTAGRAM RETURNS': 'facebook',
    'FILES APP': 'file-text',
    'FILES BY GOOGLE': 'file',
    'FIREBASE CLOUD MESSAGING': 'database',
    'FIREFOX': {
        'BOOKMARKS': 'bookmark',
        'COOKIES': 'info',
        'DOWNLOADS': 'download',
        'FORM HISTORY': 'edit-3',
        'PERMISSIONS': 'sliders',
        'RECENTLY CLOSED TABS': 'x-square',
        'SEARCH TERMS': 'search',
        'TOP SITES': 'list',
        'VISITS': 'globe',
        'WEB HISTORY': 'globe',
        'default': 'firefox',
        '_mode': 'search',
    },
    'FITBIT': 'watch',
    'GALLERY TRASH': 'image',
    'GARMIN': {
        'DEVICES': 'watch',
        'NOTIFICATIONS': 'bell',
        'SLEEP': 'moon',
        'WEATHER': 'sun',
        'default': 'activity',
        '_mode': 'search',
    },
    'GARMIN-API': {
        'ACTIVITY API': 'watch',
        'DAILIES API': 'calendar',
        'HEART RATE API': 'heart',
        'STEPS API': 'arrow-up-circle',
        'SLEEP API': 'moon',
        'STRESS API': 'frown',
        'POLYLINE API': 'map-pin',
        'default': 'activity',
        '_mode': 'search',
    },
    'GARMIN-CACHE': {
        'ACTIVITIES': 'watch',
        'CHARTS': 'activity',
        'DAILIES': 'calendar',
        'POLYLINE': 'map-pin',
        'RESPONSE': 'terminal',
        'SPO2': 'heart',
        'SLEEP': 'moon',
        'WEIGHT': 'bar-chart-2',
        'default': 'activity',
        '_mode': 'search',
    },
    'GARMIN-FILES': {
        'LOG': 'file-text',
        'PERSISTENT': 'code',
        '_mode': 'search',
    },
    'GARMIN-GCM': {
        'ACTIVITIES': 'watch',
        'JSON': 'code',
        '_mode': 'search',
    },
    'GARMIN-NOTIFICATIONS': 'message-square',
    'GARMIN-SHAREDPREFS': {
        'FACEBOOK': 'facebook',
        'USER': 'user',
        '_mode': 'search',
    },
    'GARMIN-SYNC': 'loader',
    'GEO LOCATION': 'map-pin',
    'GEOLOCATION': {
        'APPLICATIONS': 'grid',
        'MAP TILE CACHE': 'map',
        'MAPSSYNC': 'map',
        'PD PLACE CACHE': 'map-pin',
        'default': 'map-pin',
    },
    'GMAIL': {
        'GMAIL - LABEL DETAILS': 'mail',
        'GMAIL - OFFLINE SEARCH': 'search',
        'ACTIVE': 'at-sign',
        'APP EMAILS': 'at-sign',
        'DOWNLOAD REQUESTS': 'download-cloud',
        'LABEL DETAILS': 'mail',
        '_mode': 'search',
    },
    'GOOGLE CALL SCREEN': 'phone-incoming',
    'GOOGLE CHAT': {
        'GROUP INFORMATION': 'users',
        'MESSAGES': 'message-circle',
        'DRAFTS': 'edit-3',
        'USERS': 'users',
        'default': 'message-circle',
        '_mode': 'search',
    },
    'GOOGLE DRIVE': 'file',
    'GOOGLE DUO': {
        'GOOGLE DUO - CALL HISTORY': 'phone-call',
        'GOOGLE DUO - CLIPS': 'video',
        'GOOGLE DUO - CONTACTS': 'user',
        'CALL HISTORY': 'phone-call',
        'CONTACTS': 'users',
        'NOTES': 'edit-3',
        '_mode': 'search',
    },
    'GOOGLE FIT (GMS)': 'activity',
    'GOOGLE KEEP': 'list',
    'GBOARD KEYBOARD': {
        'CLIPBOARD': 'clipboard',
        '_mode': 'search',
    },
    'GOOGLE MAPS VOICE GUIDANCE': 'map',
    'GOOGLE MAPS TEMP VOICE GUIDANCE': 'map',
    'GOOGLE MESSAGES': 'message-circle',
    'GOOGLE NOW & QUICKSEARCH': 'search',
    'GOOGLE PHOTOS': {
        'LOCAL TRASH': 'trash-2',
        'BACKED UP FOLDER': 'refresh-cw',
        '_mode': 'search',
    },
    'GOOGLE PLAY': {
        'GOOGLE PLAY SEARCHES': 'search',
        'default': 'play',
        '_mode': 'search',
    },
    'GOOGLE RETURNS': {
        'GOOGLE RETURNS - ACTIVITIES': 'activity',
        'default': 'chrome'
    },
    'GOOGLE RETURNS MBOXES': 'mail',
    'GOOGLE RETURNS SUBSCRIBER INFO': 'user',
    'GOOGLE RETURNS PLAY USER ACT': 'smartphone',
    'GOOGLE RETURNS ANDROID DEVICE CONFIG': 'smartphone',
    'GOOGLE RETURNS MY ACTIVITY IMAGE SEARCH': 'search',
    'GOOGLE RETURNS MY ACTIVITY SEARCH': 'search',
    'GOOGLE RETURNS YOUTUBE SUBS INFO': 'search',
    'GOOGLE RETURNS ACCOUNT TARGET ASSOC. PHONE': 'target',
    'GOOGLE RETURNS ACCOUNT TARGET ASSOC. COOKIES': 'target',
    'GOOGLE RETURNS GOOGLE PLAY STORE DEVICES': 'tablet',
    'GOOGLE RETURNS GOOGLE PLAY INSTALLS': 'shield',
    'GOOGLE RETURNS GOOGLE PLAY LIBRARY': 'book-open',
    'GOOGLE RETURNS GOOGLE PLAY USER REVIEWS': 'book-open',
    'GOOGLE TAKEOUT ARCHIVE': {
        'CHROME WEB HISTORY': 'chrome',
        'CHROME ARC PACKAGES': 'package',
        'CHROME AUTOFILL': 'edit-3',
        'CHROME BOOKMARKS': 'star',
        'CHROME DEVICE INFO': 'chrome',
        'CHROME EXTENSIONS': 'tool',
        'CHROME OS SETTINGS': 'settings',
        'CHROME READING LIST': 'book',
        'CHROME SEARCH ENGINES': 'search',
        'CHROME OMNIBOX': 'search',
        'FITBIT ACCOUNT PROFILE': 'user',
        'FITBIT ACTIVITY GOALS': 'check-circle',
        'FITBIT COMPUTED TEMPERATURE': 'thermometer',
        'FITBIT OXYGEN SATURATION': 'droplet',
        'FITBIT SLEEP': 'moon',
        'FITBIT STRESS': 'activity',
        'FITBIT TRACKERS': 'watch',
        'GOOGLE ACCESS LOG ACTIVITIES': 'activity',
        'GOOGLE ACCESS LOG DEVICES': 'smartphone',
        'GOOGLE CHAT - MESSAGES': 'message-square',
        'GOOGLE FI - USER INFO RECORDS': 'phone',
        'GOOGLE FIT - DAILY ACTIVITY METRICS': 'trending-up',
        'GOOGLE LOCATION HISTORY - LOCATION HISTORY': 'map-pin',
        'GOOGLE PAY TRANSACTIONS': 'credit-card',
        'GOOGLE PLAY STORE DEVICES': 'smartphone',
        'GOOGLE PLAY STORE INSTALLS': 'box',
        'GOOGLE PLAY STORE LIBRARY': 'grid',
        'GOOGLE PLAY STORE PURCHASE HISTORY': 'shopping-cart',
        'GOOGLE PLAY STORE REVIEWS': 'edit-3',
        'GOOGLE PLAY STORE SUBSCRIPTIONS': 'refresh-cw',
        'GOOGLE PROFILE': 'user',
        'GOOGLE SEMANTIC LOCATION HISTORY - PLACE VISITS': 'map-pin',
        'GOOGLE SEMANTIC LOCATION HISTORY - ACTIVITY SEGMENTS': 'activity',
        'GOOGLE TASKS': 'check-circle',
        'MBOX': 'mail',
        'SAVED LINKS - DEFAULT LIST': 'list',
        'SAVED LINKS - FAVORITE IMAGES': 'image',
        'SAVED LINKS - FAVORITE PAGES': 'link-2',
        'SAVED LINKS - WANT TO GO': 'navigation-2',
        'YOUTUBE SUBSCRIPTIONS': 'youtube',
        'default': 'user'
    },
    'GOOGLE TAKEOUT SEMANTIC LOCATIONS BY MONTH': 'map-pin',
    'GOOGLE TASKS': 'list',
    'GOOGLE TRANSLATE': {
        'HISTORY': 'type',
        'FAVORITE TRANSLATIONS': 'star',
        'TEXT-TO-SPEECH': 'volume-2',
        '_mode': 'search',
    },
    'GPS_DATA': 'map-pin',
    'GROUPME': {
        'GROUP INFORMATION': 'users',
        'CHAT INFORMATION': 'message-circle',
        '_mode': 'search',
    },
    'HEALTH': {
        'DEFAULT': 'heart',
        'HEALTH - ACHIEVEMENTS': 'star',
        'HEALTH - HEADPHONE AUDIO LEVELS': 'headphones',
        'HEALTH - HEART RATE': 'activity',
        'HEALTH - RESTING HEART RATE': 'activity',
        'HEALTH - STEPS': 'activity',
        'HEALTH - WORKOUTS': 'activity',
    },
    'HEALTH & FITNESS': {
        'ALLTRAILS - TRAIL DETAILS': 'map',
        'ALLTRAILS - USER INFO': 'user',
    },
    'HIDEX': 'eye-off',
    'HIKVISION': {
        'CCTV ACTIVITY': 'activity',
        'CCTV CHANNELS': 'film',
        'CCTV INFO': 'settings',
        'USER CREATED MEDIA': 'video',
        '_mode': 'search',
    },
    'ICLOUD DOCUMENTS FOLDERS': 'book-open',
    'ICLOUD QUICK LOOK': 'file',
    'ICLOUD RETURNS': {
        'ICLOUD - ACCOUNT FEATURES': 'user',
        'default': 'cloud'
    },
    'ICLOUD SHARED ALBUMS': 'cloud',
    'IDENTIFIERS': {
        'IOS MESSAGE RETENTION': 'message-circle',
        'PREFERENCES PLIST': 'settings',
        'default': 'file',
    },
    'IDENTITY LOOKUP SERVICE': 'user-check',
    'IMAGE CACHEV0': 'image',
    'IMAGE MANAGER CACHE': 'image',
    'IMO': {
        'IMO - ACCOUNT ID': 'user',
        'IMO - MESSAGES': 'message-square',
    },
    'IMO HD CHAT': {
        'IMO HD CHAT - CONTACTS': 'user',
        'IMO HD CHAT - MESSAGES': 'message-circle',
    },
    'INSTAGRAM': {
        'INSTAGRAM THREADS': 'message-square',
        'INSTAGRAM THREADS CALLS': 'phone',
    },
    'INSTAGRAM ARCHIVE': {
        'INSTAGRAM ARCHIVE - ACCOUNT INFO': 'user',
        'INSTAGRAM ARCHIVE - PERSONAL INFO': 'user',
        'default': 'instagram'
    },
    'INSTALLED APPS': 'package',
    'INTENTS': 'command',
    'INTERACTIONC': {
        'ATTACHMENTS': 'paperclip',
        'CONTACTS': 'user',
    },
    'IOS ATXDATASTORE': 'database',
    'IOS BUILD': 'git-commit',
    'IOS BUILD (ITUNES BACKUP)': 'git-commit',
    'IOS SCREENS': 'maximize',
    'KEYBOARD': {
        'KEYBOARD APPLICATION USAGE': 'type',
        'KEYBOARD DYNAMIC LEXICON': 'type',
        'default': 'type',
    },
    'KIK': {
        'KIK GROUP ADMINISTRATORS': 'user-plus',
        'KIK LOCAL ACCOUNT': 'user-check',
        'KIK MEDIA METADATA': 'file-plus',
        'KIK MESSAGES': 'message-square',
        'KIK PENDING UPLOADS': 'upload',
        'KIK USERS': 'user',
        'KIK USERS IN GROUPS': 'user',
    },
    'KIK RETURNS': {
        'KIK - PROFILE PIC': 'image',
        'default': 'file-text'
    },
    'KNOWLEDGEC': {
        'KNOWLEDGEC - BATTERY PERCENTAGE': 'battery',
        'KNOWLEDGEC DEVICE LOCKED': 'lock',
        'KNOWLEDGEC - MEDIA PLAYING': 'play-circle',
        'KNOWLEDGEC - DEVICE PLUGIN STATUS': 'battery-charging',
        'KNOWLEDGEC - DO NOT DISTURB': 'moon',
        'default': 'activity',
    },
    'LEAPP_REPORT': {
        'default': 'git-commit',
        '_mode': 'search',
    },
    'LIBRE TORRENT': 'download',
    'LINE': {
        'LINE - CONTACTS': 'user',
        'LINE - MESSAGES': 'message-square',
        'LINE - CALL LOGS': 'phone',
    },
    'LINKEDIN' : {
        'LINKEDIN - ACCOUNT': 'user',
        'LINKEDIN - MESSAGES': 'message-square',
        'LINKEDIN - CONVERSATIONS': 'message-circle'
    },
    'LIFE360': {
        'LIFE360 - CHAT MESSAGES': 'message-circle',
        'LIFE360 - DEVICE BATTERY': 'battery',
        'LIFE360 - LOCATIONS': 'map-pin',
        'LIFE360 - MEMBERS': 'users',
    },
    'LOCATION SERVICES CONFIGURATIONS': 'settings',
    'LOCATIONS': {
        'APPLE MAPS SEARCH HISTORY': 'search',
        'default': 'map-pin',
    },
    'MAP-MY-WALK': {
        'ACTIVITIES': 'map',
        'USER': 'user',
        '_mode': 'search',
    },
    'MASTODON': {
        'ACCOUNT DETAILS': 'user',
        'ACCOUNT SEARCHES': 'users',
        'HASHTAG SEARCHES': 'hash',
        'INSTANCE DETAILS': 'info',
        'NOTIFICATIONS': 'bell',
        'TIMELINE': 'activity',
        '_mode': 'search',
    },
    'MEDIA LIBRARY': 'play-circle',
    'MEDIA METADATA': 'file-plus',
    'MEDICAL ID': 'thermometer',
    'MEGA': 'message-circle',
    'METAMASK': {
        'BROWSER': 'globe',
        'CONTACTS': 'users',
        '_mode': 'search',
    },
    'MEWE': 'message-circle',
    'MICROSOFT RETURNS': 'target',
    'MICROSOFT TEAMS': {
        'TEAMS CALL LOGS': 'phone',
        'TEAMS CONTACT': 'users',
        'TEAMS MESSAGES': 'message-square',
        'TEAMS SHARED LOCATIONS': 'map-pin',
        'TEAMS USER': 'user',
    },
    'MICROSOFT TEAMS - LOGS': {
        'TEAMS LOCATIONS': 'map-pin',
        'TEAMS MOTION': 'move',
        'TEAMS POWER LOG': 'battery-charging',
        'TEAMS STATE CHANGE': 'truck',
        'TEAMS TIMEZONE': 'clock',
    },
    'MOBILE ACTIVATION LOGS': 'clipboard',
    'MOBILE BACKUP PLIST': 'settings',
    'MOBILE CONTAINER MANAGER': 'save',
    'MOBILE INSTALLATION LOGS': 'clipboard',
    'MOBILE SOFTWARE UPDATE': 'refresh-cw',
    'MY FILES': {
        'MY FILES DB - CACHE MEDIA': 'image',
        '_mode': 'search',
    },
    'NETFLIX ARCHIVE': {
        'NETFLIX - BILLING HISTORY': 'credit-card',
        'NETFLIX - PROFILES': 'users',
        'NETFLIX - IP ADDRESS LOGIN': 'log-in',
        'NETFLIX - ACCOUNT DETAILS': 'users',
        'NETFLIX - MESSAGES SENT BY NETFLIX': 'mail',
        'NETFLIX - SEARCH HISTORY': 'search',
        'default': 'tv'
    },
    'NETWORK USAGE': {
        'APP_DATA': 'activity',
        'CONNECTIONS': 'bar-chart',
        'default': 'send',
        '_mode': 'search',
    },
    'NIKE-RUN': {
        'ACTIVITIES': 'watch',
        'ACTIVITY ROUTE': 'map-pin',
        'ACTIVITY MOMENTS': 'list',
        'NOTIFICATIONS': 'bell',
        '_mode': 'search',
    },
    'NOTES': 'file-text',
    'NOTIFICATIONS': 'bell',
    'NOW PLAYING': 'music',
    'OFFLINE PAGES': 'cloud-off',
    'OOPS': 'message-square',
    'PACKAGE PREDICTIONS': 'package',
    'PAS_DEBUG': {
        'SEND GPS CAN DATA': 'map-pin',
        'DEV LOC RESULTS': 'map-pin',
        'ROAD SPEED LIMITS': 'target',
        'ACCESS POINT LIST': 'wifi',
        'VEHICLE SPEED': 'trending-up',
        'TRANSMISSION STATUS': 'corner-up-right',
        'OUTSIDE TEMPERATURE': 'thermometer',
        'ODOMETER': 'plus-circle',
        'default': 'archive',
    },
    'PERMISSIONS': 'check',
    'PHONE BOOK DB': 'smartphone',
    'PHONE CONFIG': 'smartphone',
    'PHOTOS': {
        'MIGRATIONS': 'chevrons-up',
        'default': 'image',
    },
    'PHOTOS.SQLITE-A-ASSET_BASIC_DATA': {
        'PH1.1-ASSET BASIC DATA-PHDAPSQL': 'image',
        'PH2.1-ASSET BASIC DATA & GENALBUM DATA-PHDAPSQL': 'image',
    },
    'PHOTOS.SQLITE-B-INTERACTION_ARTIFACTS': {
        'PH3.1-TRASHED RECENTLY DELETED-PHDAPSQL': 'trash-2',
        'PH4-HIDDEN-PHDAPSQL': 'eye-off',
        'PH6-VIEWED AND PLAYED DATA-PHDAPSQL': 'eye',
        'PH7-FAVORITE-PHDAPSQL': 'heart',
        'PH8-HAS ADJUSTMENT-PHDAPSQL': 'edit',
        'PH11-KWRDSCAPSTITLESDESCRIPSLIKESBASICASSTDATA-PHDAPSQL': 'info',
    },
    'PHOTOS.SQLITE-C-OTHER_ARTIFACTS': {
        'PH5.1-HAS LOCATIONS-PHDAPSQL': 'map-pin',
        'PH9-BURST AVALANCHE-PHDAPSQL': 'layers',
        'PH10.1-ASSETS HAVE EMBEDDED FILES-PHDAPSQL': 'file-plus',
        'PH26.1-SYNDICATION ID ASSETS-PHDAPSQL': 'refresh-ccw',
    },
    'PHOTOS.SQLITE-D-GENERIC_ALBUM_RECORDS-NAD': {
        'PH20.1-ALBUM RECORDS NAD-PHDAPSQL': 'book',
        'PH21-NON-SHARED ALBUM RECORDS NAD-PHDAPSQL': 'book',
        'PH23-SHARED ALBUM RECORDS NAD-PHDAPSQL': 'upload-cloud',
        'PH25.1-SWY CONVERSATION RECORDS NAD-PHDAPSQL': 'message-square',
    },
    'PHOTOS.SQLITE-E-ASSET_IN_ALBUMS': {
        'PH22-ASSETS IN NON-SHARED ALBUMS-PHDAPSQL': 'book-open',
        'PH24-ASSETS IN SHARED ALBUMS-PHDAPSQL': 'upload-cloud',
    },
    'PHOTOS.SQLITE-F-CLOUD_SHARED_METHODS': {
        'PH30-ICLD SHARE METHODS NAD-PHDAPSQL': 'upload-cloud',
        'PH31-ICLD SHARED PHOTO LIB RECORDS NAD-PHDAPSQL': 'upload-cloud',
        'PH32-ICLD SHARED PHOTO LIB ASSETS-PHDAPSQL': 'upload-cloud',
        'PH33-ICLD SPL ASSETS FROM OTHER CONTRIB-PHDAPSQL': 'download-cloud',
        'PH34-ICLD SHARED LINK RECORDS NAD-PHDAPSQL': 'link',
        'PH35-ICLD SHARED LINK ASSETS-PHDAPSQL': 'link',
    },
    'PHOTOS.SQLITE-G-PEOPLE_FACES_DATA': {
        'PH15.1-PEOPLE & FACES NAD-PHDAPSQL': 'smile',
        'PH16.1-PEOPLE & FACES ASSET DATA-PHDAPSQL': 'smile',
    },
    'PHOTOS.SQLITE-H-POSSIBLE_USER_ADJUSTED_DATA': {
        'PH70.1-POSSIBLE_ADJUST_DATE-TIMEZONE-LOCATION-PHDAPSQL': 'edit',
        'PH71.1-POSSIBLE_ADJUST_DATE-TIMEZONE-PHDAPSQL': 'edit',
        'PH72.1-POSSIBLE_ADJUST_DATE-LOCATION-PHDAPSQL': 'edit',
        'PH73.1-POSSIBLE_ADJUST_DATE-PHDAPSQL': 'edit',
        'PH74.1-POSSIBLE_ADJUST_TIMEZONE-LOCATION-PHDAPSQL': 'edit',
        'PH75.1-POSSIBLE_ADJUST_TIMEZONE-PHDAPSQL': 'edit',
        'PH76.1-POSSIBLE_ADJUST_LOCATION-PHDAPSQL': 'edit',
    },
    'PHOTOS.SQLITE-I-ASSET_INTRESOU-OPTIMIZATION': {
        'PH50.1-ASSET_INTRESOU-PHDAPSQL': 'database',
        'PH51-POSSIBLE_OPTIMIZED_ASSETS_INTRESOU-PHDAPSQL': 'upload-cloud',
    },
    'PHOTOS.SQLITE-R-REFERENCE_FOR_ASSET_ANALYSIS': {
        'PH94.1-IOS14_REF_FOR_ASSET_ANALYSIS-PHDAPSQL': 'database',
        'PH94.2-IOS14_REF_FOR_ASSET_ANALYSIS-SYNDPL': 'database',
        'PH95.1-IOS15_REF_FOR_ASSET_ANALYSIS-PHDAPSQL': 'database',
        'PH95.2-IOS15_REF_FOR_ASSET_ANALYSIS-SYNDPL': 'database',
        'PH96.1-IOS16_REF_FOR_ASSET_ANALYSIS-PHDAPSQL': 'database',
        'PH96.2-IOS16_REF_FOR_ASSET_ANALYSIS-SYNDPL': 'database',
        'PH97.1-IOS17_REF_FOR_ASSET_ANALYSIS-PHDAPSQL': 'database',
        'PH97.2-IOS17_REF_FOR_ASSET_ANALYSIS-SYNDPL': 'database',
        'PH98.1-IOS18_REF_FOR_ASSET_ANALYSIS-PHDAPSQL': 'database',
        'PH98.2-IOS18_REF_FOR_ASSET_ANALYSIS-SYNDPL': 'database',
    },
    'PHOTOS.SQLITE-S-SYNDICATION_PL_ARTIFACTS': {
        'PH1.2-ASSET BASIC DATA-SYNDPL': 'image',
        'PH2.2-ASSET BASIC DATA & CONVERS DATA-SYNDPL': 'image',
        'PH3.2-REMOVED FROM CAMERA ROLL-SYNDPL': 'delete',
        'PH5.2-HAS LOCATIONS-SYNDPL': 'map-pin',
        'PH10.2-ASSETS HAVE EMBEDDED FILES-SYNDPL': 'file-plus',
        'PH15.2-PEOPLE & FACES NAD-SYNDPL': 'smile',
        'PH16.2-PEOPLE & FACES ASSET DATA-SYNDPL': 'smile',
        'PH20.2-ALBUM RECORDS NAD-SYNDPL': 'book',
        'PH25.2-SWY CONVERSATION RECORDS NAD-SYNDPL': 'message-square',
        'PH26.2-SYNDICATION PL ASSETS-SYNDPL': 'message-square',
        'PH50.2-ASSET_INTRESOU-SYNDPL': 'database',
    },
    'PHOTOS-Z-SETTINGS': {
        'PH80-COM-APPLE-MOBILESLIDESHOW-PLIST': 'settings',
        'PH81-COM-APPLE-CAMERA-PLIST': 'settings',
        'PH82-COM-APPLE-MEDIAANALYSISD-PLIST': 'book',
        'PH83-COM-APPLE-PURPLEBUDDY-PLIST': 'settings',
        'PH84-CAMERA-SMART-SHARING-METADATA-PLIST': 'camera',
        'PH85-ACCOUNTSD-CLOUD-SERVICE-ENABLE-LOG-PLIST': 'settings',
        'PH86-ASSETSD-CLOUD-SERVICE-ENABLE-LOG-PLIST': 'settings',
        'PH99-SYSTEM-VERSION-PLIST': 'settings',
        'PH100-UFED-DEVICE-VALUES-PLIST': 'settings',
    },
    'PIKPAK': 'cloud',
    'PINGER': {
        'PINGER - CDR': 'phone',
        'PINGER - DML': 'phone',
        'PINGER - IP': 'monitor',
        'PINGER - MESSAGES': 'message-square',
        'PINGER - ACCOUNT': 'user',
        'default': 'phone'
    },
    'PLAYGROUND VAULT': 'lock',
    'PODCAST ADDICT': 'music',
    'POWER EVENTS': {
        'POWER OFF RESET': 'power',
        'LAST BOOT TIME': 'power',
        'SHUTDOWN CHECKPOINTS': 'power',
        '_mode': 'search',
    },
    'POWERLOG': 'power',
    'POWERLOG BACKUPS': 'power',
    'PRIVACY DASHBOARD': 'eye',
    'PROTON MAIL': 'mail',
    'PROTONMAIL': {
        'CONTACTS': 'users',
        'MESSAGES': 'inbox',
        '_mode': 'search',
    },
    'PROTONVPN': 'shield',
    'PUMA-TRAC': {
        'ACTIVITIES': 'watch',
        'USER': 'user',
        '_mode': 'search',
    },
    'RAR LAB PREFS': 'settings',
    'RCS CHATS': 'message-circle',
    'RECENT ACTIVITY': 'activity',
    'REDDIT RETURNS': 'chevrons-up',
    'REMINDERS': 'list',
    'ROUTINED': 'map',
    'RUNKEEPER': {
        'ACTIVITIES': 'watch',
        'USER': 'user',
        '_mode': 'search',
    },
    'SAFARI BROWSER': 'compass',
    'SAMSUNG SMARTTHINGS': 'bluetooth',
    'SAMSUNG WEATHER CLOCK': {
        'DAILY': 'sunrise',
        'HOURLY': 'thermometer',
        '_mode': 'search',
    },
    'SAMSUNG_CMH': 'disc',
    'SCREENTIME': 'monitor',
    'SCRIPT LOGS': 'archive',
    'SECRET CALCULATOR PHOTO ALBUM': 'image',
    'SETTINGS SERVICES': 'battery-charging',
    'SIM INFO': 'info',
    'SKOUT': {
        'SKOUT MESSAGES': 'message-circle',
        'SKOUT USERS': 'users',
    },
    'SKYPE': {
        'SKYPE - CALL LOGS': 'phone',
        'SKYPE - MESSAGES': 'message-square',
        'SKYPE - CONTACTS': 'user',
    },
    'SLACK': {
        'SLACK ATTACHMENTS': 'paperclip',
        'SLACK CHANNEL DATA': 'slack',
        'SLACK MESSAGES': 'message-square',
        'SLACK TEAM DATA': 'slack',
        'SLACK USER DATA': 'user',
        'SLACK WORKSPACE DATA': 'slack',
    },
    'SLOPES': {
        'SLOPES - ACTIONS': 'trending-down',
        'SLOPES - LIFT DETAILS': 'shuffle',
        'SLOPES - RESORT DETAILS': 'home',
    },
    'SMS & IMESSAGE': 'message-square',
    'SMS & MMS': 'message-square',
    'SNAPCHAT': 'bell',
    'SNAPCHAT ARCHIVE': 'camera',
    'SNAPCHAT RETURNS': 'camera',
    'SPLITWISE': {
        'SPLITWISE - EXPENSES': 'dollar-sign',
        'SPLITWISE - EXPENSE BALANCES': 'dollar-sign',
        'SPLITWISE - GROUPS': 'users',
        'SPLITWISE - NOTIFICATIONS': 'bell',
        'SPLITWISE - TOTAL BALANCES': 'dollar-sign',
        'SPLITWISE - USERS': 'user',
    },
    'SQLITE JOURNALING': 'book-open',
    'STRAVA': 'map',
    'SYNCED DEVICES': 'refresh-cw',
    'SYSDIAGNOSE': {
        'SYSDIAGNOSE - SHUTDOWN LOG PROCESSES': 'loader',
        'SYSDIAGNOSE - SHUTDOWN LOG REBOOTS': 'refresh-cw',
    },
    'TEAMS': {  # TODO: align I & A artifacts since theres a 'microsoft teams' also
        'TEAMS MESSAGES': 'message-circle',
        'TEAMS USERS': 'users',
        'TEAMS CALL LOG': 'phone',
        'TEAMS ACTIVITY FEED': 'at-sign',
        'TEAMS FILE INFO': 'file',
        'default': 'file-text',
    },
    'TANGO': 'message-square',
    'TELEGRAM': 'message-square',
    'TELEGUARD': {
        'TELEGUARD CONTACTS': 'users',
        'TELEGUARD MESSAGES': 'message-square',
        'TELEGUARD POSTS': 'at-sign',
        'TELEGUARD CHANNELS': 'home',
    },
    'TELEMATICS': {
        'GPS DETAIL': 'map-pin',
        'WDWSTATUS REPORT': 'map-pin',
        '_mode': 'search',
    },
    'TEXT INPUT MESSAGES': 'message-square',
    'TEXT NOW': {
        'TEXT NOW - CALL LOGS': 'phone',
        'TEXT NOW - MESSAGES': 'message-square',
        'TEXT NOW - CONTACTS': 'user',
    },
    'TIKTOK': {  # TODO: align I & A artifacts with each other
        'TIKTOK CONTACTS': 'user',
        'TIKTOK MESSAGES': 'message-square',
        'TIKTOK SEARCH': 'search',
        'TIKTOK - MESSAGES': 'message-square',
        'TIKTOK - CONTACTS': 'user',
        'TIKTOK REFERENCED REPLIED': 'message-square',
        '_mode': 'search'

    },
    'TIKTOK RETURNS': 'film',
    'TODOIST': {
        'ITEMS': 'list',
        'NOTES': 'file-text',
        'PROJECTS': 'folder',
        '_mode': 'search',
    },
    'TOR': 'globe',
    'TORRENT DATA': 'download',
    'TUSKY': {
        'TIMELINE': 'activity',
        'ACCOUNT': 'user',
        '_mode': 'search',
    },
    'TWITTER': 'twitter',
    'TWITTER RETURNS': 'twitter',
    'USAGE STATS': 'bar-chart-2',
    'USER DICTIONARY': 'book',
    'VEHICLE INFO': 'truck',
    'VENMO': 'dollar-sign',
    'VERIZON RDD ANALYTICS': {
        'VERIZON RDD - BATTERY HISTORY': 'power',
        'VERIZON RDD - WIFI DATA': 'wifi',
    },
    'UBER': {
            'UBER APP LOCATION DATA': 'map-pin',
            'default': 'move',
    },
    'VIBER': {
        'VIBER - CALL REMNANTS': 'phone-call',
        'VIBER - CHATS': 'message-square',
        'VIBER - CONTACTS': 'users',
        'VIBER - SETTINGS': 'settings',
        'VIBER - MESSAGES': 'message-square',
        'VIBER - CALL LOGS': 'phone',
    },
    'VIPPS': {
        'VIPPS CONTACTS': 'users',
        'default': 'dollar-sign',
    },
    'VLC': {
        'VLC MEDIA LIST': 'film',
        'VLC THUMBNAILS': 'image',
    },
    'VLC THUMBS': {
        'VLC MEDIA LIB': 'film',
        'VLC THUMBNAILS': 'image',
        'VLC THUMBNAIL DATA': 'image',
        'default': 'image',
    },
    'VOICE-RECORDINGS': 'mic',
    'VOICE-TRIGGERS': 'mic',
    'WAZE': 'navigation-2',
    'WHATSAPP': {  # TODO: I don't think search mode is required
        'WHATSAPP - CONTACTS': 'users',
        'WHATSAPP - MESSAGES': 'message-square',
        'WHATSAPP - ONE TO ONE MESSAGES': 'message-circle',
        'WHATSAPP - GROUP MESSAGES': 'message-circle',
        'WHATSAPP - CALL LOGS': 'phone',
        'WHATSAPP - GROUP DETAILS': 'users',
        'default': 'user',
        '_mode': 'search',
    },
    'WHATSAPP EXPORTED CHAT': 'message-circle',
    'WITHINGS HEALTH MATE' : {
        'WITHINGS HEALTH MATE - ACCOUNTS': 'user',
        'WITHINGS HEALTH MATE - MESSAGES': 'message-square',
        'WITHINGS HEALTH MATE - DEVICES': 'watch',
        'WITHINGS HEALTH MATE - TRACKED ACTIVITIES': 'activity',
        'WITHINGS HEALTH MATE - DAILY SUMMARY': 'activity',
        'WITHINGS HEALTH MATE - MEASUREMENTS': 'activity',
    },
    'WIFI CONNECTIONS': 'wifi',
    'WIFI KNOWN NETWORKS': 'wifi',
    'WIFI PROFILES': 'wifi',
    'WIPE & SETUP': {
        'FACTORY RESET': 'loader',
        'SUGGESTIONS.XML': 'loader',
        'SETUP_WIZARD_INFO.XML': 'loader',
        'APPOPS.XML': 'loader',
        'SAMSUNG WIPE HISTORY': 'trash-2',
        'SAMSUNG WIPE RECOVERY HISTORY LOG': 'trash-2',
        'default': 'loader',
    },
}

# function that can be run against the list to sort and output to console
def sort_and_print_mappings():
    sorted_keys = sorted(icon_mappings.keys(), key=lambda x: x.lower())
    sorted_dict = {key: icon_mappings[key] for key in sorted_keys}

    print("{")
    for category, mappings in sorted_dict.items():
        if isinstance(mappings, dict):
            print(f"    '{category}': {{")
            # Sort the artifacts, with 'default' and '_mode' at the end
            sorted_artifacts = sorted(
                [(k, v) for k, v in mappings.items() if k not in ['default', '_mode']],
                key=lambda x: x[0]
            )
            # Append 'default' and '_mode' at the end if they exist
            if 'default' in mappings:
                sorted_artifacts.append(('default', mappings['default']))
            if '_mode' in mappings:
                sorted_artifacts.append(('_mode', mappings['_mode']))
            for artifact, icon in sorted_artifacts:
                print(f"        '{artifact}': '{icon}',")
            print("    },")
        else:
            print(f"    '{category}': '{mappings}',")
    print("}")


if __name__ == '__main__':
    # Call the function to print the sorted mappings to the console
    sort_and_print_mappings()