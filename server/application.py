from flask import Flask, request, jsonify
from configuration import *
from opencv import adaptors
from opencv.cv import *
from PIL import Image

app = Flask(__name__)

@app.route('/test')
def test():
    return "worked 2"

@app.route('/detectfaces/1', methods=['POST'])
def detect_faces_1():
    if 'image' not in request.files:
        return jsonify(ERROR_NOIMAGE)
    
    file = request.files['image']
    
    try:
        pil_image = Image.open(file)
    except Exception, e:
        if MASK_ERRORS:
            return ERROR_IMAGEERROR
        raise e
    
    image = adaptors.PIL2Ipl(pil_image)
    
    grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)  
    cvCvtColor(image, grayscale, CV_BGR2GRAY)
    storage = cvCreateMemStorage(0)
    cvClearMemStorage(storage)
    cvEqualizeHist(grayscale, grayscale)
    cascade = cvLoadHaarClassifierCascade('%s/haarcascade_frontalface_default.xml' % HAARCASCADES_DIR, cvSize(1,1))
    faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2, CV_HAAR_DO_CANNY_PRUNING, cvSize(100,100))

    if faces.total > 0:
        return_data = { 'status':'success', 'faces':[] }
        for face in faces:
            return_data['faces'].append({ 'sw':{'x':face.x, 'y':face.y}, 'ne':{'x':face.x+face.width, 'y':face.y+face.height }})
        return jsonify(return_data)
    
    return jsonify({'status':'success', 'faces':[] })
        


    