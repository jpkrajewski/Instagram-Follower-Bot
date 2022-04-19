from instagram_automated_following import InstagramAutomatedFollowing as Iaf

CHROME_DRIVER_PATH = 'chrome driver path'
SIMILAR_ACCOUNT = 'ig account to follow all its followers'
USERNAME = 'login'
PASSWORD = 'password'

iaf = Iaf(CHROME_DRIVER_PATH)
iaf.login(USERNAME, PASSWORD)
iaf.find_followers(SIMILAR_ACCOUNT)
iaf.follow()
