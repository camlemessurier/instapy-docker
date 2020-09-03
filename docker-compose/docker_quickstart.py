from instapy import InstaPy
from instapy import smart_run

insta_username = 'boardwalksurfboards'
insta_password = 'Rfvtgb99$'

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=10000,
                                    max_following=10000,
                                    min_followers=30,
                                    min_following=30)
    session.set_user_interact(amount=1, randomize=False, percentage=55,
                              media='Photo')
    ##session.set_skip_users(skip_private=False)
    ## session.like_by_feed(amount=3, randomize=True, unfollow=True, interact=False)                    broken

    
    session.set_dont_unfollow_active_users(enabled=True, posts=80)
    session.set_action_delays(enabled=True, follow=1.5,  unfollow=2.2, randomize=True, random_range_from=70, random_range_to=140)
    session.set_quota_supervisor(enabled=True, peak_follows_daily=99, peak_follows_hourly=14, peak_unfollows_hourly=14, peak_unfollows_daily=99, sleep_after=["follows_h", "follows_d", "unfollows_d", "unfollows_h"], sleepyhead=True, stochastic_flow=True)

    # follow activity
    session.follow_user_followers(['shane.blue', 'eastendboardriders', 'sldsurfboards', 'dustnglass', 'nithup_photography', 'uonstudentcentral'],
                                  amount=28, randomize=True,
                                  interact=False, sleep_delay=240)

    # unfollow activity
    session.unfollow_users(amount=29, nonFollowers=True, style="RANDOM",
                           unfollow_after=99 * 60 * 60, sleep_delay=200)

    


    

   
