from flask import Flask,request,jsonify
from pytube import Playlist ,YouTube


app=Flask(__name__)

@app.route('/videeeos',methods=["POST"])
def api():

 if request.method=="POST":
        videos=[]

    # if 'img' in request.files:
        # img=request.files.get('img')
        url=str(request.form.get('url'))

        pd=Playlist(url)
       
        for urll in pd.video_urls:

          yt=YouTube(urll)


          videos.append({"video_url":yt.embed_url,"image_url":yt.thumbnail_url,"title":yt.title,"author":yt.author})




        return jsonify({"playlist_title": pd.title,"videos":videos })




        # if request.method=="POST":
        # videos=[]
        # url0=str(request.form.get('url'))
        # Playlist_d=Playlist(url0)
        # for url in Playlist_d.video_urls:

        #     #  url.streams.get_lowest_resolution().download("dawnloads")
        #      print(f" video done : ${url} ")
        #      videos.append(str(url))



        # print("playList has been dawnloded !!")
        # return jsonify({"videos":videos})


if __name__=="__main__":
    app.run()