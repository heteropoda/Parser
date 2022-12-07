
import json
import re
from parse import Parser
from tool.time import format_time_twitter


class P1(Parser):
    
    def parse(self, text, path, task):
        text = json.loads(text)
        entries = text.get('data',{}).get('threaded_conversation_with_injections',{}).get('instructions',[{}])[0].get('entries')
        if not entries:
            return 

        for entry in entries:
            try:
                entry = entry['content']
                if 'items' in entry:
                    for i in entry['items']:
                        i = i['item']['itemContent'].get('tweet_results',{}).get('result',{})
                        i = i.get('tweet', i)
                        yield self.parse_item(i)
                else:
                    entry = entry['itemContent'].get('tweet_results',{}).get('result',{})
                    entry = entry.get('tweet', entry)
                    yield self.parse_item(entry)
            except Exception as e:
                print(e)
        
    def parse_item(self, tweet):
        if not tweet:
            return
        user_name = tweet['core']['user_results']['result']['legacy']['screen_name']
        tweet = tweet['legacy']
        
        item = {}
        item['id'] = int(tweet['id_str'])
        item['content'] = tweet['full_text']
        content_del = re.findall(r'https://t.co/\S+?$', item['content'])
        item['content'] = item['content'].replace(content_del[0],'') if content_del else item['content']
        item['uname'] = user_name
        item['pub_time'] = format_time_twitter(tweet['created_at'])
        item['url'] = 'https://twitter.com/{}/status/{}'.format(item['uname'],item['id'])
        item['retweet_count'] = tweet['retweet_count']
        item['favorite_count'] = tweet['favorite_count']
        item['reply_count'] = tweet['reply_count']
        item['quote_count'] = tweet['quote_count']
        item['entities'] = []
        for j in tweet.get('entities',{}).get('media',[]):
            item['entities'].append(j['media_url_https'])

        print('信息解析成功 id:<{}>'.format(item['id']))
        return item
        