from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera, IPWebCam
# Create your views here.

def index(request):
	return render(request, 'streamapp/home.html')

def gen(camera):
	while True:
		frame, saludo = camera.get_frame()
		print(saludo)
		yield ((b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'))
		yield count

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')
