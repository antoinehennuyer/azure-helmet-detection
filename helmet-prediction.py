from matplotlib import pyplot as plt, patches
from matplotlib import image
from tkinter import filedialog
from tkinter import *



path = "test_img.jpg"

# SEND TO API HELMET DETECTION

# SEND TO API FACE RECOGNITION

# PRINT IMAGE DETECTION WITH PROBABILITIES

json_test = {
    "id": "694159a4-1e54-4fe3-89ed-79d19942acbf",
    "project": "e1d47eeb-1e08-480c-9e0c-485b59dc6bd6",
    "iteration": "8e6e14f1-98cb-4bda-8314-a9e1dc14eab6",
    "created": "2020-06-11T12:06:12.557Z",
    "predictions": [{
        "probability": 0.0130675444,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0630928,
            "top": 0.0,
            "width": 0.023223646,
            "height": 0.07293058
        }
    }, {
        "probability": 0.0140295494,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.108049639,
            "top": 0.0,
            "width": 0.0244648233,
            "height": 0.0738712549
        }
    }, {
        "probability": 0.0106687471,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.615568638,
            "top": 0.0,
            "width": 0.03121692,
            "height": 0.08884957
        }
    }, {
        "probability": 0.0278099924,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.6549295,
            "top": 0.0,
            "width": 0.0281694531,
            "height": 0.08008353
        }
    }, {
        "probability": 0.0118989786,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.06544384,
            "top": 0.124892011,
            "width": 0.0144571736,
            "height": 0.117843077
        }
    }, {
        "probability": 0.0122352121,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0709262341,
            "top": 0.193950191,
            "width": 0.0129389763,
            "height": 0.120691076
        }
    }, {
        "probability": 0.0116044246,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.117050827,
            "top": 0.192671344,
            "width": 0.0120024234,
            "height": 0.123355672
        }
    }, {
        "probability": 0.0151109612,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.7179198,
            "top": 0.169276655,
            "width": 0.0184859037,
            "height": 0.166989267
        }
    }, {
        "probability": 0.0132711036,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.7635861,
            "top": 0.171888739,
            "width": 0.019250989,
            "height": 0.154738545
        }
    }, {
        "probability": 0.0150951669,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.06538838,
            "top": 0.4519185,
            "width": 0.0222739279,
            "height": 0.0450842679
        }
    }, {
        "probability": 0.0115956049,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.108688317,
            "top": 0.440477818,
            "width": 0.0286952928,
            "height": 0.0497171879
        }
    }, {
        "probability": 0.0164364222,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0150359087,
            "top": 0.5016229,
            "width": 0.0219722278,
            "height": 0.0444563627
        }
    }, {
        "probability": 0.0172976367,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.9789306,
            "top": 0.476376772,
            "width": 0.009192228,
            "height": 0.128354192
        }
    }, {
        "probability": 0.015519808,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.969826,
            "top": 0.5075047,
            "width": 0.0128458142,
            "height": 0.1999824
        }
    }, {
        "probability": 0.0642036647,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.07393543,
            "top": 0.6696323,
            "width": 0.007410802,
            "height": 0.0460856557
        }
    }, {
        "probability": 0.07092433,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.111966036,
            "top": 0.652661741,
            "width": 0.01052098,
            "height": 0.0458382964
        }
    }, {
        "probability": 0.0134804081,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.163093746,
            "top": 0.651105046,
            "width": 0.0123572052,
            "height": 0.0412282944
        }
    }, {
        "probability": 0.0126089361,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0190077014,
            "top": 0.7046538,
            "width": 0.005847454,
            "height": 0.06571472
        }
    }, {
        "probability": 0.0455636419,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.159771577,
            "top": 0.7176104,
            "width": 0.02615872,
            "height": 0.06899792
        }
    }, {
        "probability": 0.02638498,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.16369988,
            "top": 0.7766651,
            "width": 0.0217073858,
            "height": 0.06595212
        }
    }, {
        "probability": 0.0152910175,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.170876443,
            "top": 0.8683987,
            "width": 0.0206655264,
            "height": 0.05992198
        }
    }, {
        "probability": 0.0125033567,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.211906582,
            "top": 0.8752472,
            "width": 0.0169094652,
            "height": 0.0612992644
        }
    }, {
        "probability": 0.02040758,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0156916529,
            "top": 0.936423957,
            "width": 0.0193420723,
            "height": 0.06356603
        }
    }, {
        "probability": 0.0123396991,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.154996812,
            "top": 0.9656239,
            "width": 0.0508527,
            "height": 0.0187094212
        }
    }, {
        "probability": 0.0150770489,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.203824788,
            "top": 0.9516502,
            "width": 0.0333329141,
            "height": 0.0246326327
        }
    }, {
        "probability": 0.0106631359,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.900468349,
            "top": 0.954615653,
            "width": 0.05641049,
            "height": 0.0309557915
        }
    }, {
        "probability": 0.0493624732,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.806796253,
            "top": 0.0262040272,
            "width": 0.158425629,
            "height": 0.146202177
        }
    }, {
        "probability": 0.03998426,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.225781381,
            "top": 0.07988326,
            "width": 0.0803133845,
            "height": 0.175634041
        }
    }, {
        "probability": 0.0233020615,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.409006476,
            "top": 0.312495738,
            "width": 0.159602046,
            "height": 0.154608011
        }
    }, {
        "probability": 0.0104783317,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0114683583,
            "top": 0.418175042,
            "width": 0.133301526,
            "height": 0.109394729
        }
    }, {
        "probability": 0.01013377,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.00868839,
            "top": 0.5314335,
            "width": 0.129653782,
            "height": 0.165848076
        }
    }, {
        "probability": 0.0120971566,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.195995212,
            "top": 0.5766569,
            "width": 0.165448725,
            "height": 0.06832999
        }
    }, {
        "probability": 0.01812329,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0374681652,
            "top": 0.6277304,
            "width": 0.162615523,
            "height": 0.110630095
        }
    }, {
        "probability": 0.0188243259,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0270688981,
            "top": 0.6876386,
            "width": 0.183196619,
            "height": 0.143231928
        }
    }, {
        "probability": 0.0198128521,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0179575756,
            "top": 0.7442258,
            "width": 0.199499488,
            "height": 0.139853656
        }
    }, {
        "probability": 0.0117836231,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.9011552,
            "top": 0.822270036,
            "width": 0.07683277,
            "height": 0.139164269
        }
    }, {
        "probability": 0.01571674,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0,
            "top": 0.908361137,
            "width": 0.0579751134,
            "height": 0.09162885
        }
    }, {
        "probability": 0.0487943031,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.7855031,
            "top": 0.010100171,
            "width": 0.200149834,
            "height": 0.3304776
        }
    }, {
        "probability": 0.0136130871,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.177605838,
            "top": 0.0634309649,
            "width": 0.189279884,
            "height": 0.3676618
        }
    }, {
        "probability": 0.949071467,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.40668878,
            "top": 0.178856164,
            "width": 0.193151683,
            "height": 0.2926548
        }
    }, {
        "probability": 0.06152937,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0,
            "top": 0.2914676,
            "width": 0.177996174,
            "height": 0.328083217
        }
    }, {
        "probability": 0.423641771,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.132958025,
            "top": 0.2547331,
            "width": 0.279403627,
            "height": 0.364828229
        }
    }, {
        "probability": 0.01649123,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0328386948,
            "top": 0.449741155,
            "width": 0.169631988,
            "height": 0.316698283
        }
    }, {
        "probability": 0.0220461991,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.77066797,
            "top": 0.5847912,
            "width": 0.2113958,
            "height": 0.350056827
        }
    }, {
        "probability": 0.012378036,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.0238591433,
            "top": 0.544621766,
            "width": 0.315852821,
            "height": 0.140005827
        }
    }, {
        "probability": 0.0367158651,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.005758062,
            "top": 0.6995345,
            "width": 0.336243153,
            "height": 0.250045478
        }
    }, {
        "probability": 0.0147071965,
        "tagId": "20c17a3b-3a4d-4e6b-99e1-a2beb59dd9ea",
        "tagName": "helmet",
        "boundingBox": {
            "left": 0.609557033,
            "top": 0.00679406524,
            "width": 0.390432954,
            "height": 0.7710924
        }
    }, {
        "probability": 0.02774822,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.07393543,
            "top": 0.6696323,
            "width": 0.007410802,
            "height": 0.0460856557
        }
    }, {
        "probability": 0.02848745,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.111966036,
            "top": 0.652661741,
            "width": 0.01052098,
            "height": 0.0458382964
        }
    }, {
        "probability": 0.0169489123,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.163093746,
            "top": 0.651105046,
            "width": 0.0123572052,
            "height": 0.0412282944
        }
    }, {
        "probability": 0.026860984,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.159771577,
            "top": 0.7176104,
            "width": 0.02615872,
            "height": 0.06899792
        }
    }, {
        "probability": 0.109458581,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.806796253,
            "top": 0.0262040272,
            "width": 0.158425629,
            "height": 0.146202177
        }
    }, {
        "probability": 0.0272426847,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.225781381,
            "top": 0.07988326,
            "width": 0.0803133845,
            "height": 0.175634041
        }
    }, {
        "probability": 0.0114577254,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.785373151,
            "top": 0.175724149,
            "width": 0.07907182,
            "height": 0.1603874
        }
    }, {
        "probability": 0.0101985857,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.0374681652,
            "top": 0.6277304,
            "width": 0.162615523,
            "height": 0.110630095
        }
    }, {
        "probability": 0.0184720214,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.0270688981,
            "top": 0.6876386,
            "width": 0.183196619,
            "height": 0.143231928
        }
    }, {
        "probability": 0.0123102767,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.0179575756,
            "top": 0.7442258,
            "width": 0.199499488,
            "height": 0.139853656
        }
    }, {
        "probability": 0.04994361,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.7855031,
            "top": 0.010100171,
            "width": 0.200149834,
            "height": 0.3304776
        }
    }, {
        "probability": 0.1300907,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.132867619,
            "top": 0.265602767,
            "width": 0.276214361,
            "height": 0.313104928
        }
    }, {
        "probability": 0.08365871,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.400942266,
            "top": 0.212032929,
            "width": 0.2097122,
            "height": 0.317794919
        }
    }, {
        "probability": 0.0154359033,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.002693221,
            "top": 0.2676543,
            "width": 0.2219909,
            "height": 0.372318923
        }
    }, {
        "probability": 0.0337458365,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.0124316365,
            "top": 0.64940995,
            "width": 0.326274753,
            "height": 0.214145541
        }
    }, {
        "probability": 0.01080454,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.6463239,
            "top": 0.6233881,
            "width": 0.353666067,
            "height": 0.3583042
        }
    }, {
        "probability": 0.0179326888,
        "tagId": "f05a5bf2-2019-4b0e-94ba-d3bb58ae7e50",
        "tagName": "no helmet",
        "boundingBox": {
            "left": 0.100131929,
            "top": 0.1361165,
            "width": 0.6506306,
            "height": 0.8638735
        }
    }]
}

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
img = plt.imread(root.filename)
figure, ax = plt.subplots(1)
prediction_list = json_test["predictions"]
for predic in prediction_list:
    if predic["probability"] > 0.5:
        print("prediction detected ! It is:" + predic["tagName"])
        left_corner = predic["boundingBox"]["left"] * img.shape[1]
        top_corner = predic["boundingBox"]["top"] * img.shape[0]
        width = predic["boundingBox"]["width"] * img.shape[1]
        height = predic["boundingBox"]["height"] * img.shape[0]
        rect = patches.Rectangle((left_corner, top_corner), width, height, edgecolor='r', facecolor="none")
        ax.add_patch(rect)
        ax.imshow(img)
        plt.show()
root.destroy()
# PRINT IF SAS OPEN OR NOT

# WRITE ON CSV THE RESULT
