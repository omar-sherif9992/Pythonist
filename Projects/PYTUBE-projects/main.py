# from pytube import YouTube
# # from pytube import Playlist
# # from pytube import Channel
# #
# #
# import os
# def main():
#     link="https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y"
#     video=YouTube(url=link)
#     print(video.thumbnail_url) the thumbnali image
#     print(video.author)==> the author
# #     # print(dir(video)) ==> all attributes
# #     # print(f"The Video title is: \n{video.title}\n-------------------")
# #     # print(f"The Video description is: \n{video.description}\n-------------------")
# #     # print(f"The Video views is: \n{video.views}\n-------------------")
# #     # print(f"The Video rating is: \n{video.rating}\n-------------------")
# #     # print(f"The Video duration is: \n{video.length/60}:{video.length%60}\n-------------------")
# #     # print(f"The Video url is: \n{video.watch_url}\n-------------------")
# #     # for stream in video.streams:
# #     #     print(stream)
# #     # for stream in video.streams.filter(progressive=True):#progressive=True means that it contains video with audio
# #     #     print(stream)
# #     # for stream in video.streams.filter(progressive=True,res='720p'):#progressive=True means that it contains video with audio
# #     #     print(stream)
# #     # for stream in video.streams.filter(progressive=True,subtype='mp4'):#progressive=True means that it contains video with audio
# #     #     print(stream)
# #     # print(video.streams.get_highest_resolution())
# #     # print(video.streams.get_lowest_resolution())
# #     # print(video.streams.get_audio_only())
# #     # print(video.js)==>useless
# #     # print(video.keywords) ==> the video keywords
# #     # print(video.js_url)==>useless
# #     # video.streams.get_lowest_resolution().download(output_path=os.getcwd(),filename="Choose filename")
# #     # video.register_on_complete_callback(lambda :print('Download Done'))
# #     # playlist_link="https://youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y"
# #     # playlist=Playlist(playlist_link)
# #     # for video in playlist.videos:
# #     #     video.streams.get_lowest_resolution().download(output_path=os.getcwd(),filename="choose filename")==> download every video in the playlist
# #     for url in playlist.video_urls:
# #         try:
# #             yt = YouTube(url)
# #         except VideoUnavailable:
# #           print(f'Video {url} is unavaialable, skipping.')
# #         else:
# #           print(f'Downloading video: {url}')
# #
# #           yt.streams.first().download()
# #
# #
# #     c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
# #     print(f'Downloading videos by: {c.channel_name}')
# #
# #     for video in c.videos:
# #         video.streams.first().download()
# #
# #
# if __name__=="__main__":
#     main()