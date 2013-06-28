import p2p
import random
connection = p2p.get_connection()

def make_random_content():
  random_slug = "chi-ugc-relatedphoto-andre-bellos-interview%s-2013-06-24" % random.random()

  test_json = {"content_item_type_code": "photo", "display_time": "2013-06-24T19:15:53Z", "content_item_state_code": "live", "title": "Andre Bellos interview", "credit": "Posted By Andre Bellos, <a href='http://community.chicagotribune.com/'>Community  Contributor</a>", "caption": "Hollywood fun=)", "photo_upload": {"alt_thumbnail": {"url": "https://www.filepicker.io/api/file/JoypBj9YTyeL0UtXwARm?dl=false"}}, "product_affiliate_code": "chinews", "source_code": "chicagotribuneugc", "slug": random_slug} 

  return test_json

print "About to hit p2p API with photo json"
random_content = make_random_content()
resp = connection.create_content_item(random_content)

print resp