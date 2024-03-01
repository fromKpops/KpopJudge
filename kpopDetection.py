import streamlit as st
import numpy as np
from PIL import Image
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import affList as afl
import base64
import random

class CNN(nn.Module):

  def __init__(self):
    super(CNN, self).__init__()
    self.cn1 = nn.Conv2d(3, 6, 5)
    self.pool1 = nn.MaxPool2d(2, 2)
    self.cn2 = nn.Conv2d(6, 16, 5)
    self.pool2 = nn.MaxPool2d(2, 2)
    self.cn3 = nn.Conv2d(16, 32, 4)
    self.dropout = nn.Dropout2d()
    self.fc1 = nn.Linear(32*10*10, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 5)
  
  def forward(self, x):
    x = F.relu(self.cn1(x))
    x = self.pool1(x)
    x = F.relu(self.cn2(x))
    x = self.pool2(x)
    x = F.relu(self.cn3(x))
    x = self.dropout(x)
    x = x.view(-1, 32*10*10)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)
        
    return x
  
#読み込んだ画像の中からウマ娘の顔を検出し，名前とBoxを描画する関数
def detect(image, model):
  #顔検出器の準備
  classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

  #画像をグレースケール化
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  #画像の中から顔を検出
  faces = classifier.detectMultiScale(gray_image, scaleFactor = 1.1)
  #1人以上の顔を検出した場合
  if len(faces)>0:
      for face in faces:
          x, y, width, height = face
          detect_face = image[y:y+height, x:x+width]
          detect_face = cv2.resize(detect_face, (64, 64))
          if detect_face.shape[0] < 64:
              print("tuuka")
              continue
          detect_face = cv2.resize(detect_face, (64,64))
          transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
          detect_face = transform(detect_face)
          detect_face = detect_face.view(1,3,64,64)

          output = model(detect_face)
          print(f"output{output}")
          name_type = output.argmax(dim=1, keepdim=True)
          print(name_type)
          name = type_to_name(name_type)
  else:
    name = None
  return name


def type_to_name(name_type):
  if name_type == 0:
      name = "HYBE"
  elif name_type == 1:
      name = "JYP"
  elif name_type == 2:
      name = "SM"
  elif name_type == 3:
      name = "STARSHIP"
  elif name_type == 4:
      name = "YG"

  return name


def main():
  st.set_page_config(layout="centered")
  image_path = "./background5.png"

# 画像ファイルをbase64形式にエンコード
  with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()
  backscreen = f'''
          <style>
          .stApp {{
              background-image: url('data:image/jpeg;base64,{encoded_image}');
              background-size: cover;
              background-repeat: no-repeat;
          }}
          </style>
          '''
  st.markdown(backscreen, unsafe_allow_html=True)

  if 'isTurned' not in st.session_state:
     st.session_state['isTurned'] = True
  if 'output' not in st.session_state:
     st.session_state['output'] = None
     print(f"何と{st.session_state['isTurned']}です")
     print(f"何と{st.session_state['output']}です")
  #タイトルの表示
  st.markdown('''<h1 style="color: dimgrey;">KPOP事務所顔AI診断</h1>''', unsafe_allow_html=True)
  #アプリの説明の表示
  st.markdown("韓国の事務所別の顔を識別するアプリです")

  is_men = st.radio("性別を選択", ("男性", "女性"), horizontal=True, args=[1, 0])

  if is_men == "男性":
    st.session_state['sex'] = '男性'
  else:
    st.session_state['sex'] = '女性'
  
  img_upload()

  st.button('判定結果を見る', on_click=change_page, disabled=st.session_state['isTurned'])
  num = random.randint(0, len(afl.ad_urls)) - 1
  print(num)
  ad_url = afl.ad_urls[num]
  ad_img = afl.ad_imgs[num]
  ad_html = f"""
              <center>
                <!--<h2>広告</h2>-->
                <a href={ad_url}>
                    <img src={ad_img} width='300' alt='' style='vertical-align: middle; border: 0 none;'>
                </a>
              </center>
 
            """
  print(ad_url)
  print(ad_img)
  st.markdown(ad_html, unsafe_allow_html=True)


def next_page():
  st.balloons()
  image_path = "./background5.png"
  # 画像ファイルをbase64形式にエンコード
  with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()
  backscreen = f'''
          <style>
          .stApp {{
              background-image: url('data:image/jpeg;base64,{encoded_image}');
              background-size: cover;
              background-repeat: no-repeat;
          }}
          </style>
          '''
  st.markdown(backscreen, unsafe_allow_html=True)

  st.markdown('''<h1 style="color: dimgrey;">KPOP事務所顔AI診断</h1>''', unsafe_allow_html=True)
  output = st.session_state['output']
  path = f"./output_img/{output}_out.png"
  img = np.array(Image.open(path))
  st.image(img)
  urls = afl.url_dic[output]
  imgs = afl.img_dic[output]
  intros = afl.intro_dic[output]

  for i in range(len(urls)):
    container =  st.container()
    html = f"""<div class='shr_item' style='position:relative; min-height:158px; margin:12px 0; padding:9px 10px; border:1px solid #dbdbdb; border-radius:1px; background-color:#fff;'><div class='item_dtl' style='position:relative; height:158px; padding:5px; border:1px solid #f0f1f4;'><span class='thmb' style='float:left; overflow:hidden; width:156px; height:156px; margin-right:9px; border:1px solid #e7e7e7;'><a href={urls[i]}><img src={imgs[i]} width='156' alt='' style='vertical-align: middle; border: 0 none;'></a></span><p class='tit' style='overflow:hidden; max-height:68px; margin-bottom:7px; line-height:17px; color:#000;'>[Qoo10] {intros[i]}</p><span class='url' style='position:absolute; left:170px; bottom:10px; display:block; font-weight:bold; color:#9197a3;'>WWW.QOO10.JP</span></div></div>"""
    container.markdown(html ,unsafe_allow_html=True)
  col1, col2 = st.columns([9,1])
  col1.write("")
  col2.button('戻る', on_click=back_page())



def link_set(link):
  container = st.container(border=True, height=150)
  col1, col2 = container.columns([3,1])
  col1.header(f"check out this [ここをクリック]({link})")
  col2.image('https://gd.image-qoo10.jp/li/469/522/5523522469.g_400-w-st_g.jpg')  

def change_page():
   st.session_state['page_control'] = 1

def back_page():
   st.session_state['page_control'] = 0
   st.session_state['output'] = None
   st.session_state['isTurned'] = True
   print('backpage 関数')
   
   
def img_upload():
  image = st.file_uploader("画像をアップロードしてください", type=['jpg','jpeg', 'png'])
  if st.session_state['sex'] == '男性':
    model = CNN()
    checkpoint = torch.load("./men_cnn.pt", map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    if image != None:
      #画像の読み込み
      image = np.array(Image.open(image))
      #画像から顔検出を行う
      st.session_state['output'] = detect(image, model)
      if st.session_state['output'] == None:
        st.markdown(""":red[顔を認識できませんでした。別の画像を試してください。] """, unsafe_allow_html=True)
      print(f"{st.session_state['output']}です")
      if st.session_state['output'] != None:
         st.session_state['isTurned'] = False
    print('男性を選択')
    
  elif st.session_state['sex'] == '女性':
    model = CNN()
    checkpoint = torch.load("./women_cnn.pt", map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    if image != None:
      #画像の読み込み
      image = np.array(Image.open(image))
      #画像からウマ娘の顔検出を行う¥
      st.session_state['output'] = detect(image, model)
      if st.session_state['output'] == None:
        st.markdown(""":red[顔を認識できませんでした。別の画像を試してください。] """, unsafe_allow_html=True)
      print(f"{st.session_state['output']}")
    print('女性を選択') 

  if st.session_state['output'] != None:
    st.session_state['isTurned'] = False
  
  

if __name__ == "__main__":
  if ("page_control" in st.session_state and st.session_state["page_control"] == 1):
      next_page()
  else:
    st.session_state["page_control"] = 0
    main()