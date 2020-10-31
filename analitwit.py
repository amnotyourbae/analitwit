import tweepy
import pandas as pd

from toktok import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def ngulik(screen_name):
    print(f'------------------------------')
    print(f'Ngulik akun @{screen_name}... ')
    try:
        # get user twitter profile (tweet, likes, followers, following)
        user = api.get_user(screen_name)
    except TweepError as e:
        error_code = eval(str(e))[0]['code']
        if str(error_code) == '136':
            print('Stalking gagal. Sepertinya kamu di block, atau mungkin digembok')
            return None
        else:
            print ('try again someday')
    # desk
    description = user.description
    print('bionya ' + screen_name + ': ' + str(description))
    # followers
    followers_count = user.followers_count
    print('jumlah followers: ' + str(followers_count))
    # tweets
    statuses_count = user.statuses_count
    print('jumlah tweet: ' + str(statuses_count) + ' termasuk reply & retweet')
    # jumlah tweet yng likes
    favourites_count = user.favourites_count
    print('jumlah tweet yang di likes: ' + str(favourites_count))
    # get user fav account
    print(f'\nAkun sring di likes {screen_name}: ')
    favorites = api.favorites(screen_name, count= 50)
    all_favorites = []
    for status in favorites:
        text = status.user.screen_name
        text = " ".join(list(set(text.split())))
        all_favorites.append(text)

    df = pd.DataFrame(data=all_favorites, columns=['[akun]'])
    df = df.value_counts()
    dfl = df.head(10)
    print(dfl.to_string())

if __name__ == "__main__":
    screen_name = sys.argv[0]
    ngulik(screen_name)
